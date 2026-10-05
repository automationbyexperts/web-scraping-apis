# AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers

**AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Our autotrader.ca scraper makes it simple to collect car listings at scale. It automatically gathers URLs from all available pages and extracts complete details for every listing including price, mileage, year, and more.

[Run it on Apify](https://apify.com/fayoussef/autotrader-canada?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/autotrader-canada?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Car & Vehicle Scrapers](../categories/vehicle-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Car & Vehicle Scrapers](../categories/vehicle-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/autotrader-canada?fpr=youssef)) |
| Rating | 5.0 out of 5 (3 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers

- **[Find used Toyota RAV4s for sale around Toronto](https://apify.com/fayoussef/autotrader-canada/examples/toyota-rav4-used-toronto?fpr=youssef)**: Uses the filter form to search AutoTrader.ca for used Toyota RAV4 from model year 2019 within 100 km of Toronto and returns 127 fields per vehicle, including VIN, numeric price, kilometres, trim, dealer name and phone...
- **[Export used pickup trucks under 40,000 CAD in Alberta](https://apify.com/fayoussef/autotrader-canada/examples/used-pickup-trucks-alberta-under-40000?fpr=youssef)**: Searches AutoTrader.ca for used pickup trucks priced under 40,000 CAD within 200 km of Calgary and exports each with VIN, price, kilometres, engine, drivetrain, dealer and photos. Fleet buyers and dealers use it to...
- **[Track electric cars for sale in Vancouver](https://apify.com/fayoussef/autotrader-canada/examples/electric-cars-for-sale-vancouver?fpr=youssef)**: Returns new and used fully electric vehicles listed on AutoTrader.ca within 100 km of Vancouver, with price, kilometres, battery details, dealer and photos. Schedule it to follow BC's EV market week by week or run once...

## How to use AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "vehicle_type": "cars",
  "makes": [
    "Toyota"
  ],
  "models": [
    "RAV4"
  ],
  "conditions": [
    "used"
  ],
  "model_year_from": 2019,
  "postal_code": "Toronto, ON",
  "radius_km": "100",
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
run_input = {'vehicle_type': 'cars',
 'makes': ['Toyota'],
 'models': ['RAV4'],
 'conditions': ['used'],
 'model_year_from': 2019,
 'postal_code': 'Toronto, ON',
 'radius_km': '100',
 'max_items': 300}
run = client.actor("fayoussef/autotrader-canada").call(run_input=run_input)

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
  "vehicle_type": "cars",
  "makes": [
    "Toyota"
  ],
  "models": [
    "RAV4"
  ],
  "conditions": [
    "used"
  ],
  "model_year_from": 2019,
  "postal_code": "Toronto, ON",
  "radius_km": "100",
  "max_items": 300
};
const run = await client.actor('fayoussef/autotrader-canada').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~autotrader-canada/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"vehicle_type": "cars", "makes": ["Toyota"], "models": ["RAV4"], "conditions": ["used"], "model_year_from": 2019, "postal_code": "Toronto, ON", "radius_km": "100", "max_items": 300}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/autotrader-canada
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/autotrader-canada?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/autotrader-canada` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Car & Vehicle Scrapers

- [AutoScout24 Scraper: Car Listings, Prices & Dealer Contacts](autoscout24.md): AutoScout24 car listings from autoscout24.de, .at, .fr, .it, .es, .nl, .be, .lu and .com: price, make, model, mileage, first registration...
- [AutoTrader.ca Price Drop Monitor & Car Scraper](autotrader-ca.md): Monitor AutoTrader Canada searches and get only new listings, price drops and sold cars since the last run, with previous price and price...
- [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](kijiji-scraper.md): Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location...
- [CarGurus Scraper (US, Canada & UK Car Listings)](cargurus-listings-scraper.md): Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing.
- [autotrader.co.za Car Scraper with Seller Phone Numbers](autotrader-co-za-scraper.md): Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number.
- [AutoTrader Australia Car Scraper: Prices, VIN & Dealers](autotrader-au-scraper.md): Scrape Autotrader Australia. Paste any autotrader.com.au search URL to export every vehicle: price, make, model, variant, year, odometer...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/autotrader-canada](https://automationbyexperts.com/apify/autotrader-canada?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/autotrader-canada.md](https://automationbyexperts.com/apify/autotrader-canada.md)
