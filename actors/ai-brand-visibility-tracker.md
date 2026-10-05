# AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)

**AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Is AI recommending you or your competitors? Track brand mentions, ranking position, sentiment, share of voice and cited sources in ChatGPT, Perplexity, Gemini, Claude & Grok answers for the questions your buyers ask. GEO / AEO / LLM SEO monitoring .no OpenAI or Anthropic API key needed.

[Run it on Apify](https://apify.com/fayoussef/ai-brand-visibility-tracker?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/ai-brand-visibility-tracker?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All SEO & AI Visibility](../categories/seo-ai-visibility.md)

## Key facts

| | |
|---|---|
| Category | [SEO & AI Visibility](../categories/seo-ai-visibility.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/ai-brand-visibility-tracker?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)

- **[Check if AI recommends your CRM to small businesses](https://apify.com/fayoussef/ai-brand-visibility-tracker/examples/crm-brand-visibility-in-ai-answers?fpr=youssef)**: Asks ChatGPT, Perplexity and Gemini the questions a small business owner asks when choosing a CRM, and reports whether HubSpot is named, where it ranks, which competitors are recommended instead, and whether hubspot.com...
- **[Measure an ecommerce platform's share of voice in AI search](https://apify.com/fayoussef/ai-brand-visibility-tracker/examples/ecommerce-platform-ai-share-of-voice?fpr=youssef)**: Runs each buying intent question twice per platform for a stable score and computes Shopify's share of voice against WooCommerce, BigCommerce and Wix across ChatGPT, Perplexity and Gemini. The answers view keeps the...

## How to use AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "brand_name": "HubSpot",
  "queries": [
    "What is the best CRM for a small business?",
    "Which CRM should a 20 person sales team use in 2026?",
    "HubSpot vs Salesforce for a startup"
  ],
  "competitors": [
    "Salesforce",
    "Pipedrive",
    "Zoho CRM"
  ],
  "brand_domains": [
    "hubspot.com"
  ],
  "platforms": [
    "chatgpt",
    "perplexity",
    "gemini"
  ],
  "runs_per_query": 1
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'brand_name': 'HubSpot',
 'queries': ['What is the best CRM for a small business?',
             'Which CRM should a 20 person sales team use in 2026?',
             'HubSpot vs Salesforce for a startup'],
 'competitors': ['Salesforce', 'Pipedrive', 'Zoho CRM'],
 'brand_domains': ['hubspot.com'],
 'platforms': ['chatgpt', 'perplexity', 'gemini'],
 'runs_per_query': 1}
run = client.actor("fayoussef/ai-brand-visibility-tracker").call(run_input=run_input)

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
  "brand_name": "HubSpot",
  "queries": [
    "What is the best CRM for a small business?",
    "Which CRM should a 20 person sales team use in 2026?",
    "HubSpot vs Salesforce for a startup"
  ],
  "competitors": [
    "Salesforce",
    "Pipedrive",
    "Zoho CRM"
  ],
  "brand_domains": [
    "hubspot.com"
  ],
  "platforms": [
    "chatgpt",
    "perplexity",
    "gemini"
  ],
  "runs_per_query": 1
};
const run = await client.actor('fayoussef/ai-brand-visibility-tracker').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~ai-brand-visibility-tracker/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"brand_name": "HubSpot", "queries": ["What is the best CRM for a small business?", "Which CRM should a 20 person sales team use in 2026?", "HubSpot vs Salesforce for a startup"], "competitors": ["Salesforce", "Pipedrive", "Zoho CRM"], "brand_domains": ["hubspot.com"], "platforms": ["chatgpt", "perplexity", "gemini"], "runs_per_query": 1}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/ai-brand-visibility-tracker
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini) free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/ai-brand-visibility-tracker?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/ai-brand-visibility-tracker` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related SEO & AI Visibility

- [SEO, GEO & AEO Audit: AI Search Readiness Checker](seo-geo-aeo-audit.md): Audit any website for Google SEO and AI search visibility in one run. Get 0-100 SEO, GEO & AEO scores per page, AI-crawler & llms.txt...
- [Google Maps Geo-Grid Local Rank Tracker](geo-grid-local-rank-tracker.md): Track where a business ranks in the Google Maps local pack across a grid of points around it. Per-point rank, average rank, coverage, Share...
- [llms.txt Generator: llms-full.txt for Any Website (AI SEO)](llms-txt-generator.md): Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/ai-brand-visibility-tracker](https://automationbyexperts.com/apify/ai-brand-visibility-tracker?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/ai-brand-visibility-tracker.md](https://automationbyexperts.com/apify/ai-brand-visibility-tracker.md)
