# Reddit Scraper for Leads: Buying Intent Posts & Comments

**Reddit Scraper for Leads: Buying Intent Posts & Comments** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape Reddit posts and comments for buying intent: people asking for a tool, a recommendation, or an alternative to your competitor. Every lead is scored 0-100, budget mentions are extracted, and scheduled runs surface only leads you have not seen before. No login, no API key, no LLM cost.

[Run it on Apify](https://apify.com/fayoussef/reddit-lead-finder?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/reddit-lead-finder?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/reddit-lead-finder?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with Reddit Scraper for Leads: Buying Intent Posts & Comments

- **[Find Reddit users looking for an email marketing tool](https://apify.com/fayoussef/reddit-lead-finder/examples/reddit-leads-for-email-marketing-tools?fpr=youssef)**: Scans Reddit posts and comments from the past week for people asking for an email marketing tool or an alternative to Mailchimp or Klaviyo, scores each for buying intent, and returns the ones at 30 or above with the...
- **[Get alerted to 'alternative to' threads about your competitors](https://apify.com/fayoussef/reddit-lead-finder/examples/competitor-alternative-threads-alert?fpr=youssef)**: Watches r/smallbusiness, r/Entrepreneur and r/sales for people asking for a CRM or an alternative to HubSpot or Salesforce, keeps only strong buying signals at 50 plus, and returns just the leads not seen in a previous...

## How to use Reddit Scraper for Leads: Buying Intent Posts & Comments

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "keywords": [
    "email marketing tool"
  ],
  "competitors": [
    "Mailchimp",
    "Klaviyo"
  ],
  "timeRange": "week",
  "includeComments": true,
  "minIntentScore": 30,
  "maxLeads": 100
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'keywords': ['email marketing tool'],
 'competitors': ['Mailchimp', 'Klaviyo'],
 'timeRange': 'week',
 'includeComments': True,
 'minIntentScore': 30,
 'maxLeads': 100}
run = client.actor("fayoussef/reddit-lead-finder").call(run_input=run_input)

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
    "email marketing tool"
  ],
  "competitors": [
    "Mailchimp",
    "Klaviyo"
  ],
  "timeRange": "week",
  "includeComments": true,
  "minIntentScore": 30,
  "maxLeads": 100
};
const run = await client.actor('fayoussef/reddit-lead-finder').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~reddit-lead-finder/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["email marketing tool"], "competitors": ["Mailchimp", "Klaviyo"], "timeRange": "week", "includeComments": true, "minIntentScore": 30, "maxLeads": 100}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/reddit-lead-finder
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Reddit Scraper for Leads: Buying Intent Posts & Comments free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/reddit-lead-finder?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/reddit-lead-finder` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Lead Generation Actors

- [Canada411 Scraper: Business Phones, Addresses](canada411-ca.md): Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing.
- [Journalist Request Finder: HARO Alternative for Digital PR](journalist-request-finder.md): Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon...
- [Whop Content Rewards Scraper: Clipping & UGC Campaigns](whop-clipping-campaigns-scraper.md): Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a...
- [GitHub Developer Lead Finder & Email Enricher](github-developer-leads.md): Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B...
- [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](luma-events-scraper.md): Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest...
- [11888.gr Scraper: Greek Business Phones, Emails & Websites](11888-gr-scraper.md): Scrape Greek businesses from the 11888.gr Yellow Pages by category and place: name, phones, mobile, email, website, address, GPS and...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/reddit-lead-finder](https://automationbyexperts.com/apify/reddit-lead-finder?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/reddit-lead-finder.md](https://automationbyexperts.com/apify/reddit-lead-finder.md)
