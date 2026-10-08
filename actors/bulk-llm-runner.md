# Run ChatGPT, Claude, Gemini & DeepSeek in Bulk (No API Key)

**Run ChatGPT, Claude, Gemini & DeepSeek in Bulk (No API Key)** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Run hundreds of prompts in parallel across GPT, Claude, Gemini, Perplexity, DeepSeek, Qwen, Kimi and 350+ models, with web search, JSON columns and side-by-side model comparison. Optional: upload an Excel, CSV or Google Sheet to run AI on every row. No API key needed.

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
| Catalog updated | 2026-10-08 |

## What you can do with Run ChatGPT, Claude, Gemini & DeepSeek in Bulk (No API Key)

- **[Write SEO product descriptions in bulk](https://apify.com/fayoussef/bulk-llm-runner/examples/seo-product-descriptions-in-bulk?fpr=youssef)**: Feed it one line per product and get back a structured description for each: a short benefit led paragraph, a set of feature bullets and a meta description. Output arrives as JSON columns you can paste straight into a...
- **[Classify and tag customer reviews at scale](https://apify.com/fayoussef/bulk-llm-runner/examples/classify-customer-reviews?fpr=youssef)**: Runs every review through the same rubric and returns sentiment, a topic tag, an urgency flag and a one line summary as separate columns. Temperature is held low so the labels stay consistent across the batch, which is...
- **[Compare GPT, Claude and Gemini side by side](https://apify.com/fayoussef/bulk-llm-runner/examples/compare-gpt-claude-gemini-answers?fpr=youssef)**: Sends the same prompts to GPT-5, Claude Sonnet 5, Gemini 3.8 Flash and Perplexity Sonar, then returns one row per model per prompt with the answer, the cost and the token count. Use it to pick a model on evidence from...

## How to use Run ChatGPT, Claude, Gemini & DeepSeek in Bulk (No API Key)

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "prompts": [
    "Product: Patagonia Nano Puff insulated jacket. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.",
    "Product: Hydro Flask 32oz wide mouth water bottle. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.",
    "Product: Anker 737 140W USB-C power bank. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.",
    "Product: Brooks Ghost 16 neutral running shoe. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description."
  ],
  "system_prompt": "You are a senior ecommerce SEO copywriter. Write in plain, concrete language. Never invent specifications you were not given. Return the keys description, bullets and meta_description.",
  "model": "anthropic/claude-haiku-4.5",
  "response_format": "json_object",
  "enable_web_search": false,
  "temperature": 60,
  "concurrency": 4
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'prompts': ['Product: Patagonia Nano Puff insulated jacket. Write a 60 word benefit '
             'led description, 4 feature bullets, and a 155 character meta '
             'description.',
             'Product: Hydro Flask 32oz wide mouth water bottle. Write a 60 word '
             'benefit led description, 4 feature bullets, and a 155 character meta '
             'description.',
             'Product: Anker 737 140W USB-C power bank. Write a 60 word benefit led '
             'description, 4 feature bullets, and a 155 character meta description.',
             'Product: Brooks Ghost 16 neutral running shoe. Write a 60 word benefit '
             'led description, 4 feature bullets, and a 155 character meta '
             'description.'],
 'system_prompt': 'You are a senior ecommerce SEO copywriter. Write in plain, concrete '
                  'language. Never invent specifications you were not given. Return '
                  'the keys description, bullets and meta_description.',
 'model': 'anthropic/claude-haiku-4.5',
 'response_format': 'json_object',
 'enable_web_search': False,
 'temperature': 60,
 'concurrency': 4}
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
  "prompts": [
    "Product: Patagonia Nano Puff insulated jacket. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.",
    "Product: Hydro Flask 32oz wide mouth water bottle. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.",
    "Product: Anker 737 140W USB-C power bank. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.",
    "Product: Brooks Ghost 16 neutral running shoe. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description."
  ],
  "system_prompt": "You are a senior ecommerce SEO copywriter. Write in plain, concrete language. Never invent specifications you were not given. Return the keys description, bullets and meta_description.",
  "model": "anthropic/claude-haiku-4.5",
  "response_format": "json_object",
  "enable_web_search": false,
  "temperature": 60,
  "concurrency": 4
};
const run = await client.actor('fayoussef/bulk-llm-runner').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~bulk-llm-runner/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["Product: Patagonia Nano Puff insulated jacket. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.", "Product: Hydro Flask 32oz wide mouth water bottle. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.", "Product: Anker 737 140W USB-C power bank. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description.", "Product: Brooks Ghost 16 neutral running shoe. Write a 60 word benefit led description, 4 feature bullets, and a 155 character meta description."], "system_prompt": "You are a senior ecommerce SEO copywriter. Write in plain, concrete language. Never invent specifications you were not given. Return the keys description, bullets and meta_description.", "model": "anthropic/claude-haiku-4.5", "response_format": "json_object", "enable_web_search": false, "temperature": 60, "concurrency": 4}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/bulk-llm-runner
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Run ChatGPT, Claude, Gemini & DeepSeek in Bulk (No API Key) free to try?

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

- [Bulk AI Image Generator: Nano Banana, GPT Image | No API Key](bulk-ai-image-generator.md): Generate hundreds of AI images from a list of prompts or an Excel/CSV file with Nano Banana Pro, Nano Banana 2 and GPT Image. Any aspect...
- [Bulk Text to Speech: MP3 + SRT Subtitles | No API Key](bulk-text-to-speech.md): Convert texts or an Excel/CSV file into MP3 voiceovers with perfectly timed SRT/VTT subtitles. 322 neural voices in 75 languages...
- [Translate Excel, CSV & Websites in Bulk with AI | No API Key](bulk-ai-translator.md): Translate Excel, CSV and Google Sheets files, whole websites, PDFs and SRT/VTT subtitles into 42 languages in one run, and get the same...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/bulk-llm-runner](https://automationbyexperts.com/apify/bulk-llm-runner?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/bulk-llm-runner.md](https://automationbyexperts.com/apify/bulk-llm-runner.md)
