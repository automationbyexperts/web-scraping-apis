# FnacPro Scraper: Product, Price, EAN & Spec Extractor

**FnacPro Scraper: Product, Price, EAN & Spec Extractor** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape fnacpro.com product data at scale: price, EAN, reference, brand, availability, condition, full specifications, ratings, images and video, from any product or listing URL. Fast and concurrent, with one clean record per product for catalog building, price monitoring and B2B reselling.

[Run it on Apify](https://apify.com/fayoussef/fnacpro-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/fnacpro-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/fnacpro-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## How to use FnacPro Scraper: Product, Price, EAN & Spec Extractor

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
run = client.actor("fayoussef/fnacpro-scraper").call(run_input=run_input)

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
const run = await client.actor('fayoussef/fnacpro-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~fnacpro-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/fnacpro-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is FnacPro Scraper: Product, Price, EAN & Spec Extractor free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/fnacpro-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/fnacpro-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related E-commerce & Marketplace Scrapers

- [wallapop Scraper (Spain,Italy,Portugal)](wallapop-scraper.md): Scrape Wallapop listings at scale across Spain, Italy, and Portugal without writing a single line of code. Paste any Wallapop search URL or...
- [Fnac.com Scraper: Prices, EAN, Stock, Sellers & Reviews](fnac-data-scraping.md): Scrape fnac.com products from any search, category or product URL, or by keyword with brand, category, price, seller and stock filters. Get...
- [G2G Scraper: Extract G2G.com Prices, Sellers & Stock](g2g-offer-scraper.md): Scrape live G2G.com prices, sellers, stock and delivery times from any category or Trending URL. Export JSON, CSV or Excel. No G2G login or...
- [Bike24 Scraper: Cycling Product Prices, Stock & Specs](bike24-result-scraper.md): Our bike24.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each product page
- [Skroutz Scraper: Prices, Shop Offers & Price History](skroutz-scraper.md): Scrape Skroutz products from Greece, Cyprus, Bulgaria, Romania, Germany and Malta in English, Greek, Bulgarian, Romanian or German. Paste...
- [Cheap Amazon Scraper: Extract Products, Offers, Prices](cheap-amazon-scraper.md): Fast, reliable Amazon scraper. Extract product details, search results, seller offers and raw HTML from 21 marketplaces with geo-targeting...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/fnacpro-scraper](https://automationbyexperts.com/apify/fnacpro-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/fnacpro-scraper.md](https://automationbyexperts.com/apify/fnacpro-scraper.md)
