# RentFaster Scraper: Canada Rentals, Rents & Landlord Phones

**RentFaster Scraper: Canada Rentals, Rents & Landlord Phones** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape Canadian rental listings from RentFaster.ca in 105 cities (Calgary, Edmonton, Toronto, Montreal...). Filter by type, bedrooms, rent, pets and utilities. Export rent, beds, baths, sq ft, address, GPS, landlord phone and website to JSON, CSV or Excel.

[Run it on Apify](https://apify.com/fayoussef/rentfaster-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/rentfaster-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Real Estate Scrapers](../categories/real-estate-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Real Estate Scrapers](../categories/real-estate-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/rentfaster-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-08 |

## How to use RentFaster Scraper: Canada Rentals, Rents & Landlord Phones

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
run = client.actor("fayoussef/rentfaster-scraper").call(run_input=run_input)

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
const run = await client.actor('fayoussef/rentfaster-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~rentfaster-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/rentfaster-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

### From AI agents with no Apify account (x402 or Skyfire)

This actor accepts [agentic payments](../agentic-payments.md): an AI agent can run it and pay per run with USDC (x402) or a Skyfire token, with no Apify account.

```bash
# x402: TOKEN is the prepaid token bought from Apify AGI with USDC on Base
curl -X POST "https://api.apify.com/v2/acts/fayoussef~rentfaster-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'

# Skyfire: send the PAY token instead
curl -X POST "https://api.apify.com/v2/acts/fayoussef~rentfaster-scraper/run-sync-get-dataset-items" \
  -H "skyfire-pay-id: $SKYFIRE_PAY_TOKEN" -H "Content-Type: application/json" -d '{}'
```

With MCP and Skyfire: `https://mcp.apify.com?payment=skyfire&tools=fayoussef/rentfaster-scraper`

## FAQ

### Is RentFaster Scraper: Canada Rentals, Rents & Landlord Phones free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/rentfaster-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/rentfaster-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can an AI agent run it without an Apify account?

Yes. This actor accepts agentic payments: an agent can pay per run with USDC through the x402 protocol, or with a Skyfire PAY token, and no Apify account is needed. See [AI agents and x402 payments](../agentic-payments.md).

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Real Estate Scrapers

- [Spitogatos Real Estate Scraper: Greece Listings & Agent Phones](spitogatos-scraper.md): Scrape Greece real estate listings from Spitogatos.gr, the country's largest property portal. Homes, land and commercial property for sale...
- [XE.gr Greek Property Scraper](xe-gr-scraper.md): Scrape Greek real estate listings from XE.gr: prices, size, rooms, GPS coordinates, amenities, photos and advertiser phone numbers. Works...
- [Centris.ca Scraper: Quebec Real Estate Listings & Photos](centris-property-scraper.md): Scrape Centris.ca real estate listings into clean structured data: MLS number, price, full address, rooms, bedrooms, bathrooms, the full...
- [Cyprus Property Scraper: Spitogatos.com.cy Listings & Agents](spitogatos-cy-scraper.md): Scrape Cyprus real estate listings and estate agents from Spitogatos.com.cy, in English or Greek. Search by town, price and property type...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/rentfaster-scraper](https://automationbyexperts.com/apify/rentfaster-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/rentfaster-scraper.md](https://automationbyexperts.com/apify/rentfaster-scraper.md)
