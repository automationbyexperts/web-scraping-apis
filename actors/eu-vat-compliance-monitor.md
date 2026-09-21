# EU VAT Number Validation: Bulk VIES Check & Supplier Monitor

**EU VAT Number Validation: Bulk VIES Check & Supplier Monitor** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Validate a whole supplier or customer list against VIES, get the consultation number that proves you checked, and be told the moment a VAT number goes invalid or its registered name changes. Knows the difference between an invalid number and a member state that is simply down.

[Run it on Apify](https://apify.com/fayoussef/eu-vat-compliance-monitor?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/eu-vat-compliance-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Developer Tools & APIs](../categories/developer-tools.md)

## Key facts

| | |
|---|---|
| Category | [Developer Tools & APIs](../categories/developer-tools.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/eu-vat-compliance-monitor?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-21 |

## How to use EU VAT Number Validation: Bulk VIES Check & Supplier Monitor

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

Open the input form on the Store page to see every field. An empty input runs the defaults.

```json
{}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {}
run = client.actor("fayoussef/eu-vat-compliance-monitor").call(run_input=run_input)

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
const input = {};
const run = await client.actor('fayoussef/eu-vat-compliance-monitor').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~eu-vat-compliance-monitor/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/eu-vat-compliance-monitor
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is EU VAT Number Validation: Bulk VIES Check & Supplier Monitor free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/eu-vat-compliance-monitor?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/eu-vat-compliance-monitor` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Developer Tools & APIs

- [New Business License Feed: Fresh Openings by City](business-license-feed.md): Every business, food, liquor and trade license newly issued in Chicago, Los Angeles, New York, Seattle and New Orleans, filtered to the...
- [Dataset Diff: Only New & Changed Items From Any Actor](dataset-diff.md): Point it at any Apify Actor, Task or dataset and get only what changed since its last run: new rows, edited rows, rows that disappeared...
- [License Verification & Expiry Monitor: Bulk US License Lookup](license-roster-monitor.md): Re-verify a whole roster of contractors, nurses, agents or providers against official state registries, then get only what changed...
- [Scrape any site, Anti-Bot Proxy, JS Render & AI](scrape-any-site-anti-bot-proxy-js-render-ai.md): Free web scraper API for any website. Rotating anti-bot proxies, JS rendering, screenshots, CSS + AI extraction. Clean HTML, Markdown and...
- [Website Change Detector: Page Diff, Price & Content Alerts](website-change-monitor.md): Monitor any web page for changes and get a line-by-line diff of what was added and removed. Track competitor pricing, product listings...

## More

- Full catalog: [all 54 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/eu-vat-compliance-monitor](https://automationbyexperts.com/apify/eu-vat-compliance-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/eu-vat-compliance-monitor.md](https://automationbyexperts.com/apify/eu-vat-compliance-monitor.md)
