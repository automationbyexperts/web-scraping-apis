# SaaS Price Hike Monitor: Pricing Page Change Alerts

**SaaS Price Hike Monitor: Pricing Page Change Alerts** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Watch the pricing pages of the software you pay for and get warned before renewal: price increases with old and new price, removed free plans, new tiers. AI reads each page into plans and prices, any vendor, no setup.

[Run it on Apify](https://apify.com/fayoussef/saas-price-hike-monitor?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/saas-price-hike-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Price & Brand Monitoring](../categories/price-monitoring.md)

## Key facts

| | |
|---|---|
| Category | [Price & Brand Monitoring](../categories/price-monitoring.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/saas-price-hike-monitor?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-11-09 |

## How to use SaaS Price Hike Monitor: Pricing Page Change Alerts

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
run = client.actor("fayoussef/saas-price-hike-monitor").call(run_input=run_input)

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
const run = await client.actor('fayoussef/saas-price-hike-monitor').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~saas-price-hike-monitor/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/saas-price-hike-monitor
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

### From AI agents with no Apify account (x402 or Skyfire)

This actor accepts [agentic payments](../agentic-payments.md): an AI agent can run it and pay per run with USDC (x402) or a Skyfire token, with no Apify account.

```bash
# x402: TOKEN is the prepaid token bought from Apify AGI with USDC on Base
curl -X POST "https://api.apify.com/v2/acts/fayoussef~saas-price-hike-monitor/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'

# Skyfire: send the PAY token instead
curl -X POST "https://api.apify.com/v2/acts/fayoussef~saas-price-hike-monitor/run-sync-get-dataset-items" \
  -H "skyfire-pay-id: $SKYFIRE_PAY_TOKEN" -H "Content-Type: application/json" -d '{}'
```

With MCP and Skyfire: `https://mcp.apify.com?payment=skyfire&tools=fayoussef/saas-price-hike-monitor`

## FAQ

### Is SaaS Price Hike Monitor: Pricing Page Change Alerts free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/saas-price-hike-monitor?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/saas-price-hike-monitor` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can an AI agent run it without an Apify account?

Yes. This actor accepts agentic payments: an agent can pay per run with USDC through the x402 protocol, or with a Skyfire PAY token, and no Apify account is needed. See [AI agents and x402 payments](../agentic-payments.md).

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Price & Brand Monitoring

- [Brand Protection: Fake Shop, Counterfeit & Typosquat Finder](brand-abuse-counterfeit-detector.md): Find fake webshops, counterfeit marketplace listings, typosquatted domains and impersonation profiles abusing your brand. AI classifies...
- [MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers](map-violation-monitor.md): Enter your products and MAP prices and get every public offer advertised below them on Amazon, eBay, Best Buy and Newegg. AI verifies each...
- [Amazon, eBay, Best Buy & Newegg Price Checker by ASIN or UPC](multi-marketplace-price-checker.md): Paste ASINs, UPCs, model numbers or product names and get what that exact product sells for on Amazon, eBay, Best Buy and Newegg. AI...
- [Amazon Best Sellers Scraper: Rank Tracker, 21 Marketplaces](amazon-bestsellers-tracker.md): Track Amazon Best Sellers and New Releases ranks 1-100 in 21 marketplaces (US, UK, DE, FR, JP, IN, BR and more). Each run shows what moved...

## More

- Full catalog: [all 64 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/saas-price-hike-monitor](https://automationbyexperts.com/apify/saas-price-hike-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/saas-price-hike-monitor.md](https://automationbyexperts.com/apify/saas-price-hike-monitor.md)
