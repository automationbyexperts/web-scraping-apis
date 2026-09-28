# Translate Excel, CSV & Websites in Bulk with AI | No API Key

**Translate Excel, CSV & Websites in Bulk with AI | No API Key** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Translate Excel, CSV and Google Sheets files, whole websites, PDFs and SRT/VTT subtitles into 42 languages in one run, and get the same file back translated. Brand terms, HTML and {{variables}} stay intact, and repeat runs only pay for what changed. No API key needed.

[Run it on Apify](https://apify.com/fayoussef/bulk-ai-translator?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/bulk-ai-translator?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Bulk AI Tools](../categories/ai-bulk-tools.md)

## Key facts

| | |
|---|---|
| Category | [Bulk AI Tools](../categories/ai-bulk-tools.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-ai-translator?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-28 |

## What you can do with Translate Excel, CSV & Websites in Bulk with AI | No API Key

- **[Translate a product catalog into 5 languages](https://apify.com/fayoussef/bulk-ai-translator/examples/translate-product-catalog-5-languages?fpr=youssef)**: Translates a list of product strings into German, French, Spanish, Italian and Dutch in marketing tone, keeping brand names in the glossary untouched and preserving placeholders and HTML. One run, five localised...
- **[Translate a whole website into German](https://apify.com/fayoussef/bulk-ai-translator/examples/translate-website-into-german?fpr=youssef)**: Crawls up to 25 pages of a site, staying on the same domain, and returns the German translation of every text block with its source URL and original text side by side, tags and links intact. The quickest way to get a...

## How to use Translate Excel, CSV & Websites in Bulk with AI | No API Key

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "mode": "text",
  "targetLanguages": [
    "de",
    "fr",
    "es",
    "it",
    "nl"
  ],
  "texts": [
    "EcoBrew insulated travel mug, 450 ml, keeps drinks hot for 8 hours.",
    "Leak proof lid with one handed open. Dishwasher safe.",
    "Free shipping on orders over 50 EUR. 30 day returns."
  ],
  "glossary": [
    "EcoBrew"
  ],
  "tone": "marketing",
  "model": "google/gemini-2.5-flash"
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'mode': 'text',
 'targetLanguages': ['de', 'fr', 'es', 'it', 'nl'],
 'texts': ['EcoBrew insulated travel mug, 450 ml, keeps drinks hot for 8 hours.',
           'Leak proof lid with one handed open. Dishwasher safe.',
           'Free shipping on orders over 50 EUR. 30 day returns.'],
 'glossary': ['EcoBrew'],
 'tone': 'marketing',
 'model': 'google/gemini-2.5-flash'}
run = client.actor("fayoussef/bulk-ai-translator").call(run_input=run_input)

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
  "mode": "text",
  "targetLanguages": [
    "de",
    "fr",
    "es",
    "it",
    "nl"
  ],
  "texts": [
    "EcoBrew insulated travel mug, 450 ml, keeps drinks hot for 8 hours.",
    "Leak proof lid with one handed open. Dishwasher safe.",
    "Free shipping on orders over 50 EUR. 30 day returns."
  ],
  "glossary": [
    "EcoBrew"
  ],
  "tone": "marketing",
  "model": "google/gemini-2.5-flash"
};
const run = await client.actor('fayoussef/bulk-ai-translator').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~bulk-ai-translator/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"mode": "text", "targetLanguages": ["de", "fr", "es", "it", "nl"], "texts": ["EcoBrew insulated travel mug, 450 ml, keeps drinks hot for 8 hours.", "Leak proof lid with one handed open. Dishwasher safe.", "Free shipping on orders over 50 EUR. 30 day returns."], "glossary": ["EcoBrew"], "tone": "marketing", "model": "google/gemini-2.5-flash"}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/bulk-ai-translator
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Translate Excel, CSV & Websites in Bulk with AI | No API Key free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-ai-translator?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/bulk-ai-translator` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Bulk AI Tools

- [Bulk AI Image Generator: Nano Banana, GPT Image | No API Key](bulk-ai-image-generator.md): Generate hundreds of AI images from a list of prompts or an Excel/CSV file with Nano Banana Pro, Nano Banana 2 and GPT Image. Any aspect...
- [Run ChatGPT, Claude, Gemini & DeepSeek in Bulk (No API Key)](bulk-llm-runner.md): Run hundreds of prompts in parallel across GPT, Claude, Gemini, Perplexity, DeepSeek, Qwen, Kimi and 350+ models, with web search, JSON...
- [Bulk Text to Speech: MP3 + SRT Subtitles | No API Key](bulk-text-to-speech.md): Convert texts or an Excel/CSV file into MP3 voiceovers with perfectly timed SRT/VTT subtitles. 322 neural voices in 75 languages...

## More

- Full catalog: [all 54 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/bulk-ai-translator](https://automationbyexperts.com/apify/bulk-ai-translator?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/bulk-ai-translator.md](https://automationbyexperts.com/apify/bulk-ai-translator.md)
