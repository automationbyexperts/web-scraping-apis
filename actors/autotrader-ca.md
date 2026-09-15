# AutoTrader Canada Car Scraper

**AutoTrader Canada Car Scraper** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Our autotrader.ca scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing cars.

[Run it on Apify](https://apify.com/fayoussef/autotrader-ca?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/autotrader-ca?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Car & Vehicle Scrapers](../categories/vehicle-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Car & Vehicle Scrapers](../categories/vehicle-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/autotrader-ca?fpr=youssef)) |
| Rating | 5.0 out of 5 (2 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with AutoTrader Canada Car Scraper

- **[Find used Honda Civics for sale around Montreal](https://apify.com/fayoussef/autotrader-ca/examples/honda-civic-used-montreal?fpr=youssef)**: Searches AutoTrader.ca with the built in filters for used Honda Civic from model year 2018 within 100 km of Montreal and returns 127 fields per car: VIN, numeric price, kilometres, trim, transmission, dealer name and...
- **[Export used SUVs under 25,000 CAD around Ottawa](https://apify.com/fayoussef/autotrader-ca/examples/used-suvs-under-25000-ottawa?fpr=youssef)**: Pulls used SUV listings priced under 25,000 CAD within 100 km of Ottawa from AutoTrader.ca with VIN, price, kilometres, drivetrain, fuel, dealer and photos. Family buyers and small dealers get the whole affordable SUV...

## How to use AutoTrader Canada Car Scraper

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "conditions": [
    "used"
  ],
  "include_damaged": false,
  "makes": [
    "Honda"
  ],
  "max_items": 300,
  "model_year_from": 2018,
  "models": [
    "Civic"
  ],
  "postal_code": "Montreal, QC",
  "radius_km": "100",
  "sort_descending": false,
  "vehicle_type": "cars"
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'conditions': ['used'],
 'include_damaged': False,
 'makes': ['Honda'],
 'max_items': 300,
 'model_year_from': 2018,
 'models': ['Civic'],
 'postal_code': 'Montreal, QC',
 'radius_km': '100',
 'sort_descending': False,
 'vehicle_type': 'cars'}
run = client.actor("fayoussef/autotrader-ca").call(run_input=run_input)

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
  "conditions": [
    "used"
  ],
  "include_damaged": false,
  "makes": [
    "Honda"
  ],
  "max_items": 300,
  "model_year_from": 2018,
  "models": [
    "Civic"
  ],
  "postal_code": "Montreal, QC",
  "radius_km": "100",
  "sort_descending": false,
  "vehicle_type": "cars"
};
const run = await client.actor('fayoussef/autotrader-ca').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~autotrader-ca/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"conditions": ["used"], "include_damaged": false, "makes": ["Honda"], "max_items": 300, "model_year_from": 2018, "models": ["Civic"], "postal_code": "Montreal, QC", "radius_km": "100", "sort_descending": false, "vehicle_type": "cars"}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/autotrader-ca
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is AutoTrader Canada Car Scraper free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/autotrader-ca?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/autotrader-ca` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Car & Vehicle Scrapers

- [AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers](autotrader-canada.md): Our autotrader.ca scraper makes it simple to collect car listings at scale. It automatically gathers URLs from all available pages and...
- [AutoScout24 All-Country Scraper](autoscout24.md): Our autoscout24 scraper makes it simple to collect listings at scale and in all countries. Works on autoscout24.de, .at, .fr, .it, .es...
- [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](kijiji-scraper.md): Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location...
- [CarGurus Scraper (US, Canada & UK Car Listings)](cargurus-listings-scraper.md): Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing.
- [autotrader.co.za Car Scraper with Seller Phone Numbers](autotrader-co-za-scraper.md): Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number.
- [AutoTrader Australia Car Scraper: Prices, VIN & Dealers](autotrader-au-scraper.md): Scrape Autotrader Australia. Paste any autotrader.com.au search URL to export every vehicle: price, make, model, variant, year, odometer...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/autotrader-ca](https://automationbyexperts.com/apify/autotrader-ca?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/autotrader-ca.md](https://automationbyexperts.com/apify/autotrader-ca.md)
