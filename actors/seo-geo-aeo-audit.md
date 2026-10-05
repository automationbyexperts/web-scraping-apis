# SEO, GEO & AEO Audit: AI Search Readiness Checker

**SEO, GEO & AEO Audit: AI Search Readiness Checker** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Audit any website for Google SEO and AI search visibility in one run. Get 0-100 SEO, GEO & AEO scores per page, AI-crawler & llms.txt checks, schema validation, and a prioritized fix list with a shareable HTML report. No API keys needed - just enter a URL.

[Run it on Apify](https://apify.com/fayoussef/seo-geo-aeo-audit?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/seo-geo-aeo-audit?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All SEO & AI Visibility](../categories/seo-ai-visibility.md)

## Key facts

| | |
|---|---|
| Category | [SEO & AI Visibility](../categories/seo-ai-visibility.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/seo-geo-aeo-audit?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with SEO, GEO & AEO Audit: AI Search Readiness Checker

- **[Audit a website for AI search readiness](https://apify.com/fayoussef/seo-geo-aeo-audit/examples/ai-search-readiness-audit?fpr=youssef)**: Crawls the homepage and the 25 most important pages, runs 45 plus checks and scores the site 0 to 100 for classic SEO, GEO (visibility in ChatGPT, Perplexity and Gemini answers) and AEO (featured snippets). Returns a...
- **[Run a quick 5 page SEO check on a small business site](https://apify.com/fayoussef/seo-geo-aeo-audit/examples/quick-5-page-seo-check?fpr=youssef)**: A fast first look: the homepage plus the four key pages the Actor discovers on its own, scored for SEO, AI search visibility and answer engine readiness. Fits inside the free plan limit, so it is the right size for a...
- **[Full 100 page SEO and GEO audit for a content site](https://apify.com/fayoussef/seo-geo-aeo-audit/examples/full-site-seo-geo-audit-100-pages?fpr=youssef)**: Audits up to 100 pages of a blog, docs or ecommerce site and returns every issue per page, from blocked AI crawlers and JavaScript only content to missing schema, thin titles and slow pages. Use the issues view to hand...

## How to use SEO, GEO & AEO Audit: AI Search Readiness Checker

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "websiteUrl": "https://books.toscrape.com",
  "maxPages": 25,
  "includeHtmlReport": true
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'websiteUrl': 'https://books.toscrape.com', 'maxPages': 25, 'includeHtmlReport': True}
run = client.actor("fayoussef/seo-geo-aeo-audit").call(run_input=run_input)

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
  "maxPages": 25,
  "includeHtmlReport": true
};
const run = await client.actor('fayoussef/seo-geo-aeo-audit').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~seo-geo-aeo-audit/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"websiteUrl": "https://books.toscrape.com", "maxPages": 25, "includeHtmlReport": true}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/seo-geo-aeo-audit
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is SEO, GEO & AEO Audit: AI Search Readiness Checker free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/seo-geo-aeo-audit?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/seo-geo-aeo-audit` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related SEO & AI Visibility

- [Google Maps Geo-Grid Local Rank Tracker](geo-grid-local-rank-tracker.md): Track where a business ranks in the Google Maps local pack across a grid of points around it. Per-point rank, average rank, coverage, Share...
- [AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)](ai-brand-visibility-tracker.md): Is AI recommending you or your competitors? Track brand mentions, ranking position, sentiment, share of voice and cited sources in ChatGPT...
- [llms.txt Generator: llms-full.txt for Any Website (AI SEO)](llms-txt-generator.md): Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/seo-geo-aeo-audit](https://automationbyexperts.com/apify/seo-geo-aeo-audit?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/seo-geo-aeo-audit.md](https://automationbyexperts.com/apify/seo-geo-aeo-audit.md)
