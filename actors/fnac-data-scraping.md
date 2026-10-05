# Fnac.com Scraper: Products, Prices, EAN, Stock & Reviews

**Fnac.com Scraper: Products, Prices, EAN, Stock & Reviews** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape fnac.com products from any search, category or product URL, or by keyword with brand, category, price, seller and stock filters. Get price, list price, discount, EAN, SKU, brand, stock, marketplace sellers, ratings, reviews, specs and images. No API key needed.

[Run it on Apify](https://apify.com/fayoussef/fnac-data-scraping?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/fnac-data-scraping?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [E-commerce & Marketplace Scrapers](../categories/ecommerce-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/fnac-data-scraping?fpr=youssef)) |
| Rating | 5.0 out of 5 (1 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with Fnac.com Scraper: Products, Prices, EAN, Stock & Reviews

- **[Scrape Fnac laptop prices, EAN and stock in France](https://apify.com/fayoussef/fnac-data-scraping/examples/fnac-laptop-prices-france?fpr=youssef)**: Exports every laptop in the fnac.com Tous les ordinateurs portables category with current price, crossed-out list price, discount, EAN, SKU, brand, stock status, marketplace sellers, ratings and the full spec table...
- **[Find Lenovo and HP laptops under 600 EUR sold by Fnac](https://apify.com/fayoussef/fnac-data-scraping/examples/fnac-lenovo-hp-laptops-under-600?fpr=youssef)**: Searches fnac.com for laptops, keeps only new Lenovo and HP models under 600 EUR that are sold by Fnac and in stock, cheapest first. Each result has the price, list price, discount, EAN, stock status, rating and full...
- **[Casques Bluetooth Sony vendus par Fnac, les mieux notés](https://apify.com/fayoussef/fnac-data-scraping/examples/fnac-casques-sony-bluetooth-vendus-par-fnac?fpr=youssef)**: Recherche les casques et écouteurs Bluetooth Sony sur fnac.com, garde uniquement ceux vendus par Fnac et les classe par note client. Chaque produit comprend le prix, le prix barré, la remise, l'EAN, la disponibilité, la...
- **[Meilleures ventes de romans policiers Fnac avec EAN](https://apify.com/fayoussef/fnac-data-scraping/examples/fnac-romans-policiers-meilleures-ventes?fpr=youssef)**: Recherche les romans policiers dans la catégorie Livres de fnac.com, classés par meilleures ventes. Chaque livre comprend le prix, l'EAN (ISBN), l'auteur, la disponibilité, la note, les avis et le résumé. Idéal pour les...

## How to use Fnac.com Scraper: Products, Prices, EAN, Stock & Reviews

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "start_urls": [
    {
      "url": "https://www.fnac.com/Tous-les-ordinateurs-portables/Ordinateurs-portables/nsh154425/w-4"
    }
  ],
  "max_depth": 3
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'start_urls': [{'url': 'https://www.fnac.com/Tous-les-ordinateurs-portables/Ordinateurs-portables/nsh154425/w-4'}],
 'max_depth': 3}
run = client.actor("fayoussef/fnac-data-scraping").call(run_input=run_input)

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
  "start_urls": [
    {
      "url": "https://www.fnac.com/Tous-les-ordinateurs-portables/Ordinateurs-portables/nsh154425/w-4"
    }
  ],
  "max_depth": 3
};
const run = await client.actor('fayoussef/fnac-data-scraping').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~fnac-data-scraping/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"start_urls": [{"url": "https://www.fnac.com/Tous-les-ordinateurs-portables/Ordinateurs-portables/nsh154425/w-4"}], "max_depth": 3}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/fnac-data-scraping
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Fnac.com Scraper: Products, Prices, EAN, Stock & Reviews free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/fnac-data-scraping?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/fnac-data-scraping` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related E-commerce & Marketplace Scrapers

- [wallapop Scraper (Spain,Italy,Portugal)](wallapop-scraper.md): Scrape Wallapop listings at scale across Spain, Italy, and Portugal without writing a single line of code. Paste any Wallapop search URL or...
- [G2G Scraper: Extract G2G.com Prices, Sellers & Stock](g2g-offer-scraper.md): Scrape live G2G.com prices, sellers, stock and delivery times from any category or Trending URL. Export JSON, CSV or Excel. No G2G login or...
- [Bike24 Scraper: Cycling Product Prices, Stock & Specs](bike24-result-scraper.md): Our bike24.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each product page
- [Skroutz Scraper: Greek Price Comparison, Offers & History](skroutz-scraper.md): Scrape Skroutz, Greece's largest price comparison site, plus Skroutz Cyprus, Bulgaria, Romania, Germany and Malta. Paste any category...
- [RONA Scraper: Canada Home Improvement Prices, Stock & Specs](rona-scraper.md): Scrape RONA.ca products in English and French from any category, search or product URL. Export price, sale price, regular price, stock by...
- [Amazon Scraper: Products, Search Results, Offers & Buy Box](cheap-amazon-scraper.md): Scrape Amazon product details, search results, seller offers and Buy Box data from 21 marketplaces, with ZIP-level pricing and...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/fnac-data-scraping](https://automationbyexperts.com/apify/fnac-data-scraping?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/fnac-data-scraping.md](https://automationbyexperts.com/apify/fnac-data-scraping.md)
