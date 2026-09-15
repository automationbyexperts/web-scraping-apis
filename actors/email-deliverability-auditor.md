# SPF, DKIM & DMARC Checker: Email Deliverability Auditor

**SPF, DKIM & DMARC Checker: Email Deliverability Auditor** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Audit any domain's email deliverability in seconds. Checks SPF, DKIM (around 30 selectors), DMARC, MX, MTA-STS, BIMI and DNSSEC, tests your mail servers against DNS blacklists, and returns a 0-100 score with prioritized fixes. Bulk-ready. No login and no SMTP connection, just fast DNS.

[Run it on Apify](https://apify.com/fayoussef/email-deliverability-auditor?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/email-deliverability-auditor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All SEO & AI Visibility](../categories/seo-ai-visibility.md)

## Key facts

| | |
|---|---|
| Category | [SEO & AI Visibility](../categories/seo-ai-visibility.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/email-deliverability-auditor?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with SPF, DKIM & DMARC Checker: Email Deliverability Auditor

- **[Check SPF, DKIM and DMARC for a list of domains](https://apify.com/fayoussef/email-deliverability-auditor/examples/spf-dkim-dmarc-check-for-domains?fpr=youssef)**: Reads the public DNS of each domain and reports whether SPF, DKIM and DMARC are present and correctly configured, whether the SPF policy is strict or open, which DKIM selectors exist, plus MX, MTA-STS, BIMI and DNSSEC...
- **[Audit email authentication for all agency clients at once](https://apify.com/fayoussef/email-deliverability-auditor/examples/agency-client-email-authentication-audit?fpr=youssef)**: Runs the full deliverability audit across a whole client list in parallel, probing the Google and Microsoft 365 DKIM selectors on top of the 30 common ones, and returns one row per domain that says exactly what is...

## How to use SPF, DKIM & DMARC Checker: Email Deliverability Auditor

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "domains": [
    "apify.com",
    "google.com",
    "github.com"
  ],
  "checkBlacklists": true,
  "concurrency": 10
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'domains': ['apify.com', 'google.com', 'github.com'],
 'checkBlacklists': True,
 'concurrency': 10}
run = client.actor("fayoussef/email-deliverability-auditor").call(run_input=run_input)

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
  "domains": [
    "apify.com",
    "google.com",
    "github.com"
  ],
  "checkBlacklists": true,
  "concurrency": 10
};
const run = await client.actor('fayoussef/email-deliverability-auditor').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~email-deliverability-auditor/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"domains": ["apify.com", "google.com", "github.com"], "checkBlacklists": true, "concurrency": 10}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/email-deliverability-auditor
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is SPF, DKIM & DMARC Checker: Email Deliverability Auditor free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/email-deliverability-auditor?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/email-deliverability-auditor` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related SEO & AI Visibility

- [SEO, GEO & AEO Audit: AI Search Readiness Checker](seo-geo-aeo-audit.md): Audit any website for Google SEO and AI search visibility in one run. Get 0-100 SEO, GEO & AEO scores per page, AI-crawler & llms.txt...
- [Google Maps Geo-Grid Local Rank Tracker](geo-grid-local-rank-tracker.md): Track where a business ranks in the Google Maps local pack across a grid of points around it. Per-point rank, average rank, coverage, Share...
- [AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)](ai-brand-visibility-tracker.md): Is AI recommending you or your competitors? Track brand mentions, ranking position, sentiment, share of voice and cited sources in ChatGPT...
- [llms.txt Generator: llms-full.txt for Any Website (AI SEO)](llms-txt-generator.md): Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/email-deliverability-auditor](https://automationbyexperts.com/apify/email-deliverability-auditor?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/email-deliverability-auditor.md](https://automationbyexperts.com/apify/email-deliverability-auditor.md)
