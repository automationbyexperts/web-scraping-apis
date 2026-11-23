# 350+ AI Models: Run ChatGPT, Claude, Gemini in Bulk

**350+ AI Models: Run ChatGPT, Claude, Gemini in Bulk** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Run hundreds of prompts in parallel across GPT, Claude, Gemini, Perplexity, DeepSeek, Qwen, Kimi and 350+ models, with web search, JSON columns and side-by-side model comparison. Optional: upload an Excel, CSV or Google Sheet to run AI on every row. No API key needed.

[Run it on Apify](https://apify.com/fayoussef/bulk-llm-runner?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/bulk-llm-runner?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Bulk AI Tools](../categories/ai-bulk-tools.md)

## Key facts

| | |
|---|---|
| Category | [Bulk AI Tools](../categories/ai-bulk-tools.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-llm-runner?fpr=youssef)) |
| Rating | 5.0 out of 5 (2 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-11-23 |

## What you can do with 350+ AI Models: Run ChatGPT, Claude, Gemini in Bulk

- **[Run a ChatGPT prompt for every row of a Google Sheet](https://apify.com/fayoussef/bulk-llm-runner/examples/run-chatgpt-prompts-from-google-sheet?fpr=youssef)**: Have a Google Sheet or Excel file with one ChatGPT prompt per SKU, product or row? Paste the link and every prompt runs exactly as written with GPT-5 Mini, no copy-pasting into ChatGPT one by one. You get your sheet...

## How to use 350+ AI Models: Run ChatGPT, Claude, Gemini in Bulk

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "spreadsheet_file": "https://api.apify.com/v2/key-value-stores/I40EWpLzQaVq08gCm/records/sku-chatgpt-prompts-sample.csv",
  "prompts": [
    "{{Prompt}}"
  ],
  "model": "openai/gpt-5-mini",
  "enable_web_search": false,
  "response_format": "text",
  "reasoning_effort": "low",
  "concurrency": 4,
  "system_prompt": "You are an ecommerce copywriter. Follow each prompt exactly as written and return only the finished copy, with no preamble, headings or notes."
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'spreadsheet_file': 'https://api.apify.com/v2/key-value-stores/I40EWpLzQaVq08gCm/records/sku-chatgpt-prompts-sample.csv',
 'prompts': ['{{Prompt}}'],
 'model': 'openai/gpt-5-mini',
 'enable_web_search': False,
 'response_format': 'text',
 'reasoning_effort': 'low',
 'concurrency': 4,
 'system_prompt': 'You are an ecommerce copywriter. Follow each prompt exactly as '
                  'written and return only the finished copy, with no preamble, '
                  'headings or notes.'}
run = client.actor("fayoussef/bulk-llm-runner").call(run_input=run_input)

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
  "spreadsheet_file": "https://api.apify.com/v2/key-value-stores/I40EWpLzQaVq08gCm/records/sku-chatgpt-prompts-sample.csv",
  "prompts": [
    "{{Prompt}}"
  ],
  "model": "openai/gpt-5-mini",
  "enable_web_search": false,
  "response_format": "text",
  "reasoning_effort": "low",
  "concurrency": 4,
  "system_prompt": "You are an ecommerce copywriter. Follow each prompt exactly as written and return only the finished copy, with no preamble, headings or notes."
};
const run = await client.actor('fayoussef/bulk-llm-runner').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~bulk-llm-runner/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"spreadsheet_file": "https://api.apify.com/v2/key-value-stores/I40EWpLzQaVq08gCm/records/sku-chatgpt-prompts-sample.csv", "prompts": ["{{Prompt}}"], "model": "openai/gpt-5-mini", "enable_web_search": false, "response_format": "text", "reasoning_effort": "low", "concurrency": 4, "system_prompt": "You are an ecommerce copywriter. Follow each prompt exactly as written and return only the finished copy, with no preamble, headings or notes."}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/bulk-llm-runner
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is 350+ AI Models: Run ChatGPT, Claude, Gemini in Bulk free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-llm-runner?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/bulk-llm-runner` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Bulk AI Tools

- [Bulk AI Image Generator & Photo Editor: Nano Banana Pro](bulk-ai-image-generator.md): Generate hundreds of AI images from prompts or an Excel/CSV file, or edit your own product photos in bulk: white or transparent background...
- [Bulk Text to Speech: MP3 + SRT Subtitles | No API Key](bulk-text-to-speech.md): Convert texts or an Excel/CSV file into MP3 voiceovers with perfectly timed SRT/VTT subtitles. 322 neural voices in 75 languages...
- [Translate Excel, CSV & Websites in Bulk with AI | No API Key](bulk-ai-translator.md): Translate Excel, CSV and Google Sheets files, whole websites, PDFs and SRT/VTT subtitles into 42 languages in one run, and get the same...

## More

- Full catalog: [all 67 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/bulk-llm-runner](https://automationbyexperts.com/apify/bulk-llm-runner?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/bulk-llm-runner.md](https://automationbyexperts.com/apify/bulk-llm-runner.md)
