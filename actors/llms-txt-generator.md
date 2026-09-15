# llms.txt Generator: llms-full.txt for Any Website (AI SEO)

**llms.txt Generator: llms-full.txt for Any Website (AI SEO)** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every page's title, meta description and full Markdown content, and outputs two ready-to-upload files for ChatGPT, Claude, Perplexity and Gemini.

[Run it on Apify](https://apify.com/fayoussef/llms-txt-generator?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/llms-txt-generator?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All SEO & AI Visibility](../categories/seo-ai-visibility.md)

## Key facts

| | |
|---|---|
| Category | [SEO & AI Visibility](../categories/seo-ai-visibility.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/llms-txt-generator?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with llms.txt Generator: llms-full.txt for Any Website (AI SEO)

- **[Generate llms.txt and llms-full.txt for any website](https://apify.com/fayoussef/llms-txt-generator/examples/generate-llms-txt-for-any-website?fpr=youssef)**: Paste a homepage and the Actor finds the sitemap, picks the 50 most important pages, and writes a spec compliant llms.txt index plus an llms-full.txt with the complete Markdown content of every page, ready to upload to...
- **[Build an llms-full.txt for a documentation site](https://apify.com/fayoussef/llms-txt-generator/examples/llms-full-txt-for-documentation-site?fpr=youssef)**: Crawls up to 200 pages of a docs site, limited to the platform and API sections, and produces a single llms-full.txt with every page as clean Markdown. Point AI coding assistants and support bots at one file instead of...

## How to use llms.txt Generator: llms-full.txt for Any Website (AI SEO)

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "websiteUrl": "https://books.toscrape.com",
  "maxPages": 50,
  "includeFullText": true
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'websiteUrl': 'https://books.toscrape.com', 'maxPages': 50, 'includeFullText': True}
run = client.actor("fayoussef/llms-txt-generator").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript / Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: '<YOUR_APIFY_TOKEN>' });
const input = {
  "websiteUrl": "https://books.toscrape.com",
  "maxPages": 50,
  "includeFullText": true
};
const run = await client.actor('fayoussef/llms-txt-generator').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~llms-txt-generator/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"websiteUrl": "https://books.toscrape.com", "maxPages": 50, "includeFullText": true}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/llms-txt-generator
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is llms.txt Generator: llms-full.txt for Any Website (AI SEO) free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/llms-txt-generator?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/llms-txt-generator` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related SEO & AI Visibility

- [SEO, GEO & AEO Audit: AI Search Readiness Checker](seo-geo-aeo-audit.md): Audit any website for Google SEO and AI search visibility in one run. Get 0-100 SEO, GEO & AEO scores per page, AI-crawler & llms.txt...
- [Google Maps Geo-Grid Local Rank Tracker](geo-grid-local-rank-tracker.md): Track where a business ranks in the Google Maps local pack across a grid of points around it. Per-point rank, average rank, coverage, Share...
- [AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)](ai-brand-visibility-tracker.md): Is AI recommending you or your competitors? Track brand mentions, ranking position, sentiment, share of voice and cited sources in ChatGPT...
- [SPF, DKIM & DMARC Checker: Email Deliverability Auditor](email-deliverability-auditor.md): Audit any domain's email deliverability in seconds. Checks SPF, DKIM (around 30 selectors), DMARC, MX, MTA-STS, BIMI and DNSSEC, tests your...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/llms-txt-generator](https://automationbyexperts.com/apify/llms-txt-generator?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/llms-txt-generator.md](https://automationbyexperts.com/apify/llms-txt-generator.md)
