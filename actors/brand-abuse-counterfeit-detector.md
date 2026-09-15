# Brand Protection: Fake Shop, Counterfeit & Typosquat Finder

**Brand Protection: Fake Shop, Counterfeit & Typosquat Finder** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Find fake webshops, counterfeit marketplace listings, typosquatted domains and impersonation profiles abusing your brand. AI classifies every hit, scores the risk, saves a dated page snapshot as takedown evidence, and tells you which report to file. No API key needed.

[Run it on Apify](https://apify.com/fayoussef/brand-abuse-counterfeit-detector?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/brand-abuse-counterfeit-detector?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Price & Brand Monitoring](../categories/price-monitoring.md)

## Key facts

| | |
|---|---|
| Category | [Price & Brand Monitoring](../categories/price-monitoring.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/brand-abuse-counterfeit-detector?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with Brand Protection: Fake Shop, Counterfeit & Typosquat Finder

- **[Find fake webshops selling your brand](https://apify.com/fayoussef/brand-abuse-counterfeit-detector/examples/fake-shops-selling-your-brand?fpr=youssef)**: Sweeps search results and marketplaces for storefronts and listings trading on the Ray-Ban name and its best known models, screens each with AI for counterfeit and fake shop signals, and returns only hits at or above a...
- **[Sweep for typosquat domains impersonating your brand](https://apify.com/fayoussef/brand-abuse-counterfeit-detector/examples/typosquat-domain-sweep?fpr=youssef)**: Generates 200 misspellings, character swaps, hyphenations and alternative TLDs of your official domain, checks which ones are registered and live, and has AI judge whether each one impersonates the brand. The output is...

## How to use Brand Protection: Fake Shop, Counterfeit & Typosquat Finder

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "brandName": "Ray-Ban",
  "officialDomains": [
    "ray-ban.com"
  ],
  "checks": [
    "fake_shops",
    "marketplace_listings"
  ],
  "productKeywords": [
    "Wayfarer",
    "Aviator"
  ],
  "minRiskScore": 60,
  "maxCandidates": 120,
  "countryCode": "us"
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'brandName': 'Ray-Ban',
 'officialDomains': ['ray-ban.com'],
 'checks': ['fake_shops', 'marketplace_listings'],
 'productKeywords': ['Wayfarer', 'Aviator'],
 'minRiskScore': 60,
 'maxCandidates': 120,
 'countryCode': 'us'}
run = client.actor("fayoussef/brand-abuse-counterfeit-detector").call(run_input=run_input)

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
  "brandName": "Ray-Ban",
  "officialDomains": [
    "ray-ban.com"
  ],
  "checks": [
    "fake_shops",
    "marketplace_listings"
  ],
  "productKeywords": [
    "Wayfarer",
    "Aviator"
  ],
  "minRiskScore": 60,
  "maxCandidates": 120,
  "countryCode": "us"
};
const run = await client.actor('fayoussef/brand-abuse-counterfeit-detector').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~brand-abuse-counterfeit-detector/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"brandName": "Ray-Ban", "officialDomains": ["ray-ban.com"], "checks": ["fake_shops", "marketplace_listings"], "productKeywords": ["Wayfarer", "Aviator"], "minRiskScore": 60, "maxCandidates": 120, "countryCode": "us"}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/brand-abuse-counterfeit-detector
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Brand Protection: Fake Shop, Counterfeit & Typosquat Finder free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/brand-abuse-counterfeit-detector?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/brand-abuse-counterfeit-detector` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Price & Brand Monitoring

- [Competitor Price Tracker & Price Comparison by Product URL](competitor-price-tracker-price-comparison-by-product-url.md): Paste any product URL to get every retailer selling the same item, live prices, your market rank, and a suggested pricing action. Matches...
- [MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers](map-violation-monitor.md): Enter your products and MAP prices and get every public offer advertised below them on Amazon, eBay, Best Buy and Newegg. AI verifies each...
- [Amazon, eBay, Best Buy & Newegg Price Checker by ASIN or UPC](multi-marketplace-price-checker.md): Paste ASINs, UPCs, model numbers or product names and get what that exact product sells for on Amazon, eBay, Best Buy and Newegg. AI...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/brand-abuse-counterfeit-detector](https://automationbyexperts.com/apify/brand-abuse-counterfeit-detector?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/brand-abuse-counterfeit-detector.md](https://automationbyexperts.com/apify/brand-abuse-counterfeit-detector.md)
