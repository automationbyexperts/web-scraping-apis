# Bulk AI Image Generator & Photo Editor: Nano Banana Pro

**Bulk AI Image Generator & Photo Editor: Nano Banana Pro** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Generate hundreds of AI images from prompts or an Excel/CSV file, or edit your own product photos in bulk: white or transparent background with no AI, or lifestyle scenes with the product kept pixel-exact. Nano Banana Pro, Nano Banana 2 and Nano Banana 2 Lite. No API key needed.

[Run it on Apify](https://apify.com/fayoussef/bulk-ai-image-generator?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/bulk-ai-image-generator?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Bulk AI Tools](../categories/ai-bulk-tools.md)

## Key facts

| | |
|---|---|
| Category | [Bulk AI Tools](../categories/ai-bulk-tools.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-ai-image-generator?fpr=youssef)) |
| Rating | 5.0 out of 5 (1 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-11-22 |

## What you can do with Bulk AI Image Generator & Photo Editor: Nano Banana Pro

- **[Create social media ad creatives in bulk](https://apify.com/fayoussef/bulk-ai-image-generator/examples/social-media-ad-creatives?fpr=youssef)**: Produces vertical ad creatives sized for Instagram Stories, Reels and TikTok. Each prompt returns three variants, so you get a set to A/B test instead of a single guess. Useful when one campaign needs a dozen visual...
- **[Generate product photos from an Excel or CSV catalog](https://apify.com/fayoussef/bulk-ai-image-generator/examples/product-photos-from-excel-catalog?fpr=youssef)**: Upload a spreadsheet of products (name, color, material, SKU) and get one studio product photo per row, made with Nano Banana. One prompt template with {{Column}} placeholders is filled in from every row, and you get...
- **[Flat lay to on-model photos for a clothing store](https://apify.com/fayoussef/bulk-ai-image-generator/examples/flat-lay-to-model-photos-for-clothing-store?fpr=youssef)**: Turns flat lay or ghost mannequin garment photos into front-facing photos of a realistic model wearing each piece, in bulk. Paste the links to your garment photos, keep the prompt or edit it, and get one on-model image...

## How to use Bulk AI Image Generator & Photo Editor: Nano Banana Pro

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "prompts": [
    "Vertical lifestyle ad creative for a fitness app: a runner at sunrise on an empty city bridge, warm light, bold empty space at the top for a headline",
    "Vertical lifestyle ad creative for a meal kit service: overhead shot of fresh ingredients on a wooden board, bright and clean, empty space at the bottom",
    "Vertical lifestyle ad creative for a travel booking app: a traveller looking out over a coastal town at golden hour, cinematic, space at the top for text",
    "Vertical lifestyle ad creative for a skincare brand: soft focus close up of a serum bottle on a marble surface with morning light, pastel tones"
  ],
  "model": "google/gemini-2.5-flash-image",
  "aspectRatio": "9:16",
  "imageSize": "2K",
  "imagesPerPrompt": 3,
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
run_input = {'prompts': ['Vertical lifestyle ad creative for a fitness app: a runner at sunrise on '
             'an empty city bridge, warm light, bold empty space at the top for a '
             'headline',
             'Vertical lifestyle ad creative for a meal kit service: overhead shot of '
             'fresh ingredients on a wooden board, bright and clean, empty space at '
             'the bottom',
             'Vertical lifestyle ad creative for a travel booking app: a traveller '
             'looking out over a coastal town at golden hour, cinematic, space at the '
             'top for text',
             'Vertical lifestyle ad creative for a skincare brand: soft focus close up '
             'of a serum bottle on a marble surface with morning light, pastel tones'],
 'model': 'google/gemini-2.5-flash-image',
 'aspectRatio': '9:16',
 'imageSize': '2K',
 'imagesPerPrompt': 3,
 'concurrency': 4}
run = client.actor("fayoussef/bulk-ai-image-generator").call(run_input=run_input)

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
    "Vertical lifestyle ad creative for a fitness app: a runner at sunrise on an empty city bridge, warm light, bold empty space at the top for a headline",
    "Vertical lifestyle ad creative for a meal kit service: overhead shot of fresh ingredients on a wooden board, bright and clean, empty space at the bottom",
    "Vertical lifestyle ad creative for a travel booking app: a traveller looking out over a coastal town at golden hour, cinematic, space at the top for text",
    "Vertical lifestyle ad creative for a skincare brand: soft focus close up of a serum bottle on a marble surface with morning light, pastel tones"
  ],
  "model": "google/gemini-2.5-flash-image",
  "aspectRatio": "9:16",
  "imageSize": "2K",
  "imagesPerPrompt": 3,
  "concurrency": 4
};
const run = await client.actor('fayoussef/bulk-ai-image-generator').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~bulk-ai-image-generator/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["Vertical lifestyle ad creative for a fitness app: a runner at sunrise on an empty city bridge, warm light, bold empty space at the top for a headline", "Vertical lifestyle ad creative for a meal kit service: overhead shot of fresh ingredients on a wooden board, bright and clean, empty space at the bottom", "Vertical lifestyle ad creative for a travel booking app: a traveller looking out over a coastal town at golden hour, cinematic, space at the top for text", "Vertical lifestyle ad creative for a skincare brand: soft focus close up of a serum bottle on a marble surface with morning light, pastel tones"], "model": "google/gemini-2.5-flash-image", "aspectRatio": "9:16", "imageSize": "2K", "imagesPerPrompt": 3, "concurrency": 4}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/bulk-ai-image-generator
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Bulk AI Image Generator & Photo Editor: Nano Banana Pro free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/bulk-ai-image-generator?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/bulk-ai-image-generator` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Bulk AI Tools

- [350+ AI Models: Run ChatGPT, Claude, Gemini in Bulk](bulk-llm-runner.md): Run hundreds of prompts in parallel across GPT, Claude, Gemini, Perplexity, DeepSeek, Qwen, Kimi and 350+ models, with web search, JSON...
- [Bulk Text to Speech: MP3 + SRT Subtitles | No API Key](bulk-text-to-speech.md): Convert texts or an Excel/CSV file into MP3 voiceovers with perfectly timed SRT/VTT subtitles. 322 neural voices in 75 languages...
- [Translate Excel, CSV & Websites in Bulk with AI | No API Key](bulk-ai-translator.md): Translate Excel, CSV and Google Sheets files, whole websites, PDFs and SRT/VTT subtitles into 42 languages in one run, and get the same...

## More

- Full catalog: [all 66 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/bulk-ai-image-generator](https://automationbyexperts.com/apify/bulk-ai-image-generator?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/bulk-ai-image-generator.md](https://automationbyexperts.com/apify/bulk-ai-image-generator.md)
