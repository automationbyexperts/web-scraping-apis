# Spitogatos Cyprus Scraper: Property Listings & Agent Phones

**Spitogatos Cyprus Scraper: Property Listings & Agent Phones** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape property listings and estate agents from Spitogatos.com.cy in English or Greek. Paste any search, listing or agent URL, or search by town, price and property type, and get price, area, rooms, GPS, photos and the agency phone across Limassol, Nicosia, Larnaca, Paphos and Famagusta.

[Run it on Apify](https://apify.com/fayoussef/spitogatos-cy-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/spitogatos-cy-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Real Estate Scrapers](../categories/real-estate-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Real Estate Scrapers](../categories/real-estate-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/spitogatos-cy-scraper?fpr=youssef)) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-09-28 |

## What you can do with Spitogatos Cyprus Scraper: Property Listings & Agent Phones

- **[Find apartments for rent in Limassol, Cyprus under 1500 EUR](https://apify.com/fayoussef/spitogatos-cy-scraper/examples/limassol-apartments-for-rent-under-1500?fpr=youssef)**: Collects apartment rentals in Limassol, Cyprus from Spitogatos.com.cy with a monthly rent up to 1500 EUR. Each listing comes with rent, area, rooms, floor, energy class, GPS coordinates, photos, the full description and...
- **[Export homes for sale in Paphos, Cyprus with agent phones](https://apify.com/fayoussef/spitogatos-cy-scraper/examples/paphos-homes-for-sale-cyprus?fpr=youssef)**: Scrapes every home for sale in Paphos listed on Spitogatos.com.cy, page by page: villas, houses and apartments with asking price, price per m2, area, bedrooms, year built, GPS coordinates, photo gallery and a direct...
- **[Ενοικιάσεις κατοικιών στη Λευκωσία από το Spitogatos Κύπρου](https://apify.com/fayoussef/spitogatos-cy-scraper/examples/nicosia-homes-for-rent-greek?fpr=youssef)**: Συλλέγει από το Spitogatos.com.cy όλες τις αγγελίες κατοικιών προς ενοικίαση στη Λευκωσία, με τα στοιχεία στα ελληνικά: ενοίκιο, τετραγωνικά, δωμάτια, όροφο, ενεργειακή κλάση, συντεταγμένες GPS, φωτογραφίες, περιγραφή...
- **[Μεσιτικά γραφεία στη Λεμεσό με τηλέφωνα επικοινωνίας](https://apify.com/fayoussef/spitogatos-cy-scraper/examples/limassol-estate-agents-greek?fpr=youssef)**: Εξάγει από το Spitogatos.com.cy όλα τα μεσιτικά γραφεία της Λεμεσού: επωνυμία, τηλέφωνα, υπεύθυνο επικοινωνίας, περιοχή, ιστοσελίδα, πλήθος αγγελιών προς πώληση και ενοικίαση και μέση τιμή πώλησης κατοικιών. Χρήσιμο για...

## How to use Spitogatos Cyprus Scraper: Property Listings & Agent Phones

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "start_urls": [],
  "locations": [
    "Limassol"
  ],
  "language": "en",
  "listing_type": "rent",
  "category": "residential",
  "property_types": "apartment",
  "price_max": 1500
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'start_urls': [],
 'locations': ['Limassol'],
 'language': 'en',
 'listing_type': 'rent',
 'category': 'residential',
 'property_types': 'apartment',
 'price_max': 1500}
run = client.actor("fayoussef/spitogatos-cy-scraper").call(run_input=run_input)

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
  "start_urls": [],
  "locations": [
    "Limassol"
  ],
  "language": "en",
  "listing_type": "rent",
  "category": "residential",
  "property_types": "apartment",
  "price_max": 1500
};
const run = await client.actor('fayoussef/spitogatos-cy-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~spitogatos-cy-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"start_urls": [], "locations": ["Limassol"], "language": "en", "listing_type": "rent", "category": "residential", "property_types": "apartment", "price_max": 1500}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/spitogatos-cy-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Spitogatos Cyprus Scraper: Property Listings & Agent Phones free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/spitogatos-cy-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/spitogatos-cy-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Real Estate Scrapers

- [Spitogatos.gr Scraper: Greek Property Listings & Agent Phones](spitogatos-scraper.md): Scrape real estate listings and Agents from Spitogatos.gr in both English and Greek. Collect prices, photos, location, and more. Easy...
- [Centris.ca Scraper: Quebec Real Estate Listings & Photos](centris-property-scraper.md): Scrape Centris.ca real estate listings into clean structured data: MLS number, price, full address, rooms, bedrooms, bathrooms, the full...
- [XE.gr Greek Property Scraper](xe-gr-scraper.md): Scrape Greek real estate listings from XE.gr: prices, size, rooms, GPS coordinates, amenities, photos and advertiser phone numbers. Works...

## More

- Full catalog: [all 54 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/spitogatos-cy-scraper](https://automationbyexperts.com/apify/spitogatos-cy-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/spitogatos-cy-scraper.md](https://automationbyexperts.com/apify/spitogatos-cy-scraper.md)
