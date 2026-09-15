"""Build the AutomationByExperts Apify actor catalog.

Reads public data only (the Apify Store API and the website llms.txt) plus the committed
data/tasks.json snapshot, then regenerates README.md, categories/, actors/, llms.txt,
llms-full.txt and data/actors.json. Safe to run in CI: it needs no token.
Standard library only.
"""
from __future__ import annotations

import json
import pprint
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'

USERNAME = 'fayoussef'
REFERRAL = 'fpr=youssef'
SITE = 'https://automationbyexperts.com'
OWNER = 'automationbyexperts'
REPO = 'web-scraping-apis'
REPO_URL = f'https://github.com/{OWNER}/{REPO}'
RAW_URL = f'https://raw.githubusercontent.com/{OWNER}/{REPO}/main'
UTM = f'utm_source=github&utm_medium=referral&utm_campaign={REPO}'
CONTACT_EMAIL = 'youssefarhan24@gmail.com'
AUTHOR = 'Youssef Farhan'
BRAND = 'AutomationByExperts'
DEFAULT_CATEGORY = ('Developer Tools & APIs', 'developer-tools', 'Scraping APIs and monitoring tools for developers.')

# Build fails if any of these reach a generated file.
FORBIDDEN = ('dataimpulse', 'sk-or-v1-', 'CAP-', 'apify_api_')
PRICE = re.compile(r'\$\s?\d')
CODE_BLOCK = re.compile(r'```.*?```', re.DOTALL)
REL_LINK = re.compile(r'\]\((?!https?://|mailto:|#)([^)\s]+)\)')

PRICING_LABELS = {
    'PAY_PER_EVENT': 'Pay per result or event',
    'PRICE_PER_DATASET_ITEM': 'Pay per result',
    'FLAT_PRICE_PER_MONTH': 'Monthly rental',
    'FREE': 'Free',
}


# ---------------------------------------------------------------- fetching

def fetch(url: str) -> bytes:
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': f'{REPO}-catalog-builder'})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # network hiccup: retry with a capped backoff
            last = exc
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f'GET {url} failed: {last}')


def fetch_json(url: str):
    return json.loads(fetch(url).decode('utf-8'))


def store_actors() -> list[dict]:
    items, offset = [], 0
    while True:
        page = fetch_json(f'https://api.apify.com/v2/store?username={USERNAME}&limit=100&offset={offset}')['data']
        items.extend(page['items'])
        offset += len(page['items'])
        if not page['items'] or offset >= page['total']:
            return items


def extra_actor(name: str) -> dict | None:
    """Actors the Store search omits (rental actors), fetched one by one."""
    try:
        data = fetch_json(f'https://api.apify.com/v2/acts/{USERNAME}~{name}')['data']
    except RuntimeError:
        print(f'WARNING: extra actor {name} not found', file=sys.stderr)
        return None
    if not data.get('isPublic') or data.get('isDeprecated'):
        return None
    pricing = (data.get('pricingInfos') or [{}])[-1]
    return {
        'name': data['name'],
        'title': data.get('title') or data['name'],
        'description': data.get('description') or '',
        'stats': data.get('stats') or {},
        'actorReviewRating': None,
        'actorReviewCount': 0,
        'currentPricingInfo': {'pricingModel': pricing.get('pricingModel')},
    }


def site_categories() -> tuple[list[tuple[str, str, str]], dict[str, str]]:
    """Parse the website llms.txt: category list and actor slug -> category name."""
    text = fetch(f'{SITE}/llms.txt').decode('utf-8')
    cats = re.findall(rf'^- \[(.+?)\]\({re.escape(SITE)}/apify/category/([\w-]+)\): ?(.*)$', text, re.MULTILINE)
    mapping, current = {}, None
    for line in text.splitlines():
        if line.startswith('### '):
            current = line[4:].strip()
        elif current and (m := re.match(rf'^- \[.+?\]\({re.escape(SITE)}/apify/([\w-]+)\)', line)):
            mapping[m.group(1)] = current
        elif line.startswith('## ') and current:
            current = None
    # The site bakes its own actor count into each blurb, which goes stale here.
    return [(clean(n), s, clean(re.sub(r'\(\d+ actors?\)', '', d))) for n, s, d in cats], mapping


# ---------------------------------------------------------------- text helpers

