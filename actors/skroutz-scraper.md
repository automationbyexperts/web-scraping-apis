# Skroutz Scraper: Greek Price Comparison, Offers & History

**Skroutz Scraper: Greek Price Comparison, Offers & History** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape Skroutz, Greece's largest price comparison site, plus Skroutz Cyprus, Bulgaria, Romania, Germany and Malta. Paste any category, brand, shop or search URL, or search by keyword, and get prices, ratings, specs, every shop's offer and daily price history.

[Run it on Apify](https://apify.com/fayoussef/skroutz-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/skroutz-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/skroutz-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-08 |

## What you can do with Skroutz Scraper: Greek Price Comparison, Offers & History

- **[Compare iPhone 17 Pro prices across all Skroutz countries](https://apify.com/fayoussef/skroutz-scraper/examples/iphone-17-pro-prices-all-skroutz-countries?fpr=youssef)**: Search Skroutz in Greece, Cyprus, Bulgaria, Romania, Germany and Malta for the iPhone 17 Pro and get every model with its price, currency, rating and delivery in English, plus every shop selling it with price, stock and...
- **[Τιμές πλυντηρίων ρούχων στο Skroutz με ιστορικό τιμών](https://apify.com/fayoussef/skroutz-scraper/examples/washing-machine-prices-greece-greek?fpr=youssef)**: Συγκεντρώστε τα πλυντήρια ρούχων του Skroutz.gr με τιμή, βαθμολογία και παράδοση, μαζί με το ιστορικό χαμηλότερης τιμής κάθε προϊόντος: τη χαμηλότερη τιμή όλων των εποχών και των τελευταίων 30 και 90 ημερών. Ιδανικό για...

## How to use Skroutz Scraper: Greek Price Comparison, Offers & History

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "search_terms": [
    "iphone 17 pro"
  ],
  "countries": [
    "gr",
    "cy",
    "bg",
    "ro",
    "de",
    "mt"
  ],
  "language": "en",
  "sort_by": "price_asc",
  "max_items": 200,
  "include_shop_offers": true
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'search_terms': ['iphone 17 pro'],
 'countries': ['gr', 'cy', 'bg', 'ro', 'de', 'mt'],
 'language': 'en',
 'sort_by': 'price_asc',
 'max_items': 200,
 'include_shop_offers': True}
run = client.actor("fayoussef/skroutz-scraper").call(run_input=run_input)

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
  "search_terms": [
    "iphone 17 pro"
  ],
  "countries": [
    "gr",
    "cy",
    "bg",
    "ro",
    "de",
    "mt"
  ],
  "language": "en",
  "sort_by": "price_asc",
  "max_items": 200,
  "include_shop_offers": true
};
const run = await client.actor('fayoussef/skroutz-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~skroutz-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"search_terms": ["iphone 17 pro"], "countries": ["gr", "cy", "bg", "ro", "de", "mt"], "language": "en", "sort_by": "price_asc", "max_items": 200, "include_shop_offers": true}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/skroutz-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

### From AI agents with no Apify account (x402 or Skyfire)

This actor accepts [agentic payments](../agentic-payments.md): an AI agent can run it and pay per run with USDC (x402) or a Skyfire token, with no Apify account.

```bash
# x402: TOKEN is the prepaid token bought from Apify AGI with USDC on Base
curl -X POST "https://api.apify.com/v2/acts/fayoussef~skroutz-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'

# Skyfire: send the PAY token instead
curl -X POST "https://api.apify.com/v2/acts/fayoussef~skroutz-scraper/run-sync-get-dataset-items" \
  -H "skyfire-pay-id: $SKYFIRE_PAY_TOKEN" -H "Content-Type: application/json" -d '{}'
```

With MCP and Skyfire: `https://mcp.apify.com?payment=skyfire&tools=fayoussef/skroutz-scraper`

## FAQ

### Is Skroutz Scraper: Greek Price Comparison, Offers & History free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/skroutz-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/skroutz-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can an AI agent run it without an Apify account?

Yes. This actor accepts agentic payments: an agent can pay per run with USDC through the x402 protocol, or with a Skyfire PAY token, and no Apify account is needed. See [AI agents and x402 payments](../agentic-payments.md).

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related E-commerce & Marketplace Scrapers

- [wallapop Scraper (Spain,Italy,Portugal)](wallapop-scraper.md): Scrape Wallapop listings at scale across Spain, Italy, and Portugal without writing a single line of code. Paste any Wallapop search URL or...
- [Fnac.com Scraper: Products, Prices, EAN, Stock & Reviews](fnac-data-scraping.md): Scrape fnac.com products from any search, category or product URL, or by keyword with brand, category, price, seller and stock filters. Get...
- [G2G Scraper: Extract G2G.com Prices, Sellers & Stock](g2g-offer-scraper.md): Scrape live G2G.com prices, sellers, stock and delivery times from any category or Trending URL. Export JSON, CSV or Excel. No G2G login or...
- [Bike24 Scraper: Cycling Product Prices, Stock & Specs](bike24-result-scraper.md): Our bike24.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each product page
- [RONA Scraper: Canada Home Improvement Prices, Stock & Specs](rona-scraper.md): Scrape RONA.ca products in English and French from any category, search or product URL. Export price, sale price, regular price, stock by...
- [Smyths Toys Scraper: Prices, EAN Codes, Stock & Product Data](smythstoys-scraper.md): Scrape Smyths Toys UK and Ireland by category, search or product URL. Get prices, was prices, discounts, EAN barcodes, brand, ratings...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/skroutz-scraper](https://automationbyexperts.com/apify/skroutz-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/skroutz-scraper.md](https://automationbyexperts.com/apify/skroutz-scraper.md)
