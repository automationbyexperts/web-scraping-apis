# MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers

**MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Enter your products and MAP prices and get every public offer advertised below them on Amazon, eBay, Best Buy and Newegg. AI verifies each listing is your exact product, so accessories and variants never trigger a false violation. Graded severity, seller identity and an evidence link per row.

[Run it on Apify](https://apify.com/fayoussef/map-violation-monitor?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/map-violation-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Price & Brand Monitoring](../categories/price-monitoring.md)

## Key facts

| | |
|---|---|
| Category | [Price & Brand Monitoring](../categories/price-monitoring.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/map-violation-monitor?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers

- **[Check Amazon and eBay for MAP violations](https://apify.com/fayoussef/map-violation-monitor/examples/amazon-ebay-map-violation-check?fpr=youssef)**: Takes your products with their minimum advertised price, searches Amazon, eBay, Best Buy and Newegg for every public offer, runs an AI exact match check so a cable or a refurbished unit is never counted, and returns...
- **[Detect unauthorized sellers of your products](https://apify.com/fayoussef/map-violation-monitor/examples/unauthorized-seller-detection?fpr=youssef)**: Lists every seller offering your product on Amazon and eBay and flags any not on your authorized reseller list, with their price relative to MAP. The sellers view groups offers by seller so you can see who is diverting...

## How to use MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "products": [
    "B0DGHMNQ5Z, 129.99",
    "Sony WH-1000XM5, 349.99"
  ],
  "marketplaces": [
    "Amazon",
    "eBay",
    "BestBuy",
    "Newegg"
  ],
  "onlyViolations": true,
  "zipCode": "10001"
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'products': ['B0DGHMNQ5Z, 129.99', 'Sony WH-1000XM5, 349.99'],
 'marketplaces': ['Amazon', 'eBay', 'BestBuy', 'Newegg'],
 'onlyViolations': True,
 'zipCode': '10001'}
run = client.actor("fayoussef/map-violation-monitor").call(run_input=run_input)

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
  "products": [
    "B0DGHMNQ5Z, 129.99",
    "Sony WH-1000XM5, 349.99"
  ],
  "marketplaces": [
    "Amazon",
    "eBay",
    "BestBuy",
    "Newegg"
  ],
  "onlyViolations": true,
  "zipCode": "10001"
};
const run = await client.actor('fayoussef/map-violation-monitor').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~map-violation-monitor/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"products": ["B0DGHMNQ5Z, 129.99", "Sony WH-1000XM5, 349.99"], "marketplaces": ["Amazon", "eBay", "BestBuy", "Newegg"], "onlyViolations": true, "zipCode": "10001"}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/map-violation-monitor
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/map-violation-monitor?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/map-violation-monitor` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Price & Brand Monitoring

- [Competitor Price Tracker & Price Comparison by Product URL](competitor-price-tracker-price-comparison-by-product-url.md): Paste any product URL to get every retailer selling the same item, live prices, your market rank, and a suggested pricing action. Matches...
- [Brand Protection: Fake Shop, Counterfeit & Typosquat Finder](brand-abuse-counterfeit-detector.md): Find fake webshops, counterfeit marketplace listings, typosquatted domains and impersonation profiles abusing your brand. AI classifies...
- [Amazon, eBay, Best Buy & Newegg Price Checker by ASIN or UPC](multi-marketplace-price-checker.md): Paste ASINs, UPCs, model numbers or product names and get what that exact product sells for on Amazon, eBay, Best Buy and Newegg. AI...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/map-violation-monitor](https://automationbyexperts.com/apify/map-violation-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/map-violation-monitor.md](https://automationbyexperts.com/apify/map-violation-monitor.md)