def clean(text: str) -> str:
    text = (text or '').replace('—', ' - ').replace('–', '-')
    return re.sub(r'\s+', ' ', text).strip()


def clean_obj(value):
    if isinstance(value, str):
        return value.replace('—', ' - ').replace('–', '-')
    if isinstance(value, dict):
        return {k: clean_obj(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean_obj(v) for v in value]
    return value


def short(text: str, limit: int = 170) -> str:
    text = clean(text)
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(' ', 1)[0].rstrip(',.;:') + '...'


def cell(text: str) -> str:
    return text.replace('|', '\\|')


def anchor(heading: str) -> str:
    """GitHub heading anchor."""
    return re.sub(r'[^a-z0-9 _-]', '', heading.lower()).replace(' ', '-')


def apify_url(slug: str) -> str:
    return f'https://apify.com/{USERNAME}/{slug}?{REFERRAL}'


def task_url(slug: str, task: str) -> str:
    return f'https://apify.com/{USERNAME}/{slug}/examples/{task}?{REFERRAL}'


def site_url(slug: str) -> str:
    return f'{SITE}/apify/{slug}?{UTM}'


# ---------------------------------------------------------------- model

def load_catalog() -> dict:
    overrides = json.loads((DATA / 'overrides.json').read_text(encoding='utf-8'))
    tasks = json.loads((DATA / 'tasks.json').read_text(encoding='utf-8')) if (DATA / 'tasks.json').exists() else {}
    previous = json.loads((DATA / 'actors.json').read_text(encoding='utf-8')) if (DATA / 'actors.json').exists() else None

    raw = store_actors()
    seen = {a['name'] for a in raw}
    for name in overrides.get('extraActors', []):
        if name not in seen and (extra := extra_actor(name)):
            raw.append(extra)
    raw = [a for a in raw if a['name'] not in set(overrides.get('exclude', []))]

    try:
        categories, mapping = site_categories()
    except RuntimeError as exc:
        if not previous:
            raise
        print(f'WARNING: website llms.txt unavailable ({exc}), reusing previous categories', file=sys.stderr)
        categories = [(c['name'], c['slug'], c['description']) for c in previous['categories']]
        mapping = {a['slug']: a['category'] for a in previous['actors']}

    by_name = {n: (n, s, d) for n, s, d in categories}
    actors = []
    for a in raw:
        slug = a['name']
        cat_name = overrides.get('category', {}).get(slug) or mapping.get(slug) or DEFAULT_CATEGORY[0]
        if slug not in mapping:
            print(f'NOTE: {slug} is not on the website llms.txt, filed under {cat_name}', file=sys.stderr)
        if cat_name not in by_name:
            by_name[cat_name] = DEFAULT_CATEGORY if cat_name == DEFAULT_CATEGORY[0] else (cat_name, anchor(cat_name), '')
            categories.append(by_name[cat_name])
        stats = a.get('stats') or {}
        actors.append({
            'slug': slug,
            'title': clean(overrides.get('title', {}).get(slug) or a.get('title') or slug),
            'description': clean(a.get('description')),
            'category': cat_name,
            'categorySlug': by_name[cat_name][1],
            'apifyUrl': apify_url(slug),
            'websiteUrl': f'{SITE}/apify/{slug}',
            'guideUrl': f'{REPO_URL}/blob/main/actors/{slug}.md',
            'users': stats.get('totalUsers') or 0,
            'users30Days': stats.get('totalUsers30Days') or 0,
            'rating': a.get('actorReviewRating'),
            'reviews': a.get('actorReviewCount') or 0,
            'pricingModel': (a.get('currentPricingInfo') or {}).get('pricingModel'),
            'useCases': [
                {
                    'title': clean(t['title']),
                    'description': clean(t.get('description')),
                    'url': task_url(slug, t['name']),
                    'input': clean_obj(t.get('input') or {}),
                }
                for t in tasks.get(slug, [])
            ],
        })

    actors.sort(key=lambda x: (-x['users'], x['slug']))
    used = {a['category'] for a in actors}
    cats = [{'name': n, 'slug': s, 'description': d} for n, s, d in categories if n in used]

    if previous and len(actors) < 0.8 * len(previous['actors']):
        sys.exit(f'Refusing to build: {len(actors)} actors vs {len(previous["actors"])} last time. Check the Store API.')
    return {'categories': cats, 'actors': actors, 'previousUpdated': previous and previous.get('updated')}


# ---------------------------------------------------------------- rendering

def run_steps() -> str:
    return (
        '1. Open the actor on Apify and sign in, or create a free Apify account.\n'
        '2. Fill in the input form, or paste the example input below, and click **Start**.\n'
        '3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.\n'
    )


def code_samples(slug: str, run_input: dict) -> str:
    as_json = json.dumps(run_input, indent=2, ensure_ascii=False)
    as_py = pprint.pformat(run_input, width=88, sort_dicts=False)
    compact = json.dumps(run_input, ensure_ascii=False).replace("'", "'\\''")
    return f"""### Example input

```json
{as_json}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {as_py}
run = client.actor("{USERNAME}/{slug}").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript / Node.js

```bash
npm install apify-client
```

```javascript
import {{ ApifyClient }} from 'apify-client';

const client = new ApifyClient({{ token: '<YOUR_APIFY_TOKEN>' }});
const input = {as_json};
const run = await client.actor('{USERNAME}/{slug}').call(input);
const {{ items }} = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/{USERNAME}~{slug}/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \\
  -H "Content-Type: application/json" \\
  -d '{compact}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools={USERNAME}/{slug}
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?{REFERRAL}).
"""


def render_actor(a: dict, catalog: dict, updated: str) -> str:
    title, slug = a['title'], a['slug']
    related = [r for r in catalog['actors'] if r['category'] == a['category'] and r['slug'] != slug][:6]
    pricing = PRICING_LABELS.get(a['pricingModel'] or '', 'Set on the Apify Store page')
    rating = f"{a['rating']:.1f} out of 5 ({a['reviews']} reviews)" if a['rating'] and a['reviews'] else None
    example = a['useCases'][0]['input'] if a['useCases'] and a['useCases'][0]['input'] else None

    out = [f'# {title}', '']
    out.append(f"**{title}** is a ready-to-run Apify actor from {BRAND} by {AUTHOR}. {a['description']}")
    out.append('')
    out.append(f"[Run it on Apify]({a['apifyUrl']}) | [Actor page on {BRAND}]({site_url(slug)}) | [All {a['category']}](../categories/{a['categorySlug']}.md)")
    out += ['', '## Key facts', '', '| | |', '|---|---|']
    out.append(f"| Category | [{a['category']}](../categories/{a['categorySlug']}.md) |")
    out.append('| Runs on | Apify cloud, nothing to install and no server to manage |')
    out.append('| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |')
    out.append(f'| Pricing model | {pricing} (the current rate is shown on the [Store page]({a["apifyUrl"]})) |')
    if rating:
        out.append(f'| Rating | {rating} |')
    out.append(f'| Maintainer | [{AUTHOR}, {BRAND}]({SITE}/?{UTM}) |')
    out.append(f'| Catalog updated | {updated} |')

    if a['useCases']:
        out += ['', f'## What you can do with {title}', '']
        for u in a['useCases']:
            line = f"- **[{u['title']}]({u['url']})**"
            if u['description']:
                line += f": {short(u['description'], 220)}"
            out.append(line)

    out += ['', f'## How to use {title}', '', '### No code', '', run_steps()]
    if example is not None:
        out.append(code_samples(slug, example))
    else:
        out.append(code_samples(slug, {}).replace(
            '### Example input\n', '### Example input\n\nOpen the input form on the Store page to see every field. An empty input runs the defaults.\n', 1))

    out += ['## FAQ', '']
    faq = [
        (f'Is {title} free to try?',
         f"Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?{REFERRAL}). The current rate is shown on the [Store page]({a['apifyUrl']})."),
        ('Do I need to know how to code?',
         'No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.'),
        ('What formats can I export the data in?',
         'JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.'),
        ('Can AI agents use it?',
         f'Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools={USERNAME}/{slug}` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.'),
        ('Can I get a custom version?',
         f'Yes. {AUTHOR} builds custom scrapers and automations. Email {CONTACT_EMAIL} or visit [{BRAND}]({SITE}/?{UTM}).'),
    ]
    for q, ans in faq:
        out += [f'### {q}', '', ans, '']

    if related:
        out += [f"## Related {a['category']}", '']
        out += [f"- [{r['title']}]({r['slug']}.md): {short(r['description'], 140)}" for r in related]
        out.append('')

    out += ['## More', '']
    out.append(f'- Full catalog: [all {len(catalog["actors"])} actors](../README.md)')
    out.append(f'- Website page: [{site_url(slug).split("?")[0]}]({site_url(slug)})')
    out.append(f"- Markdown version for AI tools: [{SITE}/apify/{slug}.md]({SITE}/apify/{slug}.md)")
    out.append('')
    return '\n'.join(out)


def actor_table(actors: list[dict], prefix: str) -> list[str]:
    rows = ['| Actor | What it does | Example use cases | Guide |', '|---|---|---|---|']
    for a in actors:
        cases = '<br>'.join(f"[{cell(u['title'])}]({u['url']})" for u in a['useCases'][:2]) or '-'
        rows.append(
            f"| [{cell(a['title'])}]({a['apifyUrl']}) | {cell(short(a['description']))} | {cases} | [Guide]({prefix}{a['slug']}.md) |"
        )
    return rows


def render_readme(catalog: dict, updated: str) -> str:
    actors, cats = catalog['actors'], catalog['categories']
    n = len(actors)
    users = sum(a['users'] for a in actors)
    cases = sum(len(a['useCases']) for a in actors)
    cat_names = ', '.join(c['name'] for c in cats)

    out = [
        f'# Web Scraping APIs: {n} Ready-to-Run Scrapers and AI Tools (Apify)',
        '',
        f'> {n} ready-to-run Apify actors by {BRAND} ({AUTHOR}): car and real estate scrapers, e-commerce and price data, '
        'lead generation, bulk AI tools and SEO audits. No code and no servers: run them in the cloud and export to JSON, CSV or Excel.',
        '',
        f'**{n} actors** | **{users:,} users** | **{cases} ready-made use cases** | Updated {updated}',
        '',
        f'[Website]({SITE}/apify?{UTM}) | [All actors on Apify](https://apify.com/{USERNAME}?{REFERRAL}) | '
        '[llms.txt for AI](llms.txt) | [JSON catalog](data/actors.json)',
        '',
        '## What is this?',
        '',
        f'This repository is the open catalog of **{BRAND}**, the actor catalogue of {AUTHOR}, an independent Python developer '
        'who builds and maintains production web scrapers on the Apify platform. Every actor listed here is a hosted cloud tool: '
        'paste a URL or a search term, click Start, and download structured data. The catalog covers '
        f'{cat_names}. It is rebuilt every week from the live Apify Store, so the list stays current.',
        '',
        '## Contents',
        '',
    ]
    for c in cats:
        count = sum(1 for a in actors if a['category'] == c['name'])
        out.append(f"- [{c['name']}](#{anchor(c['name'])}) ({count})")
    out += ['- [How to run an Apify actor](#how-to-run-an-apify-actor)', '- [FAQ](#faq)', '- [Need a custom scraper?](#need-a-custom-scraper)', '']

    for c in cats:
        members = [a for a in actors if a['category'] == c['name']]
        out += [f"## {c['name']}", '']
        if c['description']:
            out += [c['description'], '']
        out += actor_table(members, 'actors/')
        out += ['', f"More detail: [{c['name']} guide](categories/{c['slug']}.md) | [on the website]({SITE}/apify/category/{c['slug']}?{UTM})", '']

    out += [
        '## How to run an Apify actor',
        '',
        '**No code:** open any actor above, sign in to Apify (a free account works), fill in the form and click Start. '
        'Results download as JSON, CSV, Excel, XML or HTML.',
        '',
        '**Python:**',
        '',
        '```python',
        'from apify_client import ApifyClient',
        '',
        'client = ApifyClient("<YOUR_APIFY_TOKEN>")',
        f'run = client.actor("{USERNAME}/<actor-name>").call(run_input={{}})',
        'items = client.dataset(run["defaultDatasetId"]).list_items().items',
        '```',
        '',
        '**JavaScript:**',
        '',
        '```javascript',
        "import { ApifyClient } from 'apify-client';",
        '',
        "const client = new ApifyClient({ token: '<YOUR_APIFY_TOKEN>' });",
        f"const run = await client.actor('{USERNAME}/<actor-name>').call({{}});",
        'const { items } = await client.dataset(run.defaultDatasetId).listItems();',
        '```',
        '',
        '**AI agents (MCP):** connect `https://mcp.apify.com?tools=' + USERNAME + '/<actor-name>` in Claude, ChatGPT, Cursor or any MCP client.',
        '',
        'Every actor guide has a ready-to-paste example input and snippets with the real actor name.',
        '',
        '## FAQ',
        '',
        '### What is an Apify actor?',
        '',
        'An actor is a cloud program that runs on the [Apify](https://apify.com/?' + REFERRAL + ') platform. It takes an input '
        '(a URL, a search term, a list of products), does the scraping or automation, and stores the results in a dataset you can download or read through an API.',
        '',
        '### Are these scrapers free to try?',
        '',
        f'Yes. Every actor can be started with a free Apify account. Free runs have usage limits, and bigger jobs need an [Apify plan](https://apify.com/pricing?{REFERRAL}). '
        'Current rates are shown on each Store page.',
        '',
        '### Do I need to know how to code?',
        '',
        'No. Each actor has an input form in the Apify Console. Code is optional, for people who want to call the actors from their own apps.',
        '',
        '### Can ChatGPT, Claude or other AI agents use these actors?',
        '',
        'Yes, through the Apify MCP server. Add `https://mcp.apify.com?tools=' + USERNAME + '/<actor-name>` to any MCP client and the agent can run the actor and read the data.',
        '',
        '### How do I schedule a scraper or send the data somewhere?',
        '',
        'Save your input as a task in the Apify Console, add a schedule, and connect an integration such as Make, Zapier, n8n, Google Drive or a webhook.',
        '',
        '### Can I get a scraper for a site that is not listed?',
        '',
        f'Yes. {AUTHOR} builds custom scrapers and automations. See below.',
        '',
        '## Need a custom scraper?',
        '',
        f'- Email: {CONTACT_EMAIL}',
        f'- Website: [{BRAND}]({SITE}/?{UTM})',
        f'- Got a site in mind? [Suggest it here]({SITE}/apify?{UTM})',
        '',
        '## License',
        '',
        'The catalog text and code snippets are MIT licensed. Actor names and Store content belong to their author.',
        '',
    ]
    return '\n'.join(out)


def render_category(c: dict, catalog: dict, updated: str) -> str:
    members = [a for a in catalog['actors'] if a['category'] == c['name']]
    others = [o for o in catalog['categories'] if o['name'] != c['name']]
    out = [
        f"# {c['name']}: Apify Actors by {BRAND}",
        '',
        f"{len(members)} ready-to-run {c['name'].lower()} on Apify, built and maintained by {AUTHOR}. "
        + (c['description'] + ' ' if c['description'] else '')
        + 'Each one runs in the cloud with no code and exports to JSON, CSV or Excel.',
        '',
        f'Updated {updated}.',
        '',
    ]
    out += actor_table(members, '../actors/')
    out += ['', '## Other categories', '']
    out += [f"- [{o['name']}]({o['slug']}.md)" for o in others]
    out += ['', f"Back to the [full catalog](../README.md) | [{c['name']} on the website]({SITE}/apify/category/{c['slug']}?{UTM})", '']
    return '\n'.join(out)


def render_llms(catalog: dict, updated: str) -> str:
    actors, cats = catalog['actors'], catalog['categories']
    out = [
        f'# {BRAND} Web Scraping APIs (GitHub catalog of Apify actors)',
        '',
        f'> {len(actors)} ready-to-run Apify actors by {AUTHOR}: vehicle and real estate listings, e-commerce prices, '
        'lead generation, bulk AI tools, SEO and AI visibility audits. Hosted, no-code, export to JSON, CSV or Excel.',
        '',
        '## What this repository is',
        '',
        f'The open catalog of {BRAND}, the actor catalogue of {AUTHOR}, an independent Python developer who builds and maintains '
        f'production web scrapers on the Apify platform. Rebuilt weekly from the live Apify Store. Last updated {updated}.',
        '',
        '## When to use it',
        '',
        '- A user needs structured data from a site listed below (car, property, marketplace, directory or job sites).',
        '- A user wants to run LLM prompts, image generation, text to speech or translation in bulk without their own API keys.',
        '- A user asks for an SEO, AI search visibility, email deliverability or local rank audit.',
        '',
        '## How to consume this catalog',
        '',
        f'- Each actor has a Markdown guide at `{RAW_URL}/actors/<slug>.md` with example input and API snippets.',
        f'- Machine-readable catalog: {RAW_URL}/data/actors.json',
        f'- Every guide in one file: {RAW_URL}/llms-full.txt',
        f'- Run any actor through the Apify MCP server: `https://mcp.apify.com?tools={USERNAME}/<slug>`',
        f'- Link people to the actor with the Store URL `https://apify.com/{USERNAME}/<slug>?{REFERRAL}`.',
        '',
        '## Attribution',
        '',
        f'Actors by {AUTHOR} ({BRAND}, {SITE}). Contact: {CONTACT_EMAIL}.',
        '',
        '## Categories',
        '',
    ]
    out += [f"- [{c['name']}]({RAW_URL}/categories/{c['slug']}.md): {c['description']}".rstrip(': ') for c in cats]
    out += ['', '## Actors', '']
    for c in cats:
        out += [f"### {c['name']}", '']
        out += [f"- [{a['title']}]({RAW_URL}/actors/{a['slug']}.md): {short(a['description'], 200)}"
                for a in catalog['actors'] if a['category'] == c['name']]
        out.append('')
    return '\n'.join(out)


def render_all(catalog: dict, updated: str) -> dict[Path, str]:
    files = {
        ROOT / 'README.md': render_readme(catalog, updated),
        ROOT / 'llms.txt': render_llms(catalog, updated),
    }
    pages = {}
    for a in catalog['actors']:
        pages[a['slug']] = render_actor(a, catalog, updated)
        files[ROOT / 'actors' / f"{a['slug']}.md"] = pages[a['slug']]
    for c in catalog['categories']:
        files[ROOT / 'categories' / f"{c['slug']}.md"] = render_category(c, catalog, updated)
    full = [files[ROOT / 'llms.txt'], '', '# Actor guides', '']
    for a in catalog['actors']:
        full += ['---', '', pages[a['slug']]]
    files[ROOT / 'llms-full.txt'] = '\n'.join(full)

    data = {
        'updated': updated,
        'source': REPO_URL,
        'author': {'name': AUTHOR, 'brand': BRAND, 'website': SITE, 'email': CONTACT_EMAIL},
        'categories': catalog['categories'],
        'actors': [{k: v for k, v in a.items()} for a in catalog['actors']],
    }
    files[DATA / 'actors.json'] = json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    return files


# ---------------------------------------------------------------- gates and output

def check(files: dict[Path, str]) -> list[str]:
    problems = []
    for path, text in files.items():
        rel = path.relative_to(ROOT)
        if '—' in text:
            problems.append(f'{rel}: contains an em dash')
        lowered = text.lower()
        for bad in FORBIDDEN:
            if (bad.lower() if bad != 'CAP-' else bad) in (lowered if bad != 'CAP-' else text):
                problems.append(f'{rel}: contains forbidden string {bad!r}')
        if path.suffix == '.md':
            prose = CODE_BLOCK.sub('', text)
            for m in PRICE.finditer(prose):
                problems.append(f'{rel}: looks like a price: {prose[max(0, m.start() - 40):m.end() + 20]!r}')
            for m in REL_LINK.finditer(prose):
                target = (path.parent / m.group(1).split('#')[0]).resolve()
                if m.group(1).split('#')[0] and target not in files and not target.exists():
                    problems.append(f'{rel}: broken relative link {m.group(1)}')
    return problems


def main() -> None:
    catalog = load_catalog()
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    prev = catalog['previousUpdated']

    # Keep the old date when nothing but the date would change, so the weekly job only commits real updates.
    files = render_all(catalog, prev) if prev else None
    if files is None or any(not p.exists() or p.read_text(encoding='utf-8') != t for p, t in files.items()):
        files = render_all(catalog, today)

    problems = check(files)
    if problems:
        print('Build failed, nothing written:', *problems[:50], sep='\n  ', file=sys.stderr)
        sys.exit(1)

    written = 0
    for path, text in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding='utf-8') != text:
            path.write_text(text, encoding='utf-8', newline='\n')
            written += 1

    keep = {p for p in files}
    for folder in (ROOT / 'actors', ROOT / 'categories'):
        for stale in folder.glob('*.md'):
            if stale not in keep:
                stale.unlink()
                written += 1
                print(f'Removed stale page {stale.relative_to(ROOT)}')

    print(f"Built {len(catalog['actors'])} actors in {len(catalog['categories'])} categories, "
          f"{sum(len(a['useCases']) for a in catalog['actors'])} use cases; {written} files changed.")


if __name__ == '__main__':
    main()
