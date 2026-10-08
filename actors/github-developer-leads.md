# GitHub Developer Lead Finder & Email Enricher

**GitHub Developer Lead Finder & Email Enricher** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B outreach.

[Run it on Apify](https://apify.com/fayoussef/github-developer-leads?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/github-developer-leads?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Lead Generation Actors](../categories/lead-generation.md)

## Key facts

| | |
|---|---|
| Category | [Lead Generation Actors](../categories/lead-generation.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/github-developer-leads?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-08 |

## What you can do with GitHub Developer Lead Finder & Email Enricher

- **[Build an outreach list of React contributors](https://apify.com/fayoussef/github-developer-leads/examples/react-contributors-outreach-list?fpr=youssef)**: Lists the contributors to facebook/react, finds each one's email from public commits, and enriches the profile with inferred tech stack, total stars and hireable flag. DevRel teams and dev tool founders use it to reach...
- **[Find TypeScript developers in London with emails](https://apify.com/fayoussef/github-developer-leads/examples/typescript-developers-london-with-emails?fpr=youssef)**: Searches GitHub for TypeScript developers located in London with more than 100 followers, mines their public commit history for a contactable email, and keeps only profiles where one was found. Each lead carries...

## How to use GitHub Developer Lead Finder & Email Enricher

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "searchType": "contributors",
  "repositories": [
    "facebook/react"
  ],
  "maxItems": 200,
  "extractEmails": true,
  "onlyWithEmail": true,
  "enrichStats": true
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'searchType': 'contributors',
 'repositories': ['facebook/react'],
 'maxItems': 200,
 'extractEmails': True,
 'onlyWithEmail': True,
 'enrichStats': True}
run = client.actor("fayoussef/github-developer-leads").call(run_input=run_input)

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
  "searchType": "contributors",
  "repositories": [
    "facebook/react"
  ],
  "maxItems": 200,
  "extractEmails": true,
  "onlyWithEmail": true,
  "enrichStats": true
};
const run = await client.actor('fayoussef/github-developer-leads').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~github-developer-leads/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"searchType": "contributors", "repositories": ["facebook/react"], "maxItems": 200, "extractEmails": true, "onlyWithEmail": true, "enrichStats": true}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/github-developer-leads
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

### From AI agents with no Apify account (x402 or Skyfire)

This actor accepts [agentic payments](../agentic-payments.md): an AI agent can run it and pay per run with USDC (x402) or a Skyfire token, with no Apify account.

```bash
# x402: TOKEN is the prepaid token bought from Apify AGI with USDC on Base
curl -X POST "https://api.apify.com/v2/acts/fayoussef~github-developer-leads/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'

# Skyfire: send the PAY token instead
curl -X POST "https://api.apify.com/v2/acts/fayoussef~github-developer-leads/run-sync-get-dataset-items" \
  -H "skyfire-pay-id: $SKYFIRE_PAY_TOKEN" -H "Content-Type: application/json" -d '{}'
```

With MCP and Skyfire: `https://mcp.apify.com?payment=skyfire&tools=fayoussef/github-developer-leads`

## FAQ

### Is GitHub Developer Lead Finder & Email Enricher free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/github-developer-leads?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/github-developer-leads` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can an AI agent run it without an Apify account?

Yes. This actor accepts agentic payments: an agent can pay per run with USDC through the x402 protocol, or with a Skyfire PAY token, and no Apify account is needed. See [AI agents and x402 payments](../agentic-payments.md).

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Lead Generation Actors

- [Canada411 Scraper: Business Phones, Addresses](canada411-ca.md): Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing.
- [Journalist Request Finder: HARO Alternative for Digital PR](journalist-request-finder.md): Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon...
- [Whop Content Rewards Scraper: Clipping & UGC Campaigns](whop-clipping-campaigns-scraper.md): Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a...
- [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](luma-events-scraper.md): Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest...
- [11888.gr Scraper: Greek Business Phones, Emails & Websites](11888-gr-scraper.md): Scrape Greek businesses from the 11888.gr Yellow Pages by category and place: name, phones, mobile, email, website, address, GPS and...
- [AI Account Watch: Custom Sales Trigger Alerts](ai-account-watch.md): Watch a list of companies and get alerted when one does what you describe in plain English: raises funding, hires a CMO, opens a location...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/github-developer-leads](https://automationbyexperts.com/apify/github-developer-leads?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/github-developer-leads.md](https://automationbyexperts.com/apify/github-developer-leads.md)
