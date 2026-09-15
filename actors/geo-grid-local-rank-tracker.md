# Google Maps Geo-Grid Local Rank Tracker

**Google Maps Geo-Grid Local Rank Tracker** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Track where a business ranks in the Google Maps local pack across a grid of points around it. Per-point rank, average rank, coverage, Share of Local Voice, top competitors and an HTML heatmap. No Google API key.

[Run it on Apify](https://apify.com/fayoussef/geo-grid-local-rank-tracker?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/geo-grid-local-rank-tracker?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All SEO & AI Visibility](../categories/seo-ai-visibility.md)

## Key facts

| | |
|---|---|
| Category | [SEO & AI Visibility](../categories/seo-ai-visibility.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/geo-grid-local-rank-tracker?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with Google Maps Geo-Grid Local Rank Tracker

- **[Track a dentist's Google Maps ranking across a city](https://apify.com/fayoussef/geo-grid-local-rank-tracker/examples/dentist-google-maps-ranking-grid?fpr=youssef)**: Checks where a dental practice ranks in the Google Maps local pack from 49 points spread across a 7 by 7 grid, 3 miles from centre to edge, for the searches patients actually type. The result is a heat map of visibility...
- **[Measure a restaurant's local pack visibility by neighbourhood](https://apify.com/fayoussef/geo-grid-local-rank-tracker/examples/restaurant-local-pack-visibility?fpr=youssef)**: Runs burger restaurant and burgers near me from 25 points across a 5 by 5 grid around downtown Chicago and records the rank at each one. Restaurants live or die on the 3 pack within walking distance, and this shows...
- **[Weekly local SEO rank report for a plumbing company](https://apify.com/fayoussef/geo-grid-local-rank-tracker/examples/plumber-local-seo-rank-report?fpr=youssef)**: A 7 by 7 grid across a 5 mile radius of Denver for plumber and emergency plumber, the two searches that drive service calls. Schedule it weekly and the competitors view tells you who is taking the top spots in each...

## How to use Google Maps Geo-Grid Local Rank Tracker

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "businessName": "Aspen Dental",
  "keywords": [
    "dentist",
    "emergency dentist"
  ],
  "location": "Phoenix, AZ",
  "gridSize": 7,
  "radius": 3,
  "distanceUnit": "miles"
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'businessName': 'Aspen Dental',
 'keywords': ['dentist', 'emergency dentist'],
 'location': 'Phoenix, AZ',
 'gridSize': 7,
 'radius': 3,
 'distanceUnit': 'miles'}
run = client.actor("fayoussef/geo-grid-local-rank-tracker").call(run_input=run_input)

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
  "businessName": "Aspen Dental",
  "keywords": [
    "dentist",
    "emergency dentist"
  ],
  "location": "Phoenix, AZ",
  "gridSize": 7,
  "radius": 3,
  "distanceUnit": "miles"
};
const run = await client.actor('fayoussef/geo-grid-local-rank-tracker').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~geo-grid-local-rank-tracker/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"businessName": "Aspen Dental", "keywords": ["dentist", "emergency dentist"], "location": "Phoenix, AZ", "gridSize": 7, "radius": 3, "distanceUnit": "miles"}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/geo-grid-local-rank-tracker
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Google Maps Geo-Grid Local Rank Tracker free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/geo-grid-local-rank-tracker?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/geo-grid-local-rank-tracker` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related SEO & AI Visibility

- [SEO, GEO & AEO Audit: AI Search Readiness Checker](seo-geo-aeo-audit.md): Audit any website for Google SEO and AI search visibility in one run. Get 0-100 SEO, GEO & AEO scores per page, AI-crawler & llms.txt...
- [AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)](ai-brand-visibility-tracker.md): Is AI recommending you or your competitors? Track brand mentions, ranking position, sentiment, share of voice and cited sources in ChatGPT...
- [SPF, DKIM & DMARC Checker: Email Deliverability Auditor](email-deliverability-auditor.md): Audit any domain's email deliverability in seconds. Checks SPF, DKIM (around 30 selectors), DMARC, MX, MTA-STS, BIMI and DNSSEC, tests your...
- [llms.txt Generator: llms-full.txt for Any Website (AI SEO)](llms-txt-generator.md): Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/geo-grid-local-rank-tracker](https://automationbyexperts.com/apify/geo-grid-local-rank-tracker?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/geo-grid-local-rank-tracker.md](https://automationbyexperts.com/apify/geo-grid-local-rank-tracker.md)
