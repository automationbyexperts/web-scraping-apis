# XE.gr Greek Property Scraper

**XE.gr Greek Property Scraper** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape Greek real estate listings from XE.gr: prices, size, rooms, GPS coordinates, amenities, photos and advertiser phone numbers. Works in every language XE.gr publishes: Greek, English, German, French and Spanish, both for the URLs you paste in and for the data you get back.

[Run it on Apify](https://apify.com/fayoussef/xe-gr-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/xe-gr-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Real Estate Scrapers](../categories/real-estate-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Real Estate Scrapers](../categories/real-estate-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/xe-gr-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-15 |

## What you can do with XE.gr Greek Property Scraper

- **[Find apartments for rent in Athens with phone numbers](https://apify.com/fayoussef/xe-gr-scraper/examples/athens-apartments-for-rent?fpr=youssef)**: Searches XE.gr for one bedroom or larger apartments to rent in Athens up to 900 EUR a month, newest first, and returns each listing with the contact phone number XE.gr hides behind its Show phone button, plus floor...
- **[Export homes for sale in Thessaloniki](https://apify.com/fayoussef/xe-gr-scraper/examples/thessaloniki-homes-for-sale?fpr=youssef)**: Pulls residential listings for sale in Thessaloniki between 60 square metres and 250,000 EUR from XE.gr, with price per square metre, construction year, floor, energy class, exact address and the advertiser's details...
- **[Track villas for sale on the Athens Riviera](https://apify.com/fayoussef/xe-gr-scraper/examples/athens-riviera-villas-for-sale?fpr=youssef)**: Watches XE.gr for villas listed for sale in Glyfada from 500,000 EUR upwards, in English, with full details and the owner or agency phone number. Schedule it and combine with Dataset Diff to be told the day a new villa...
- **[Φοιτητικά διαμερίσματα για ενοικίαση στην Πάτρα έως 500€](https://apify.com/fayoussef/xe-gr-scraper/examples/patras-student-apartments-for-rent-greek?fpr=youssef)**: Συλλέγει από το XE.gr διαμερίσματα προς ενοικίαση στην Πάτρα κατάλληλα για φοιτητές, με ενοίκιο έως 500€ και τις νεότερες αγγελίες πρώτα. Κάθε αγγελία έρχεται με το τηλέφωνο επικοινωνίας που το XE.gr κρύβει πίσω από το...
- **[Οικόπεδα προς πώληση στη Σιθωνία Χαλκιδικής](https://apify.com/fayoussef/xe-gr-scraper/examples/sithonia-halkidiki-land-for-sale-greek?fpr=youssef)**: Εξάγει από το XE.gr τα οικόπεδα και αγροτεμάχια προς πώληση στη Σιθωνία Χαλκιδικής, από το φθηνότερο προς το ακριβότερο, με τιμή, εμβαδόν, περιοχή, συντεταγμένες, περιγραφή, τηλέφωνο του αγγελιοδότη και φωτογραφίες, όλα...

## How to use XE.gr Greek Property Scraper

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "location": "Athens",
  "transactionType": "rent",
  "propertyCategory": "residence",
  "propertyType": "apartment",
  "minBedrooms": 1,
  "maxPrice": 900,
  "includePhone": true,
  "includeDetails": true,
  "sortBy": "publication_date_desc",
  "maxItems": 200
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'location': 'Athens',
 'transactionType': 'rent',
 'propertyCategory': 'residence',
 'propertyType': 'apartment',
 'minBedrooms': 1,
 'maxPrice': 900,
 'includePhone': True,
 'includeDetails': True,
 'sortBy': 'publication_date_desc',
 'maxItems': 200}
run = client.actor("fayoussef/xe-gr-scraper").call(run_input=run_input)

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
  "location": "Athens",
  "transactionType": "rent",
  "propertyCategory": "residence",
  "propertyType": "apartment",
  "minBedrooms": 1,
  "maxPrice": 900,
  "includePhone": true,
  "includeDetails": true,
  "sortBy": "publication_date_desc",
  "maxItems": 200
};
const run = await client.actor('fayoussef/xe-gr-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~xe-gr-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"location": "Athens", "transactionType": "rent", "propertyCategory": "residence", "propertyType": "apartment", "minBedrooms": 1, "maxPrice": 900, "includePhone": true, "includeDetails": true, "sortBy": "publication_date_desc", "maxItems": 200}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/xe-gr-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is XE.gr Greek Property Scraper free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/xe-gr-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/xe-gr-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Real Estate Scrapers

- [Spitogatos.gr Scraper: Greek Property Listings & Agent Phones](spitogatos-scraper.md): Scrape real estate listings and Agents from Spitogatos.gr in both English and Greek. Collect prices, photos, location, and more. Easy...
- [Centris.ca Scraper: Quebec Real Estate Listings & Photos](centris-property-scraper.md): Scrape Centris.ca real estate listings into clean structured data: MLS number, price, full address, rooms, bedrooms, bathrooms, the full...
- [Spitogatos Cyprus Scraper: Property Listings & Agent Phones](spitogatos-cy-scraper.md): Scrape property listings and estate agents from Spitogatos.com.cy in English or Greek. Paste any search, listing or agent URL, or search by...

## More

- Full catalog: [all 50 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/xe-gr-scraper](https://automationbyexperts.com/apify/xe-gr-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/xe-gr-scraper.md](https://automationbyexperts.com/apify/xe-gr-scraper.md)
