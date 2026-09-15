# Canada411 Scraper: Business Phones, Addresses

**Canada411 Scraper: Business Phones, Addresses** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing.

[Run it on Apify](https://apify.com/fayoussef/canada411-ca?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/canada411-ca?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/canada411-ca?fpr=youssef)) |
| Rating | 5.0 out of 5 (1 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with Canada411 Scraper: Business Phones, Addresses

- **[Find business phone numbers in Toronto](https://apify.com/fayoussef/canada411-ca/examples/find-business-phone-numbers-toronto?fpr=youssef)**: Looks up every plumber listed on Canada411 in Toronto and returns name, phone number and street address for each. Change the business type or the city and the same task becomes a local B2B calling list for any trade in...
- **[Look up people by name and city on Canada411](https://apify.com/fayoussef/canada411-ca/examples/lookup-people-by-name-canada411?fpr=youssef)**: Searches Canada411's residential listings for a surname in a city and returns each match with phone number and address. Skip tracers, genealogists and recruiters use it to find listed contacts without paying per lookup...
- **[Reverse address lookup on Canada411](https://apify.com/fayoussef/canada411-ca/examples/reverse-address-lookup-canada411?fpr=youssef)**: Leave the name empty and put a full street address in Where to get everyone Canada411 lists at that address, with their phone numbers. Property managers, process servers and door to door teams use it to know who is...

## How to use Canada411 Scraper: Business Phones, Addresses

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "what": "plumber",
  "where": "Toronto, ON",
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
run_input = {'what': 'plumber', 'where': 'Toronto, ON', 'max_pages': 5}
run = client.actor("fayoussef/canada411-ca").call(run_input=run_input)

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
  "what": "plumber",
  "where": "Toronto, ON",
  "max_pages": 5
};
const run = await client.actor('fayoussef/canada411-ca').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~canada411-ca/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"what": "plumber", "where": "Toronto, ON", "max_pages": 5}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/canada411-ca
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Canada411 Scraper: Business Phones, Addresses free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/canada411-ca?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/canada411-ca` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Lead Generation Actors

- [Whop Content Rewards Scraper: Clipping & UGC Campaigns](whop-clipping-campaigns-scraper.md): Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a...
- [thebluebook.com Scraper](thebluebook-scraper.md): Scrape verified contractor and subcontractor profiles from thebluebook.com - the largest US construction directory - into clean JSON, CSV...
- [GitHub Developer Lead Finder & Email Enricher](github-developer-leads.md): Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B...
- [Journalist Request Finder: HARO Alternative for Digital PR](journalist-request-finder.md): Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon...
- [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](luma-events-scraper.md): Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest...
- [ATS Job Scraper: Greenhouse, Lever & Ashby by Company Domain](company-domain-to-job-postings.md): Paste company domains, get their live job postings. Finds each company's ATS board across Greenhouse, Lever, Ashby, Recruitee...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/canada411-ca](https://automationbyexperts.com/apify/canada411-ca?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/canada411-ca.md](https://automationbyexperts.com/apify/canada411-ca.md)
