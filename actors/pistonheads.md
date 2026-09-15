# PistonHeads Scraper: UK Used, Classic & Performance Cars

**PistonHeads Scraper: UK Used, Classic & Performance Cars** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Our pistonheads.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing card.

[Run it on Apify](https://apify.com/fayoussef/pistonheads?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/pistonheads?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Car & Vehicle Scrapers](../categories/vehicle-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Car & Vehicle Scrapers](../categories/vehicle-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/pistonheads?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with PistonHeads Scraper: UK Used, Classic & Performance Cars

- **[Track Porsche 911s for sale on PistonHeads](https://apify.com/fayoussef/pistonheads/examples/porsche-911-for-sale-uk?fpr=youssef)**: Reads PistonHeads search results for Porsche 911 and returns 30 plus fields per car: GBP price, year, mileage, engine, power, CO2, fuel economy, seller type and phone, and location. Schedule it weekly and you have a...
- **[Find performance cars between 20,000 and 40,000 GBP](https://apify.com/fayoussef/pistonheads/examples/performance-cars-20k-to-40k-uk?fpr=youssef)**: Pulls PistonHeads listings priced between 20,000 and 40,000 GBP from 2015 onwards, 16 per page, with full specs, seller contact and location. The sweet spot for enthusiast buyers and specialist dealers sourcing stock...

## How to use PistonHeads Scraper: UK Used, Classic & Performance Cars

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "start_urls": [
    {
      "url": "https://www.pistonheads.com/buy/search?make=porsche&model=911"
    }
  ],
  "max_pages": 5
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'start_urls': [{'url': 'https://www.pistonheads.com/buy/search?make=porsche&model=911'}],
 'max_pages': 5}
run = client.actor("fayoussef/pistonheads").call(run_input=run_input)

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
      "url": "https://www.pistonheads.com/buy/search?make=porsche&model=911"
    }
  ],
  "max_pages": 5
};
const run = await client.actor('fayoussef/pistonheads').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~pistonheads/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"start_urls": [{"url": "https://www.pistonheads.com/buy/search?make=porsche&model=911"}], "max_pages": 5}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/pistonheads
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is PistonHeads Scraper: UK Used, Classic & Performance Cars free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/pistonheads?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/pistonheads` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Car & Vehicle Scrapers

- [AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers](autotrader-canada.md): Our autotrader.ca scraper makes it simple to collect car listings at scale. It automatically gathers URLs from all available pages and...
- [AutoScout24 All-Country Scraper](autoscout24.md): Our autoscout24 scraper makes it simple to collect listings at scale and in all countries. Works on autoscout24.de, .at, .fr, .it, .es...
- [AutoTrader Canada Car Scraper](autotrader-ca.md): Our autotrader.ca scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing cars.
- [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](kijiji-scraper.md): Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location...
- [CarGurus Scraper (US, Canada & UK Car Listings)](cargurus-listings-scraper.md): Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing.
- [autotrader.co.za Car Scraper with Seller Phone Numbers](autotrader-co-za-scraper.md): Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number.

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/pistonheads](https://automationbyexperts.com/apify/pistonheads?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/pistonheads.md](https://automationbyexperts.com/apify/pistonheads.md)
