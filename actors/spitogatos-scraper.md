# Spitogatos.gr Scraper: Greek Property Listings & Agent Phones

**Spitogatos.gr Scraper: Greek Property Listings & Agent Phones** is a ready-to-run Apify actor from AutomationByExperts by Youssef Farhan. Scrape real estate listings and Agents from Spitogatos.gr in both English and Greek. Collect prices, photos, location, and more. Easy setup, fast results, ready for Excel, JSON, or API integration

[Run it on Apify](https://apify.com/fayoussef/spitogatos-scraper?fpr=youssef) | [Actor page on AutomationByExperts](https://automationbyexperts.com/apify/spitogatos-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All Real Estate Scrapers](../categories/real-estate-scrapers.md)

## Key facts

| | |
|---|---|
| Category | [Real Estate Scrapers](../categories/real-estate-scrapers.md) |
| Runs on | Apify cloud, nothing to install and no server to manage |
| Output | JSON, CSV, Excel, XML, HTML, API, webhooks |
| Pricing model | Pay per result or event (the current rate is shown on the [Store page](https://apify.com/fayoussef/spitogatos-scraper?fpr=youssef)) |
| Rating | 5.0 out of 5 (5 reviews) |
| Maintainer | [Youssef Farhan, AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) |
| Catalog updated | 2026-10-05 |

## What you can do with Spitogatos.gr Scraper: Greek Property Listings & Agent Phones

- **[Find apartments for sale in Kolonaki, Athens](https://apify.com/fayoussef/spitogatos-scraper/examples/kolonaki-apartments-for-sale?fpr=youssef)**: Searches Spitogatos.gr for apartments for sale in Kolonaki up to 300,000 EUR and returns 25 plus fields per property: price, price per square metre, floor, year, energy class, GPS coordinates, owner or agent phone...
- **[Find apartments for rent in Thessaloniki under 600 EUR](https://apify.com/fayoussef/spitogatos-scraper/examples/thessaloniki-apartments-for-rent-under-600?fpr=youssef)**: Pulls every apartment for rent in Thessaloniki at 600 EUR a month or less from Spitogatos.gr, with floor area, floor, heating, furnished flag, the landlord or agency phone number and the listing's coordinates. Students...
- **[Export land plots for sale in Chania, Crete](https://apify.com/fayoussef/spitogatos-scraper/examples/crete-land-plots-for-sale?fpr=youssef)**: Lists plots of land for sale around Chania on Spitogatos.gr with price, area, price per square metre, coordinates and the seller's phone number. Developers and buyers hunting for buildable land in Crete use it to map...
- **[Διαμερίσματα για ενοικίαση στο κέντρο της Αθήνας έως 800€](https://apify.com/fayoussef/spitogatos-scraper/examples/athens-center-apartments-for-rent-greek?fpr=youssef)**: Συλλέγει από το Spitogatos.gr αγγελίες διαμερισμάτων προς ενοικίαση στο κέντρο της Αθήνας με ενοίκιο έως 800€ και επιστρέφει πάνω από 25 πεδία ανά ακίνητο: τιμή, τετραγωνικά, όροφο, έτος κατασκευής, ενεργειακή κλάση...
- **[Κατοικίες προς πώληση στη Θεσσαλονίκη από το Spitogatos](https://apify.com/fayoussef/spitogatos-scraper/examples/thessaloniki-homes-for-sale-greek?fpr=youssef)**: Συλλέγει τις αγγελίες κατοικιών προς πώληση στη Θεσσαλονίκη από το Spitogatos.gr (διαμερίσματα, μονοκατοικίες, μεζονέτες) με τιμή, τετραγωνικά, όροφο, έτος κατασκευής, ενεργειακή κλάση, συντεταγμένες GPS, τηλέφωνο...

## How to use Spitogatos.gr Scraper: Greek Property Listings & Agent Phones

### No code

1. Open the actor on Apify and sign in, or create a free Apify account.
2. Fill in the input form, or paste the example input below, and click **Start**.
3. Download the results as JSON, CSV, Excel, XML or HTML, or send them to Make, Zapier, n8n or a webhook.

### Example input

```json
{
  "locations": [
    "Kolonaki"
  ],
  "listing_type": "sale",
  "category": "residential",
  "property_types": "apartment",
  "price_max": 300000,
  "max_depth": 10
}
```

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run_input = {'locations': ['Kolonaki'],
 'listing_type': 'sale',
 'category': 'residential',
 'property_types': 'apartment',
 'price_max': 300000,
 'max_depth': 10}
run = client.actor("fayoussef/spitogatos-scraper").call(run_input=run_input)

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
  "locations": [
    "Kolonaki"
  ],
  "listing_type": "sale",
  "category": "residential",
  "property_types": "apartment",
  "price_max": 300000,
  "max_depth": 10
};
const run = await client.actor('fayoussef/spitogatos-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (run and get the results in one call)

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~spitogatos-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"locations": ["Kolonaki"], "listing_type": "sale", "category": "residential", "property_types": "apartment", "price_max": 300000, "max_depth": 10}'
```

### From AI agents (MCP)

Add the Apify MCP server to Claude, ChatGPT, Cursor or any MCP client with this URL, and the agent can run the actor for you:

```text
https://mcp.apify.com?tools=fayoussef/spitogatos-scraper
```

Your Apify API token is under **Settings > API & Integrations** in the [Apify Console](https://console.apify.com/settings/integrations?fpr=youssef).

## FAQ

### Is Spitogatos.gr Scraper: Greek Property Listings & Agent Phones free to try?

Yes. You can start it with a free Apify account. Free runs have usage limits, and larger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). The current rate is shown on the [Store page](https://apify.com/fayoussef/spitogatos-scraper?fpr=youssef).

### Do I need to know how to code?

No. The actor runs from a form in the Apify Console. Code is only needed if you want to call it from your own app, and the snippets above cover Python, JavaScript and cURL.

### What formats can I export the data in?

JSON, CSV, Excel, XML and HTML from the Console, or directly through the Apify API. Runs can also be scheduled and pushed to Make, Zapier, n8n or any webhook.

### Can AI agents use it?

Yes. Connect the Apify MCP server with `https://mcp.apify.com?tools=fayoussef/spitogatos-scraper` and Claude, ChatGPT, Cursor or any MCP client can run it and read the results.

### Can I get a custom version?

Yes. Youssef Farhan builds custom scrapers and automations. Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).

## Related Real Estate Scrapers

- [Centris.ca Scraper: Quebec Real Estate Listings & Photos](centris-property-scraper.md): Scrape Centris.ca real estate listings into clean structured data: MLS number, price, full address, rooms, bedrooms, bathrooms, the full...
- [XE.gr Greek Property Scraper](xe-gr-scraper.md): Scrape Greek real estate listings from XE.gr: prices, size, rooms, GPS coordinates, amenities, photos and advertiser phone numbers. Works...
- [RentFaster Scraper: Canada Rentals, Rents & Landlord Phones](rentfaster-scraper.md): Scrape Canadian rental listings from RentFaster.ca in 105 cities (Calgary, Edmonton, Toronto, Montreal...). Filter by type, bedrooms, rent...
- [Cyprus Property Scraper: Spitogatos.com.cy Listings & Agents](spitogatos-cy-scraper.md): Scrape Cyprus real estate listings and estate agents from Spitogatos.com.cy, in English or Greek. Search by town, price and property type...

## More

- Full catalog: [all 56 actors](../README.md)
- Website page: [https://automationbyexperts.com/apify/spitogatos-scraper](https://automationbyexperts.com/apify/spitogatos-scraper?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Markdown version for AI tools: [https://automationbyexperts.com/apify/spitogatos-scraper.md](https://automationbyexperts.com/apify/spitogatos-scraper.md)
