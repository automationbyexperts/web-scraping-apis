# Naukrigulf Scraper: Gulf Jobs in 12 Languages

**Naukrigulf Scraper: Gulf Jobs in 12 Languages** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape Naukrigulf.com jobs across the UAE, Saudi Arabia, Qatar, Kuwait, Bahrain and Oman. Search in Arabic, Hindi, Malayalam, Tagalog and 8 more, and read every result back in your language. Filters on what the site hides: salary, nationality and gender requirements, agency vs direct employer.

[Run it on Apify](https://apify.com/fayoussef/naukrigulf-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/naukrigulf-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/naukrigulf-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-21 |

## What you can do with Naukrigulf Scraper: Gulf Jobs in 12 Languages

- **[Find nurse jobs across the Gulf posted this week](https://apify.com/fayoussef/naukrigulf-scraper/examples/nurse-jobs-gulf-last-7-days?fpr=youssef)**: Searches Naukrigulf for nursing roles across the six GCC countries posted in the last 7 days, newest first, and returns each with employer, city, salary band where published, experience asked, nationality and gender...
- **[Get Dubai accounting jobs that publish a salary](https://apify.com/fayoussef/naukrigulf-scraper/examples/dubai-accounting-jobs-with-salary?fpr=youssef)**: Keeps only accountant roles in Dubai where the employer states the salary and hires directly rather than through an agency, so every row has a real monthly USD band and a real company behind it. The salary view puts the...

## How to use Naukrigulf Scraper: Gulf Jobs in 12 Languages

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "searchKeywords": [
    "nurse"
  ],
  "location": "gulf",
  "gccOnly": true,
  "datePosted": "7",
  "sortBy": "date",
  "outputLanguage": "en",
  "maxItems": 300,
  "includeRecruiterContacts": true
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'searchKeywords': ['nurse'],
 'location': 'gulf',
 'gccOnly': True,
 'datePosted': '7',
 'sortBy': 'date',
 'outputLanguage': 'en',
 'maxItems': 300,
 'includeRecruiterContacts': True}
run = client.actor("fayoussef/naukrigulf-scraper").call(run_input=run_input)

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
  "searchKeywords": [
    "nurse"
  ],
  "location": "gulf",
  "gccOnly": true,
  "datePosted": "7",
  "sortBy": "date",
  "outputLanguage": "en",
  "maxItems": 300,
  "includeRecruiterContacts": true
};
const run = await client.actor('fayoussef/naukrigulf-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~naukrigulf-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"searchKeywords": ["nurse"], "location": "gulf", "gccOnly": true, "datePosted": "7", "sortBy": "date", "outputLanguage": "en", "maxItems": 300, "includeRecruiterContacts": true}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/naukrigulf-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Naukrigulf Scraper: Gulf Jobs in 12 Languages free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/naukrigulf-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/naukrigulf-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Lead Generation Actors

- [Canada411 Scraper: Business Phones, Addresses](canada411-ca.md): Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing.
- [Whop Content Rewards Scraper: Clipping & UGC Campaigns](whop-clipping-campaigns-scraper.md): Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a...
- [Journalist Request Finder: HARO Alternative for Digital PR](journalist-request-finder.md): Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon...
- [thebluebook.com Scraper](thebluebook-scraper.md): Scrape verified contractor and subcontractor profiles from thebluebook.com - the largest US construction directory - into clean JSON, CSV...
- [GitHub Developer Lead Finder & Email Enricher](github-developer-leads.md): Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B...
- [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](luma-events-scraper.md): Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest...

## More

- Full catalog: [all 54 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/naukrigulf-scraper](https://automationbyexperts.com/apify/naukrigulf-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/naukrigulf-scraper.md](https://automationbyexperts.com/apify/naukrigulf-scraper.md)
