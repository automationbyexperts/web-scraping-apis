# Bulk Text to Speech MP3 + SRT Subtitles (No API Key)

**Bulk Text to Speech MP3 + SRT Subtitles (No API Key)** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Convert text to natural AI speech in bulk. 322 neural voices, 75+ languages, no API key. Every text becomes an MP3 voiceover plus perfectly timed SRT/VTT subtitles ideal for TikTok & YouTube faceless videos, e-learning and podcasts.

[Run it on Apify](https://apify.com/fayoussef/bulk-text-to-speech?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/bulk-text-to-speech?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Bulk AI Tools](../categories/ai-bulk-tools.md)

## Key facts

| | |
|---|---|
| Category | [Bulk AI Tools](../categories/ai-bulk-tools.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-text-to-speech?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with Bulk Text to Speech MP3 + SRT Subtitles (No API Key)

- **[Generate TikTok voiceovers with word by word captions](https://apify.com/fayoussef/bulk-text-to-speech/examples/tiktok-voiceovers-word-captions?fpr=youssef)**: Turns each script into an MP3 voiceover at 25 percent faster pace with a matching SRT where every word is its own cue, the format CapCut and Premiere use for animated captions. Paste 50 scripts and get 50 clips plus 50...
- **[Create Spanish voiceovers for product videos](https://apify.com/fayoussef/bulk-text-to-speech/examples/spanish-voiceovers-for-product-videos?fpr=youssef)**: Generates natural Castilian Spanish narration for a batch of product descriptions, one MP3 per text, with sentence level SRT subtitles ready to drop into the video editor. Swap the voice for Mexican Spanish, French...
- **[Turn long form text into one narrated MP3](https://apify.com/fayoussef/bulk-text-to-speech/examples/narrate-long-text-into-one-mp3?fpr=youssef)**: Narrates each chapter or section as its own clip, then joins them in order into a single combined MP3 with one continuous subtitle file. A slightly slower British voice suits articles, course material and internal...

## How to use Bulk Text to Speech MP3 + SRT Subtitles (No API Key)

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "texts": [
    "Three things nobody tells you before you start a side business. Number one: your first customer is probably someone you already know.",
    "Stop scrolling. This is the only productivity tip that actually worked for me, and it takes ten seconds.",
    "Here is how I plan my whole week in five minutes every Sunday night."
  ],
  "voice": "en-US-AvaMultilingualNeural",
  "speed": "+25%",
  "generateSubtitles": true,
  "subtitleGranularity": "word",
  "subtitleFormat": "srt"
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'texts': ['Three things nobody tells you before you start a side business. Number '
           'one: your first customer is probably someone you already know.',
           'Stop scrolling. This is the only productivity tip that actually worked for '
           'me, and it takes ten seconds.',
           'Here is how I plan my whole week in five minutes every Sunday night.'],
 'voice': 'en-US-AvaMultilingualNeural',
 'speed': '+25%',
 'generateSubtitles': True,
 'subtitleGranularity': 'word',
 'subtitleFormat': 'srt'}
run = client.actor("fayoussef/bulk-text-to-speech").call(run_input=run_input)

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
  "texts": [
    "Three things nobody tells you before you start a side business. Number one: your first customer is probably someone you already know.",
    "Stop scrolling. This is the only productivity tip that actually worked for me, and it takes ten seconds.",
    "Here is how I plan my whole week in five minutes every Sunday night."
  ],
  "voice": "en-US-AvaMultilingualNeural",
  "speed": "+25%",
  "generateSubtitles": true,
  "subtitleGranularity": "word",
  "subtitleFormat": "srt"
};
const run = await client.actor('fayoussef/bulk-text-to-speech').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~bulk-text-to-speech/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Three things nobody tells you before you start a side business. Number one: your first customer is probably someone you already know.", "Stop scrolling. This is the only productivity tip that actually worked for me, and it takes ten seconds.", "Here is how I plan my whole week in five minutes every Sunday night."], "voice": "en-US-AvaMultilingualNeural", "speed": "+25%", "generateSubtitles": true, "subtitleGranularity": "word", "subtitleFormat": "srt"}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/bulk-text-to-speech
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Bulk Text to Speech MP3 + SRT Subtitles (No API Key) free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-text-to-speech?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/bulk-text-to-speech` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Bulk AI Tools

- [Bulk AI Image Generator (NO API KEY)](bulk-ai-image-generator.md): Generate hundreds of AI images in one run from a list of prompts using top OpenRouter models (Gemini, GPT Image, Seedream, Flux...).
- [Bulk LLM Runner GPT, Claude, Perplexity, Kimi (No API Key)](bulk-llm-runner.md): Run hundreds of prompts in parallel across GPT, Claude, Gemini and Perplexity Sonar - plus 400+ other LLMs - without API key. Built-in web...
- [Bulk AI Translator: Website, Files & Datasets (No API Key)](bulk-ai-translator.md): Translate product catalogs, websites, datasets, CSV/XLSX/JSON files and SRT/VTT subtitles into 40+ languages. AI translation with...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/bulk-text-to-speech](https://automationbyexperts.com/apify/bulk-text-to-speech?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/bulk-text-to-speech.md](https://automationbyexperts.com/apify/bulk-text-to-speech.md)
