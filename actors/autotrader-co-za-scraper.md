# autotrader.co.za Car Scraper with Seller Phone Numbers

**autotrader.co.za Car Scraper with Seller Phone Numbers** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number.

[Run it on Apify](https://apify.com/fayoussef/autotrader-co-za-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/autotrader-co-za-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Car & Vehicle Scrapers](../categories/vehicle-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Car & Vehicle Scrapers](../categories/vehicle-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/autotrader-co-za-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-28 |

## What you can do with autotrader.co.za Car Scraper with Seller Phone Numbers

- **[Find used Toyota Hilux bakkies with seller phone numbers](https://apify.com/fayoussef/autotrader-co-za-scraper/examples/used-bakkies-with-seller-phone-numbers?fpr=youssef)**: Scrapes Toyota Hilux listings on AutoTrader South Africa and, on a paid plan, also returns the seller phone number AutoTrader hides behind a captcha, so the row is ready to call. Includes ZAR price, mileage, year...
- **[Export nearly new automatic cars for sale in South Africa](https://apify.com/fayoussef/autotrader-co-za-scraper/examples/nearly-new-automatic-cars-south-africa?fpr=youssef)**: Returns 2023 and newer automatic cars listed on AutoTrader.co.za with price, mileage, engine and power figures, dealer rating, location and gallery images. Useful for dealers sizing the late model market and for buyers...

## How to use autotrader.co.za Car Scraper with Seller Phone Numbers

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "start_urls": [
    {
      "url": "https://www.autotrader.co.za/cars-for-sale/toyota/hilux"
    }
  ],
  "scrape_phone_numbers": true,
  "max_items": 200
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'start_urls': [{'url': 'https://www.autotrader.co.za/cars-for-sale/toyota/hilux'}],
 'scrape_phone_numbers': True,
 'max_items': 200}
run = client.actor("fayoussef/autotrader-co-za-scraper").call(run_input=run_input)

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
      "url": "https://www.autotrader.co.za/cars-for-sale/toyota/hilux"
    }
  ],
  "scrape_phone_numbers": true,
  "max_items": 200
};
const run = await client.actor('fayoussef/autotrader-co-za-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~autotrader-co-za-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"start_urls": [{"url": "https://www.autotrader.co.za/cars-for-sale/toyota/hilux"}], "scrape_phone_numbers": true, "max_items": 200}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/autotrader-co-za-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is autotrader.co.za Car Scraper with Seller Phone Numbers free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/autotrader-co-za-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/autotrader-co-za-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Car & Vehicle Scrapers

- [AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers](autotrader-canada.md): Our autotrader.ca scraper makes it simple to collect car listings at scale. It automatically gathers URLs from all available pages and...
- [AutoScout24 Scraper: Car Listings, Prices & Dealer Contacts](autoscout24.md): AutoScout24 car listings from autoscout24.de, .at, .fr, .it, .es, .nl, .be, .lu and .com: price, make, model, mileage, first registration...
- [AutoTrader.ca Price Drop Monitor & Car Scraper](autotrader-ca.md): Monitor AutoTrader Canada searches and get only new listings, price drops and sold cars since the last run, with previous price and price...
- [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](kijiji-scraper.md): Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location...
- [CarGurus Scraper (US, Canada & UK Car Listings)](cargurus-listings-scraper.md): Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing.
- [AutoTrader Australia Car Scraper: Prices, VIN & Dealers](autotrader-au-scraper.md): Scrape Autotrader Australia. Paste any autotrader.com.au search URL to export every vehicle: price, make, model, variant, year, odometer...

## More

- Full catalog: [all 54 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/autotrader-co-za-scraper](https://automationbyexperts.com/apify/autotrader-co-za-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/autotrader-co-za-scraper.md](https://automationbyexperts.com/apify/autotrader-co-za-scraper.md)
