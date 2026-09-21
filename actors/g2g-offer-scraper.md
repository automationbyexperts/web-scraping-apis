# G2G Scraper: Extract G2G.com Prices, Sellers & Stock

**G2G Scraper: Extract G2G.com Prices, Sellers & Stock** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape live G2G.com prices, sellers, stock and delivery times from any category or Trending URL. Export JSON, CSV or Excel. No G2G login or API key needed.

[Run it on Apify](https://apify.com/fayoussef/g2g-offer-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/g2g-offer-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/g2g-offer-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-21 |

## What you can do with G2G Scraper: Extract G2G.com Prices, Sellers & Stock

- **[Track WoW Classic gold prices and sellers on G2G](https://apify.com/fayoussef/g2g-offer-scraper/examples/wow-classic-gold-prices-g2g?fpr=youssef)**: Reads every live WoW Classic gold offer on G2G.com and returns price per unit, minimum order, stock, delivery time, seller name, rating and completed orders across 78 fields. Schedule it hourly to build a price index of...
- **[Monitor FC 26 coin prices across G2G sellers](https://apify.com/fayoussef/g2g-offer-scraper/examples/fc-26-coins-price-tracker?fpr=youssef)**: Collects all FC 26 coin offers on G2G with price, stock, delivery method and seller reputation so traders and sellers can see where the market sits before pricing their own stock. The full view carries every field G2G...

## How to use G2G Scraper: Extract G2G.com Prices, Sellers & Stock

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "urls": [
    "https://www.g2g.com/categories/wow-classic-gold"
  ],
  "maxItems": 500
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'urls': ['https://www.g2g.com/categories/wow-classic-gold'], 'maxItems': 500}
run = client.actor("fayoussef/g2g-offer-scraper").call(run_input=run_input)

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
  "urls": [
    "https://www.g2g.com/categories/wow-classic-gold"
  ],
  "maxItems": 500
};
const run = await client.actor('fayoussef/g2g-offer-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~g2g-offer-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://www.g2g.com/categories/wow-classic-gold"], "maxItems": 500}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/g2g-offer-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is G2G Scraper: Extract G2G.com Prices, Sellers & Stock free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/g2g-offer-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/g2g-offer-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related E-commerce & Marketplace Scrapers

- [wallapop Scraper (Spain,Italy,Portugal)](wallapop-scraper.md): Scrape Wallapop listings at scale across Spain, Italy, and Portugal without writing a single line of code. Paste any Wallapop search URL or...
- [Fnac.com Scraper: Prices, EAN, Stock, Sellers & Reviews](fnac-data-scraping.md): Scrape fnac.com products from any search, category or product URL, or by keyword with brand, category, price, seller and stock filters. Get...
- [Bike24 Scraper: Cycling Product Prices, Stock & Specs](bike24-result-scraper.md): Our bike24.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each product page
- [FnacPro Scraper: Product, Price, EAN & Spec Extractor](fnacpro-scraper.md): Scrape fnacpro.com product data at scale: price, EAN, reference, brand, availability, condition, full specifications, ratings, images and...
- [Skroutz Scraper: Prices, Shop Offers & Price History](skroutz-scraper.md): Scrape Skroutz products from Greece, Cyprus, Bulgaria, Romania, Germany and Malta in English, Greek, Bulgarian, Romanian or German. Paste...
- [Cheap Amazon Scraper: Extract Products, Offers, Prices](cheap-amazon-scraper.md): Fast, reliable Amazon scraper. Extract product details, search results, seller offers and raw HTML from 21 marketplaces with geo-targeting...

## More

- Full catalog: [all 54 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/g2g-offer-scraper](https://automationbyexperts.com/apify/g2g-offer-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/g2g-offer-scraper.md](https://automationbyexperts.com/apify/g2g-offer-scraper.md)
