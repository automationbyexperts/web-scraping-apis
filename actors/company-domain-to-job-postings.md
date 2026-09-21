# ATS Job Scraper: Greenhouse, Lever & Ashby by Company Domain

**ATS Job Scraper: Greenhouse, Lever & Ashby by Company Domain** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Paste company domains, get their live job postings. Finds each company's ATS board across Greenhouse, Lever, Ashby, Recruitee, SmartRecruiters and Personio, verifies it really belongs to them, and returns every open role with salary, seniority, location and remote type. No slug hunting.

[Run it on Apify](https://apify.com/fayoussef/company-domain-to-job-postings?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/company-domain-to-job-postings?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/company-domain-to-job-postings?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-21 |

## What you can do with ATS Job Scraper: Greenhouse, Lever & Ashby by Company Domain

- **[Get every engineering job at YC companies](https://apify.com/fayoussef/company-domain-to-job-postings/examples/engineering-jobs-at-yc-companies?fpr=youssef)**: Adds the curated Y Combinator company list to your own domains, finds each company's Greenhouse, Lever, Ashby, Recruitee, SmartRecruiters or Personio board, verifies it belongs to them, and returns every open role whose...
- **[Pull remote jobs from a list of company domains](https://apify.com/fayoussef/company-domain-to-job-postings/examples/remote-jobs-from-a-prospect-list?fpr=youssef)**: Paste domains straight from a CRM export and get back only the remote roles each company has open, with location, salary where published, department and full description. Recruiters and sales teams use it to know who is...

## How to use ATS Job Scraper: Greenhouse, Lever & Ashby by Company Domain

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "companies": [
    "stripe.com",
    "monzo.com"
  ],
  "preset": "yc_companies",
  "keywords": [
    "engineer",
    "developer"
  ],
  "includeDescription": true,
  "descriptionFormat": "markdown",
  "maxItems": 500
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'companies': ['stripe.com', 'monzo.com'],
 'preset': 'yc_companies',
 'keywords': ['engineer', 'developer'],
 'includeDescription': True,
 'descriptionFormat': 'markdown',
 'maxItems': 500}
run = client.actor("fayoussef/company-domain-to-job-postings").call(run_input=run_input)

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
  "companies": [
    "stripe.com",
    "monzo.com"
  ],
  "preset": "yc_companies",
  "keywords": [
    "engineer",
    "developer"
  ],
  "includeDescription": true,
  "descriptionFormat": "markdown",
  "maxItems": 500
};
const run = await client.actor('fayoussef/company-domain-to-job-postings').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~company-domain-to-job-postings/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["stripe.com", "monzo.com"], "preset": "yc_companies", "keywords": ["engineer", "developer"], "includeDescription": true, "descriptionFormat": "markdown", "maxItems": 500}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/company-domain-to-job-postings
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is ATS Job Scraper: Greenhouse, Lever & Ashby by Company Domain free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/company-domain-to-job-postings?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/company-domain-to-job-postings` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

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
- Website page: [https://automationbyexperts.com/apify/company-domain-to-job-postings](https://automationbyexperts.com/apify/company-domain-to-job-postings?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/company-domain-to-job-postings.md](https://automationbyexperts.com/apify/company-domain-to-job-postings.md)
