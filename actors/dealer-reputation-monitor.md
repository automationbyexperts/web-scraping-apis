# Car Dealer Review Alerts: DealerRater Bad Review Monitor

**Car Dealer Review Alerts: DealerRater Bad Review Monitor** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Get alerted when a car dealership gets a new 1 or 2 star review or its rating drops. Watch dealers by name, URL or market on DealerRater, see which salesperson the review names, and send alerts to Slack, Discord, Telegram or any webhook. Also exports every review with sub-scores.

[Run it on Apify](https://apify.com/fayoussef/dealer-reputation-monitor?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/dealer-reputation-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Car & Vehicle Scrapers](../categories/vehicle-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Car & Vehicle Scrapers](../categories/vehicle-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/dealer-reputation-monitor?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-26 |

## What you can do with Car Dealer Review Alerts: DealerRater Bad Review Monitor

- **[Export every DealerRater review for a dealership](https://apify.com/fayoussef/dealer-reputation-monitor/examples/dealerrater-reviews-export?fpr=youssef)**: Type a dealership name and get its 200 most recent DealerRater reviews with full text, star rating, date, the department and the name of the employee each customer dealt with, plus one summary row with the store's...
- **[Get alerted to new 1 and 2 star dealer reviews](https://apify.com/fayoussef/dealer-reputation-monitor/examples/negative-dealer-review-alerts?fpr=youssef)**: Keeps only reviews rated 2 stars or lower and, with the new since last run switch on, returns just the ones that appeared since the previous run. Schedule it daily for each store and a general manager hears about a bad...

## How to use Car Dealer Review Alerts: DealerRater Bad Review Monitor

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "dealers": [
    "Hendrick Honda"
  ],
  "maxReviewsPerDealer": 200,
  "maxDealersPerSearch": 1,
  "includeDealerSummary": true
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'dealers': ['Hendrick Honda'],
 'maxReviewsPerDealer': 200,
 'maxDealersPerSearch': 1,
 'includeDealerSummary': True}
run = client.actor("fayoussef/dealer-reputation-monitor").call(run_input=run_input)

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
  "dealers": [
    "Hendrick Honda"
  ],
  "maxReviewsPerDealer": 200,
  "maxDealersPerSearch": 1,
  "includeDealerSummary": true
};
const run = await client.actor('fayoussef/dealer-reputation-monitor').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~dealer-reputation-monitor/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"dealers": ["Hendrick Honda"], "maxReviewsPerDealer": 200, "maxDealersPerSearch": 1, "includeDealerSummary": true}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/dealer-reputation-monitor
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

### From AI agents with no Apify account (x402 or Skyfire)

This actor accepts [agentic payments](../agentic-payments.md): an AI agent can run it and pay per run with USDC (x402) or a Skyfire token, with no Apify account.

```bash
# x402: TOKEN is the prepaid token bought from Apify AGI with USDC on Base
curl -X POST "https://api.apify.com/v2/acts/fayoussef~dealer-reputation-monitor/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'

# Skyfire: send the PAY token instead
curl -X POST "https://api.apify.com/v2/acts/fayoussef~dealer-reputation-monitor/run-sync-get-dataset-items" \
  -H "skyfire-pay-id: $SKYFIRE_PAY_TOKEN" -H "Content-Type: application/json" -d '{}'
```

With MCP and Skyfire: `https://mcp.apify.com?payment=skyfire&tools=fayoussef/dealer-reputation-monitor`

## FAQ

### Is Car Dealer Review Alerts: DealerRater Bad Review Monitor free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/dealer-reputation-monitor?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/dealer-reputation-monitor` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can an AI agent run it without an Apify account?

Yes. This actor accepts agentic payments: an agent can pay per run with USDC through the x402 protocol, or with a Skyfire PAY token, and no Apify account is needed. See [AI agents and x402 payments](../agentic-payments.md).

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Car & Vehicle Scrapers

- [AutoTrader.ca Scraper: Car Prices, VIN, Mileage & Dealers](autotrader-canada.md): Scrape AutoTrader.ca car listings: price, mileage, VIN, specs, dealer phone and photos from any search or the filter form. Optional Find...
- [AutoScout24 Scraper: Car Listings, Prices & Dealer Contacts](autoscout24.md): AutoScout24 car listings from autoscout24.de, .at, .fr, .it, .es, .nl, .be, .lu and .com: price, make, model, mileage, first registration...
- [CarGurus Scraper: US, Canada & UK Car Listings, VIN & Prices](cargurus-listings-scraper.md): Scrape CarGurus car listings from cargurus.com, .ca and .co.uk by search URL or ZIP code: price, deal rating, mileage, VIN, specs, dealer...
- [AutoTrader.ca Price Drop Monitor & Car Scraper](autotrader-ca.md): Monitor AutoTrader Canada searches and get only new listings, price drops and sold cars since the last run, with price history. Schedule it...
- [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](kijiji-scraper.md): Scrape Kijiji.ca listings from any search or ad URL: cars, real estate and every other category. Get price, location, phone number, specs...
- [AutoTrader South Africa Price Drop Monitor and Scraper](autotrader-co-za-scraper.md): Track autotrader.co.za for new listings, price drops and sold cars, or scrape every listing with price, mileage, specs and dealer. Optional...

## More

- Full catalog: [all 59 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/dealer-reputation-monitor](https://automationbyexperts.com/apify/dealer-reputation-monitor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/dealer-reputation-monitor.md](https://automationbyexperts.com/apify/dealer-reputation-monitor.md)
