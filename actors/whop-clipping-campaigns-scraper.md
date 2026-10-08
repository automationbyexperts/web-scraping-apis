# Whop Content Rewards Scraper: Clipping & UGC Campaigns

**Whop Content Rewards Scraper: Clipping & UGC Campaigns** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a private archive of campaigns that have rotated off the public page, so you can benchmark CPM rates, track budget burn and catch new clipping campaigns.

[Run it on Apify](https://apify.com/fayoussef/whop-clipping-campaigns-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/whop-clipping-campaigns-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/whop-clipping-campaigns-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-08 |

## What you can do with Whop Content Rewards Scraper: Clipping & UGC Campaigns

- **[Find the highest paying clipping campaigns on Whop](https://apify.com/fayoussef/whop-clipping-campaigns-scraper/examples/high-paying-clipping-campaigns?fpr=youssef)**: Lists every live Whop Content Rewards campaign paying at least 2 dollars per 1,000 views with more than 1,000 dollars of budget still unspent, sorted by reward. Use it to pick the campaigns where a clip actually gets...
- **[Find low competition TikTok clipping campaigns](https://apify.com/fayoussef/whop-clipping-campaigns-scraper/examples/low-competition-tiktok-clipping-campaigns?fpr=youssef)**: Filters Whop Content Rewards down to TikTok campaigns with 50 or fewer creators already submitting and no application step, so you can start clipping today and compete for views against a small pool. Sorted by fewest...
- **[Get alerted when new Whop campaigns launch](https://apify.com/fayoussef/whop-clipping-campaigns-scraper/examples/new-content-rewards-campaigns-alert?fpr=youssef)**: Monitoring mode: each run returns only the campaigns that were not in the previous run, so a daily schedule becomes an alert feed for fresh clipping and UGC campaigns. Pair it with the Apify Slack or email integration...

## How to use Whop Content Rewards Scraper: Clipping & UGC Campaigns

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "sortBy": "reward",
  "minRewardPerThousand": 2,
  "minBudgetLeftUsd": 1000,
  "maxItems": 100
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'sortBy': 'reward',
 'minRewardPerThousand': 2,
 'minBudgetLeftUsd': 1000,
 'maxItems': 100}
run = client.actor("fayoussef/whop-clipping-campaigns-scraper").call(run_input=run_input)

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
  "sortBy": "reward",
  "minRewardPerThousand": 2,
  "minBudgetLeftUsd": 1000,
  "maxItems": 100
};
const run = await client.actor('fayoussef/whop-clipping-campaigns-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~whop-clipping-campaigns-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"sortBy": "reward", "minRewardPerThousand": 2, "minBudgetLeftUsd": 1000, "maxItems": 100}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/whop-clipping-campaigns-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Whop Content Rewards Scraper: Clipping & UGC Campaigns free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/whop-clipping-campaigns-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/whop-clipping-campaigns-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Lead Generation Actors

- [Canada411 Scraper: Business Phones, Addresses](canada411-ca.md): Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing.
- [Journalist Request Finder: HARO Alternative for Digital PR](journalist-request-finder.md): Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon...
- [GitHub Developer Lead Finder & Email Enricher](github-developer-leads.md): Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B...
- [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](luma-events-scraper.md): Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest...
- [11888.gr Scraper: Greek Business Phones, Emails & Websites](11888-gr-scraper.md): Scrape Greek businesses from the 11888.gr Yellow Pages by category and place: name, phones, mobile, email, website, address, GPS and...
- [AI Account Watch: Custom Sales Trigger Alerts](ai-account-watch.md): Watch a list of companies and get alerted when one does what you describe in plain English: raises funding, hires a CMO, opens a location...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/whop-clipping-campaigns-scraper](https://automationbyexperts.com/apify/whop-clipping-campaigns-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/whop-clipping-campaigns-scraper.md](https://automationbyexperts.com/apify/whop-clipping-campaigns-scraper.md)
