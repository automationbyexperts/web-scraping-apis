# Dataset Diff: Only New & Changed Items From Any Actor

**Dataset Diff: Only New & Changed Items From Any Actor** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Point it at any Apify Actor, Task or dataset and get only what changed since its last run: new rows, edited rows, rows that disappeared. Push the delta to Slack, Discord, Telegram or a webhook. No target website, so nothing breaks.

[Run it on Apify](https://apify.com/fayoussef/dataset-diff?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/dataset-diff?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Developer Tools & APIs](../categories/developer-tools.md)

## Key facts

| | |
|---|---|
| Category | [Developer Tools & APIs](../categories/developer-tools.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/dataset-diff?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with Dataset Diff: Only New & Changed Items From Any Actor

- **[Get only new places from a Google Maps scraper run](https://apify.com/fayoussef/dataset-diff/examples/new-google-maps-places-only?fpr=youssef)**: Chains after the Google Maps Scraper on your account and returns only the places that were not in its previous run, keyed on placeId, instead of the full list every time. The first run records a baseline and reports...
- **[Get price change alerts from any Actor's dataset](https://apify.com/fayoussef/dataset-diff/examples/price-change-alerts-from-any-dataset?fpr=youssef)**: Compares each run of a source Actor against its previous one and emits only the items whose price field changed, with old and new values, ignoring fields that move on their own like timestamps and rank. Add a Slack...

## How to use Dataset Diff: Only New & Changed Items From Any Actor

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "source": "apify/google-maps-scraper",
  "emit": [
    "new"
  ],
  "identityFields": [
    "placeId"
  ],
  "firstRunBehaviour": "baselineOnly",
  "outputMode": "deltaOnly"
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'source': 'apify/google-maps-scraper',
 'emit': ['new'],
 'identityFields': ['placeId'],
 'firstRunBehaviour': 'baselineOnly',
 'outputMode': 'deltaOnly'}
run = client.actor("fayoussef/dataset-diff").call(run_input=run_input)

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
  "source": "apify/google-maps-scraper",
  "emit": [
    "new"
  ],
  "identityFields": [
    "placeId"
  ],
  "firstRunBehaviour": "baselineOnly",
  "outputMode": "deltaOnly"
};
const run = await client.actor('fayoussef/dataset-diff').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~dataset-diff/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"source": "apify/google-maps-scraper", "emit": ["new"], "identityFields": ["placeId"], "firstRunBehaviour": "baselineOnly", "outputMode": "deltaOnly"}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/dataset-diff
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Dataset Diff: Only New & Changed Items From Any Actor free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/dataset-diff?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/dataset-diff` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Developer Tools & APIs

- [Scrape any site, Anti-Bot Proxy, JS Render & AI](scrape-any-site-anti-bot-proxy-js-render-ai.md): Free web scraper API for any website. Rotating anti-bot proxies, JS rendering, screenshots, CSS + AI extraction. Clean HTML, Markdown and...
- [Website Change Detector: Page Diff, Price & Content Alerts](website-change-monitor.md): Monitor any web page for changes and get a line-by-line diff of what was added and removed. Track competitor pricing, product listings...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/dataset-diff](https://automationbyexperts.com/apify/dataset-diff?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/dataset-diff.md](https://automationbyexperts.com/apify/dataset-diff.md)
