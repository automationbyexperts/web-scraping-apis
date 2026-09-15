# Podcast Guesting Lead Finder: Find Shows & Host Emails

**Podcast Guesting Lead Finder: Find Shows & Host Emails** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Find active, on-topic podcasts that book guests, with the host's contact email, ready for outreach. Search any niche on Apple's podcast index, filter to shows with a public email, and let scheduled runs surface only NEW shows. No login, no API keys.

[Run it on Apify](https://apify.com/fayoussef/podcast-guest-finder?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/podcast-guest-finder?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/podcast-guest-finder?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with Podcast Guesting Lead Finder: Find Shows & Host Emails

- **[Find B2B SaaS podcasts with host emails](https://apify.com/fayoussef/podcast-guest-finder/examples/b2b-saas-podcasts-with-host-emails?fpr=youssef)**: Searches Apple Podcasts for shows about B2B SaaS and startup founders, keeps only those that published in the last 90 days and expose a host or owner email in their RSS feed, and returns a pitch ready list with show...
- **[Build a pitch list of real estate investing podcasts](https://apify.com/fayoussef/podcast-guest-finder/examples/real-estate-investing-podcast-pitch-list?fpr=youssef)**: Finds real estate investing shows whose description signals an interview format, drops any without a reachable host email or without a recent episode, and returns up to 100 leads. What a podcast booking agency charges...

## How to use Podcast Guesting Lead Finder: Find Shows & Host Emails

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "keywords": [
    "B2B SaaS",
    "startup founders"
  ],
  "requireEmail": true,
  "activeWithinDays": 90,
  "country": "US",
  "maxPodcasts": 100
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'keywords': ['B2B SaaS', 'startup founders'],
 'requireEmail': True,
 'activeWithinDays': 90,
 'country': 'US',
 'maxPodcasts': 100}
run = client.actor("fayoussef/podcast-guest-finder").call(run_input=run_input)

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
    "B2B SaaS",
    "startup founders"
  ],
  "requireEmail": true,
  "activeWithinDays": 90,
  "country": "US",
  "maxPodcasts": 100
};
const run = await client.actor('fayoussef/podcast-guest-finder').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~podcast-guest-finder/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["B2B SaaS", "startup founders"], "requireEmail": true, "activeWithinDays": 90, "country": "US", "maxPodcasts": 100}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/podcast-guest-finder
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Podcast Guesting Lead Finder: Find Shows & Host Emails free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/podcast-guest-finder?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/podcast-guest-finder` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Lead Generation Actors

- [Canada411 Scraper: Business Phones, Addresses](canada411-ca.md): Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing.
- [Whop Content Rewards Scraper: Clipping & UGC Campaigns](whop-clipping-campaigns-scraper.md): Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a...
- [thebluebook.com Scraper](thebluebook-scraper.md): Scrape verified contractor and subcontractor profiles from thebluebook.com - the largest US construction directory - into clean JSON, CSV...
- [GitHub Developer Lead Finder & Email Enricher](github-developer-leads.md): Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B...
- [Journalist Request Finder: HARO Alternative for Digital PR](journalist-request-finder.md): Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon...
- [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](luma-events-scraper.md): Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/podcast-guest-finder](https://automationbyexperts.com/apify/podcast-guest-finder?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/podcast-guest-finder.md](https://automationbyexperts.com/apify/podcast-guest-finder.md)
