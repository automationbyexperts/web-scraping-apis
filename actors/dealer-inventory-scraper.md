# Car Dealer Website Inventory Scraper: VIN, Price & Stock

**Car Dealer Website Inventory Scraper: VIN, Price & Stock** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape live vehicle inventory from any car dealership's own website, not a marketplace. Paste a dealer homepage and get every car at VIN level with price, mileage and trim. Auto-detects DealerOn, Dealer.com, Dealer Inspire and more. Tracks price drops and sold units.

[Run it on Apify](https://apify.com/fayoussef/dealer-inventory-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/dealer-inventory-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Car & Vehicle Scrapers](../categories/vehicle-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Car & Vehicle Scrapers](../categories/vehicle-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/dealer-inventory-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with Car Dealer Website Inventory Scraper: VIN, Price & Stock

- **[Export a dealership's used inventory from its own website](https://apify.com/fayoussef/dealer-inventory-scraper/examples/dealer-website-used-inventory-export?fpr=youssef)**: Paste dealer homepages and the Actor finds their inventory pages by itself, detects the website platform, and returns every used vehicle at VIN level with the dealer's own price, mileage, stock number and photos...
- **[Track price drops on competing dealer lots](https://apify.com/fayoussef/dealer-inventory-scraper/examples/dealer-price-drop-tracker?fpr=youssef)**: Reads the full inventory of each dealer site and compares it with the previous run, labelling every vehicle new, price_drop, price_increase, unchanged or removed. Schedule it daily and the changes view is a running log...

## How to use Car Dealer Website Inventory Scraper: VIN, Price & Stock

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "dealerUrls": [
    "https://www.toyotaofdowntownla.com",
    "https://www.mbofsmithtown.com"
  ],
  "condition": "used",
  "maxVehiclesPerDealer": 300,
  "fetchDetails": true,
  "concurrency": 3
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'dealerUrls': ['https://www.toyotaofdowntownla.com', 'https://www.mbofsmithtown.com'],
 'condition': 'used',
 'maxVehiclesPerDealer': 300,
 'fetchDetails': True,
 'concurrency': 3}
run = client.actor("fayoussef/dealer-inventory-scraper").call(run_input=run_input)

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
  "dealerUrls": [
    "https://www.toyotaofdowntownla.com",
    "https://www.mbofsmithtown.com"
  ],
  "condition": "used",
  "maxVehiclesPerDealer": 300,
  "fetchDetails": true,
  "concurrency": 3
};
const run = await client.actor('fayoussef/dealer-inventory-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~dealer-inventory-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"dealerUrls": ["https://www.toyotaofdowntownla.com", "https://www.mbofsmithtown.com"], "condition": "used", "maxVehiclesPerDealer": 300, "fetchDetails": true, "concurrency": 3}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/dealer-inventory-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Car Dealer Website Inventory Scraper: VIN, Price & Stock free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/dealer-inventory-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/dealer-inventory-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Car & Vehicle Scrapers

- [AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers](autotrader-canada.md): Our autotrader.ca scraper makes it simple to collect car listings at scale. It automatically gathers URLs from all available pages and...
- [AutoScout24 Scraper: Car Listings, Prices & Dealer Contacts](autoscout24.md): AutoScout24 car listings from autoscout24.de, .at, .fr, .it, .es, .nl, .be, .lu and .com: price, make, model, mileage, first registration...
- [AutoTrader.ca Price Drop Monitor & Car Scraper](autotrader-ca.md): Monitor AutoTrader Canada searches and get only new listings, price drops and sold cars since the last run, with previous price and price...
- [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](kijiji-scraper.md): Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location...
- [CarGurus Scraper (US, Canada & UK Car Listings)](cargurus-listings-scraper.md): Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing.
- [autotrader.co.za Car Scraper with Seller Phone Numbers](autotrader-co-za-scraper.md): Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number.

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/dealer-inventory-scraper](https://automationbyexperts.com/apify/dealer-inventory-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/dealer-inventory-scraper.md](https://automationbyexperts.com/apify/dealer-inventory-scraper.md)
