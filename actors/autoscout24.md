# AutoScout24 All-Country Scraper

**AutoScout24 All-Country Scraper** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Our autoscout24 scraper makes it simple to collect listings at scale and in all countries. Works on autoscout24.de, .at, .fr, .it, .es, .nl, .be, .lu and .com

[Run it on Apify](https://apify.com/fayoussef/autoscout24?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/autoscout24?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Car & Vehicle Scrapers](../categories/vehicle-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Car & Vehicle Scrapers](../categories/vehicle-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/autoscout24?fpr=youssef)) |
| Rating | 5.0 out of 5 (1 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with AutoScout24 All-Country Scraper

- **[Find used VW Golfs in Germany under 15,000 EUR](https://apify.com/fayoussef/autoscout24/examples/vw-golf-germany-under-15000?fpr=youssef)**: Uses the built in filter form to search autoscout24.de for used Volkswagen Golf listings from 2016 onwards priced under 15,000 EUR, cheapest first, and returns 50 plus fields per car: price, mileage, equipment, dealer...
- **[Export used electric cars in the Netherlands and Belgium](https://apify.com/fayoussef/autoscout24/examples/electric-cars-netherlands-belgium?fpr=youssef)**: Searches AutoScout24 for used fully electric cars located in the Netherlands and Belgium and exports each listing with price, mileage, battery and range fields, first registration, dealer details and photos. Built for...
- **[Track new dealer SUV listings in Italy each week](https://apify.com/fayoussef/autoscout24/examples/new-dealer-suv-listings-italy?fpr=youssef)**: Returns SUV and off road listings posted by dealers on autoscout24.it in the last 7 days, newest first. Schedule it weekly and you have a running feed of fresh dealer stock in Italy, with price, mileage, equipment and...

## How to use AutoScout24 All-Country Scraper

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "search_domain": "de",
  "countries": [
    "germany"
  ],
  "makes": [
    "Volkswagen"
  ],
  "models": [
    "Golf"
  ],
  "conditions": [
    "used"
  ],
  "price_to": 15000,
  "first_registration_from": 2016,
  "sort_by": "price",
  "max_items": 300
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'search_domain': 'de',
 'countries': ['germany'],
 'makes': ['Volkswagen'],
 'models': ['Golf'],
 'conditions': ['used'],
 'price_to': 15000,
 'first_registration_from': 2016,
 'sort_by': 'price',
 'max_items': 300}
run = client.actor("fayoussef/autoscout24").call(run_input=run_input)

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
  "search_domain": "de",
  "countries": [
    "germany"
  ],
  "makes": [
    "Volkswagen"
  ],
  "models": [
    "Golf"
  ],
  "conditions": [
    "used"
  ],
  "price_to": 15000,
  "first_registration_from": 2016,
  "sort_by": "price",
  "max_items": 300
};
const run = await client.actor('fayoussef/autoscout24').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~autoscout24/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"search_domain": "de", "countries": ["germany"], "makes": ["Volkswagen"], "models": ["Golf"], "conditions": ["used"], "price_to": 15000, "first_registration_from": 2016, "sort_by": "price", "max_items": 300}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/autoscout24
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is AutoScout24 All-Country Scraper free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/autoscout24?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/autoscout24` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Car & Vehicle Scrapers

- [AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers](autotrader-canada.md): Our autotrader.ca scraper makes it simple to collect car listings at scale. It automatically gathers URLs from all available pages and...
- [AutoTrader Canada Car Scraper](autotrader-ca.md): Our autotrader.ca scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing cars.
- [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](kijiji-scraper.md): Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location...
- [CarGurus Scraper (US, Canada & UK Car Listings)](cargurus-listings-scraper.md): Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing.
- [autotrader.co.za Car Scraper with Seller Phone Numbers](autotrader-co-za-scraper.md): Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number.
- [AutoTrader Australia Car Scraper: Prices, VIN & Dealers](autotrader-au-scraper.md): Scrape Autotrader Australia. Paste any autotrader.com.au search URL to export every vehicle: price, make, model, variant, year, odometer...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/autoscout24](https://automationbyexperts.com/apify/autoscout24?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/autoscout24.md](https://automationbyexperts.com/apify/autoscout24.md)
