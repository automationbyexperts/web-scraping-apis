# Journalist Request Finder: HARO Alternative for Digital PR

**Journalist Request Finder: HARO Alternative for Digital PR** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon. Filter by your topics, sort by deadline, and schedule daily runs that return only new requests. No HARO account, no Qwoted login, no API keys.

[Run it on Apify](https://apify.com/fayoussef/journalist-request-finder?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/journalist-request-finder?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/journalist-request-finder?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with Journalist Request Finder: HARO Alternative for Digital PR

- **[Find journalist requests about SaaS and marketing](https://apify.com/fayoussef/journalist-request-finder/examples/journalist-requests-saas-marketing?fpr=youssef)**: Collects live source requests from SourceBottle and Bluesky that mention SaaS, marketing or small business, keeps only those whose deadline has not passed, and ranks them most pitchable first. The free HARO replacement...
- **[Daily alerts for new media requests in your niche](https://apify.com/fayoussef/journalist-request-finder/examples/daily-new-media-request-alerts?fpr=youssef)**: Scans all three free sources for requests mentioning cybersecurity, AI or fintech, drops anything off topic, and returns only requests not seen in a previous run. Schedule it every morning and the pitch queue view is...

## How to use Journalist Request Finder: HARO Alternative for Digital PR

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "keywords": [
    "SaaS",
    "marketing",
    "small business"
  ],
  "sources": [
    "sourcebottle",
    "bluesky"
  ],
  "onlyOpenDeadlines": true,
  "maxRequests": 200
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'keywords': ['SaaS', 'marketing', 'small business'],
 'sources': ['sourcebottle', 'bluesky'],
 'onlyOpenDeadlines': True,
 'maxRequests': 200}
run = client.actor("fayoussef/journalist-request-finder").call(run_input=run_input)

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
  "keywords": [
    "SaaS",
    "marketing",
    "small business"
  ],
  "sources": [
    "sourcebottle",
    "bluesky"
  ],
  "onlyOpenDeadlines": true,
  "maxRequests": 200
};
const run = await client.actor('fayoussef/journalist-request-finder').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~journalist-request-finder/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["SaaS", "marketing", "small business"], "sources": ["sourcebottle", "bluesky"], "onlyOpenDeadlines": true, "maxRequests": 200}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/journalist-request-finder
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Journalist Request Finder: HARO Alternative for Digital PR free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/journalist-request-finder?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/journalist-request-finder` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Lead Generation Actors

- [Canada411 Scraper: Business Phones, Addresses](canada411-ca.md): Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing.
- [Whop Content Rewards Scraper: Clipping & UGC Campaigns](whop-clipping-campaigns-scraper.md): Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a...
- [GitHub Developer Lead Finder & Email Enricher](github-developer-leads.md): Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B...
- [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](luma-events-scraper.md): Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest...
- [11888.gr Scraper: Greek Business Phones, Emails & Websites](11888-gr-scraper.md): Scrape Greek businesses from the 11888.gr Yellow Pages by category and place: name, phones, mobile, email, website, address, GPS and...
- [AI Account Watch: Custom Sales Trigger Alerts](ai-account-watch.md): Watch a list of companies and get alerted when one does what you describe in plain English: raises funding, hires a CMO, opens a location...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/journalist-request-finder](https://automationbyexperts.com/apify/journalist-request-finder?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/journalist-request-finder.md](https://automationbyexperts.com/apify/journalist-request-finder.md)
