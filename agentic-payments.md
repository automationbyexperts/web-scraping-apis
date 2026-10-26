# Web Scraping APIs for AI Agents: Pay per Run with x402 (USDC) or Skyfire, No Account

> 54 ready-to-run scrapers by AutomationByExperts that an AI agent can discover, run and pay for on its own: no Apify account, no API key sign-up, no subscription. The agent pays per run with USDC on Base through the x402 protocol, or with a Skyfire PAY token, and gets structured JSON back in the same HTTP call.

**54 agent-payable actors** | Updated 2026-10-26 | [Full catalog](README.md) | [llms.txt](llms.txt)

## How it works

1. The agent calls the Apify API for an actor below without a token. Apify answers HTTP `402 Payment Required`.
2. The agent pays: an x402 payment in USDC buys a prepaid Apify token, or the agent creates a Skyfire PAY token.
3. The agent repeats the call with that token. The actor runs in the Apify cloud and the results come back as JSON.
4. Apify charges the run's events (for example, per result) to the token. Unused balance stays on it.

Agentic payments are an experimental Apify feature. Official docs: [x402](https://docs.apify.com/integrations/x402) and [Skyfire](https://docs.apify.com/integrations/skyfire).

## Option 1: x402 (USDC on Base)

Needs USDC and a tiny amount of ETH (for gas) on Base, in a wallet such as the Coinbase Agentic Wallet (`awal`).

```bash
# 1. Log in to the wallet (a code is emailed to you)
npx -y awal auth login <email>
npx awal auth verify <code>

# 2. Fund the wallet address with USDC and a little ETH on Base
npx awal address

# 3. Buy a prepaid Apify token with x402 (amount in USD)
npx awal x402 pay 'https://agi.apify.com/protocols/x402/prepaid-tokens?amount=1&currency=usd' --max-amount 1000000 --json

# 4. Run an actor and get its results in one call
curl -X POST "https://api.apify.com/v2/acts/fayoussef~<actor-name>/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'

# Remaining balance
curl -s "https://agi.apify.com/prepaid-tokens/balance" -H "Authorization: Bearer $TOKEN"
```

There is a ready-made [Apify x402 skill](https://raw.githubusercontent.com/apify/awesome-skills/refs/heads/main/skills/apify-x402-agentic-wallet/SKILL.md) that walks an agent through the same steps.

## Option 2: Skyfire

Create a funded [Skyfire](https://skyfire.xyz/) account, then connect two MCP servers to your agent (Claude, OpenCode or any MCP client):

```text
Skyfire MCP:  https://mcp.skyfire.xyz/mcp      (header  skyfire-api-key: <your key>)
Apify MCP:    https://mcp.apify.com?payment=skyfire&tools=fayoussef/<actor-name>
```

The agent creates the PAY token, runs the actor and reads the results by itself. Without MCP, send the token as a header:

```bash
curl -X POST "https://api.apify.com/v2/acts/fayoussef~<actor-name>/run-sync-get-dataset-items" \
  -H "skyfire-pay-id: $SKYFIRE_PAY_TOKEN" -H "Content-Type: application/json" -d '{}'
```

## Actors an agent can pay for

Replace `<actor-name>` above with the name in the second column. Each guide has a ready-to-paste example input.

### Car & Vehicle Scrapers

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [AutoTrader.ca Scraper: Car Prices, VIN, Mileage & Dealers](https://apify.com/fayoussef/autotrader-canada?fpr=youssef) | `autotrader-canada` | Scrape AutoTrader.ca car listings: price, mileage, VIN, specs, dealer phone and photos from any search or the filter form. Optional Find... | [Guide](actors/autotrader-canada.md) |
| [CarGurus Scraper: US, Canada & UK Car Listings, VIN & Prices](https://apify.com/fayoussef/cargurus-listings-scraper?fpr=youssef) | `cargurus-listings-scraper` | Scrape CarGurus car listings from cargurus.com, .ca and .co.uk by search URL or ZIP code: price, deal rating, mileage, VIN, specs, dealer... | [Guide](actors/cargurus-listings-scraper.md) |
| [AutoTrader.ca Price Drop Monitor & Car Scraper](https://apify.com/fayoussef/autotrader-ca?fpr=youssef) | `autotrader-ca` | Monitor AutoTrader Canada searches and get only new listings, price drops and sold cars since the last run, with price history. Schedule it... | [Guide](actors/autotrader-ca.md) |
| [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](https://apify.com/fayoussef/kijiji-scraper?fpr=youssef) | `kijiji-scraper` | Scrape Kijiji.ca listings from any search or ad URL: cars, real estate and every other category. Get price, location, phone number, specs... | [Guide](actors/kijiji-scraper.md) |
| [AutoTrader South Africa Price Drop Monitor and Scraper](https://apify.com/fayoussef/autotrader-co-za-scraper?fpr=youssef) | `autotrader-co-za-scraper` | Track autotrader.co.za for new listings, price drops and sold cars, or scrape every listing with price, mileage, specs and dealer. Optional... | [Guide](actors/autotrader-co-za-scraper.md) |
| [AutoTrader Australia Scraper: Car Prices, Specs & Dealers](https://apify.com/fayoussef/autotrader-au-scraper?fpr=youssef) | `autotrader-au-scraper` | Scrape Autotrader Australia. Paste any autotrader.com.au search URL to export every vehicle: price, make, model, variant, year, odometer... | [Guide](actors/autotrader-au-scraper.md) |
| [Car Dealer Website Inventory Scraper: VIN, Price & Stock](https://apify.com/fayoussef/dealer-inventory-scraper?fpr=youssef) | `dealer-inventory-scraper` | Scrape live vehicle inventory from any car dealership's own website, not a marketplace. Paste a dealer homepage and get every car at VIN... | [Guide](actors/dealer-inventory-scraper.md) |
| [PistonHeads Scraper: UK Used, Classic & Performance Cars](https://apify.com/fayoussef/pistonheads?fpr=youssef) | `pistonheads` | Our pistonheads.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing card. | [Guide](actors/pistonheads.md) |
| [Canada Car Scraper: AutoTrader.ca, Kijiji, CarGurus & Carpages](https://apify.com/fayoussef/canada-car-scraper?fpr=youssef) | `canada-car-scraper` | Search AutoTrader.ca, Kijiji and CarGurus.ca at once, plus Carpages.ca if you choose, with one filter form. Duplicates are merged into one... | [Guide](actors/canada-car-scraper.md) |
| [Car Dealer Review Alerts: DealerRater Bad Review Monitor](https://apify.com/fayoussef/dealer-reputation-monitor?fpr=youssef) | `dealer-reputation-monitor` | Get alerted when a car dealership gets a new 1 or 2 star review or its rating drops. Watch dealers by name, URL or market on DealerRater... | [Guide](actors/dealer-reputation-monitor.md) |
| [coches.net Scraper: Spain Used Car Prices, Deals & Dealers](https://apify.com/fayoussef/coches-net-scraper?fpr=youssef) | `coches-net-scraper` | Scrape used cars from coches.net, Spain's largest car marketplace. Filter by make, model, price, year, km, province or radius, fuel, DGT... | [Guide](actors/coches-net-scraper.md) |
| [Canada VIN Decoder: Recalls & Market Value Report](https://apify.com/fayoussef/canada-vin-report?fpr=youssef) | `canada-vin-report` | Decode VINs in bulk and get US and Transport Canada recalls, NHTSA safety stars and complaints, plus the live Canadian market value from... | [Guide](actors/canada-vin-report.md) |
| [Clutch.ca Car Scraper: Used Car Prices, VIN & Carfax](https://apify.com/fayoussef/clutch-ca-scraper?fpr=youssef) | `clutch-ca-scraper` | Scrape used cars from Clutch.ca, Canada's online car retailer. Filter by make, model, price, biweekly or monthly payment, year, mileage... | [Guide](actors/clutch-ca-scraper.md) |

### Real Estate Scrapers

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Spitogatos Scraper: Greece Real Estate Listings & Agent Phones](https://apify.com/fayoussef/spitogatos-scraper?fpr=youssef) | `spitogatos-scraper` | Scrape Greece real estate listings from Spitogatos.gr, the country's largest property portal. Homes, land and commercial property for sale... | [Guide](actors/spitogatos-scraper.md) |
| [XE.gr Greek Property Scraper](https://apify.com/fayoussef/xe-gr-scraper?fpr=youssef) | `xe-gr-scraper` | Scrape Greek real estate listings from XE.gr: prices, size, rooms, GPS coordinates, amenities, photos and phone numbers. Owners-only mode... | [Guide](actors/xe-gr-scraper.md) |
| [Centris.ca Scraper: Quebec Real Estate Listings & Photos](https://apify.com/fayoussef/centris-property-scraper?fpr=youssef) | `centris-property-scraper` | Scrape Centris.ca real estate listings into clean structured data: MLS number, price, full address, rooms, bedrooms, bathrooms, the full... | [Guide](actors/centris-property-scraper.md) |
| [RentFaster Scraper: Canada Rentals, Rents & Landlord Phones](https://apify.com/fayoussef/rentfaster-scraper?fpr=youssef) | `rentfaster-scraper` | Scrape Canadian rental listings from RentFaster.ca in 105 cities (Calgary, Edmonton, Toronto, Montreal...). Filter by type, bedrooms, rent... | [Guide](actors/rentfaster-scraper.md) |
| [Cyprus Property Alerts: New Listings and Price Drops](https://apify.com/fayoussef/spitogatos-cy-scraper?fpr=youssef) | `spitogatos-cy-scraper` | Get alerted to new Cyprus property listings and price drops on Spitogatos.com.cy, with webhook or Telegram alerts. Also scrapes listings... | [Guide](actors/spitogatos-cy-scraper.md) |

### E-commerce & Marketplace Scrapers

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Wallapop Scraper: Deal Alerts, New Listings & Price Drops](https://apify.com/fayoussef/wallapop-scraper?fpr=youssef) | `wallapop-scraper` | Get alerted to new Wallapop listings and price drops, and spot the ones priced under the search median. Works for any search in Spain... | [Guide](actors/wallapop-scraper.md) |
| [G2G Price Monitor: Undercut & Price Drop Alerts](https://apify.com/fayoussef/g2g-offer-scraper?fpr=youssef) | `g2g-offer-scraper` | Monitor G2G.com prices and get alerted when a seller undercuts you, a price drops or a new offer appears. Also scrapes every offer, seller... | [Guide](actors/g2g-offer-scraper.md) |
| [Skroutz Scraper: Greek Price Comparison, Offers & History](https://apify.com/fayoussef/skroutz-scraper?fpr=youssef) | `skroutz-scraper` | Scrape Skroutz, Greece's largest price comparison site, plus Skroutz Cyprus, Bulgaria, Romania, Germany and Malta. Paste any category... | [Guide](actors/skroutz-scraper.md) |
| [Bike24 Scraper: Cycling Product Prices, Stock & Specs](https://apify.com/fayoussef/bike24-result-scraper?fpr=youssef) | `bike24-result-scraper` | Our bike24.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each product page | [Guide](actors/bike24-result-scraper.md) |
| [RONA Scraper: Canada Home Improvement Prices, Stock & Specs](https://apify.com/fayoussef/rona-scraper?fpr=youssef) | `rona-scraper` | Scrape RONA.ca products in English and French from any category, search or product URL. Export price, sale price, regular price, stock by... | [Guide](actors/rona-scraper.md) |
| [Smyths Toys Scraper: Prices, EAN Codes, Stock & Product Data](https://apify.com/fayoussef/smythstoys-scraper?fpr=youssef) | `smythstoys-scraper` | Scrape Smyths Toys UK and Ireland by category, search or product URL. Get prices, was prices, discounts, EAN barcodes, brand, ratings... | [Guide](actors/smythstoys-scraper.md) |
| [Bazaraki Scraper: Cyprus Property, Cars & Classifieds](https://apify.com/fayoussef/bazaraki-scraper?fpr=youssef) | `bazaraki-scraper` | Scrape Bazaraki.com, Cyprus's biggest classifieds site: property for sale and rent, cars, jobs and every other category. Filter by... | [Guide](actors/bazaraki-scraper.md) |

### Price & Brand Monitoring

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Competitor Price Tracker & Price Comparison by Product URL](https://apify.com/fayoussef/competitor-price-tracker-price-comparison-by-product-url?fpr=youssef) | `competitor-price-tracker-price-comparison-by-product-url` | Paste any product URL to get every retailer selling the same item, live prices, your market rank, and a suggested pricing action. Matches... | [Guide](actors/competitor-price-tracker-price-comparison-by-product-url.md) |
| [Brand Protection: Fake Shop, Counterfeit & Typosquat Finder](https://apify.com/fayoussef/brand-abuse-counterfeit-detector?fpr=youssef) | `brand-abuse-counterfeit-detector` | Find fake webshops, counterfeit marketplace listings, typosquatted domains and impersonation profiles abusing your brand. AI classifies... | [Guide](actors/brand-abuse-counterfeit-detector.md) |
| [Amazon Best Sellers Scraper: Rank Tracker, 21 Marketplaces](https://apify.com/fayoussef/amazon-bestsellers-tracker?fpr=youssef) | `amazon-bestsellers-tracker` | Track Amazon Best Sellers and New Releases ranks 1-100 in 21 marketplaces (US, UK, DE, FR, JP, IN, BR and more). Each run shows what moved... | [Guide](actors/amazon-bestsellers-tracker.md) |
| [MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers](https://apify.com/fayoussef/map-violation-monitor?fpr=youssef) | `map-violation-monitor` | Enter your products and MAP prices and get every public offer advertised below them on Amazon, eBay, Best Buy and Newegg. AI verifies each... | [Guide](actors/map-violation-monitor.md) |
| [Amazon, eBay, Best Buy & Newegg Price Checker by ASIN or UPC](https://apify.com/fayoussef/multi-marketplace-price-checker?fpr=youssef) | `multi-marketplace-price-checker` | Paste ASINs, UPCs, model numbers or product names and get what that exact product sells for on Amazon, eBay, Best Buy and Newegg. AI... | [Guide](actors/multi-marketplace-price-checker.md) |

### Lead Generation Actors

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Journalist Request Finder: HARO Alternative for Digital PR](https://apify.com/fayoussef/journalist-request-finder?fpr=youssef) | `journalist-request-finder` | Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon... | [Guide](actors/journalist-request-finder.md) |
| [Canada411 Scraper: Phone Numbers, Names & Addresses](https://apify.com/fayoussef/canada411-ca?fpr=youssef) | `canada411-ca` | Scrape Canada411.ca, Canada's phone directory: names, phone numbers and full addresses for businesses and people. Search by name or... | [Guide](actors/canada411-ca.md) |
| [GitHub Developer Lead Finder & Email Enricher](https://apify.com/fayoussef/github-developer-leads?fpr=youssef) | `github-developer-leads` | Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B... | [Guide](actors/github-developer-leads.md) |
| [Luma Events Scraper: New Event Alerts & Organizer Leads](https://apify.com/fayoussef/luma-events-scraper?fpr=youssef) | `luma-events-scraper` | Get alerted to new Luma (lu.ma) events in your city or calendar, with the organizer's Instagram, LinkedIn, TikTok, X and YouTube handles... | [Guide](actors/luma-events-scraper.md) |
| [Kijiji Dealer & Business Leads: Phones, Websites, Addresses](https://apify.com/fayoussef/kijiji-business-leads?fpr=youssef) | `kijiji-business-leads` | Turn any Kijiji.ca search into a B2B lead list: one row per dealer, property manager or local business, with phone, website, address... | [Guide](actors/kijiji-business-leads.md) |
| [Naukrigulf Jobs Scraper: UAE, Saudi & Gulf Jobs, 12 Languages](https://apify.com/fayoussef/naukrigulf-scraper?fpr=youssef) | `naukrigulf-scraper` | Scrape Naukrigulf jobs in Dubai, the UAE, Saudi Arabia, Qatar, Kuwait, Bahrain and Oman. Search in Arabic, Hindi, Malayalam, Tagalog and 8... | [Guide](actors/naukrigulf-scraper.md) |
| [Podcast Scraper for Guest Booking: Shows & Host Emails](https://apify.com/fayoussef/podcast-guest-finder?fpr=youssef) | `podcast-guest-finder` | Find podcasts that book guests, with the host's contact email. Search any niche across Apple Podcasts, keep active, guest-friendly shows... | [Guide](actors/podcast-guest-finder.md) |
| [Clinical Trials Scraper: ClinicalTrials.gov Data & Monitor](https://apify.com/fayoussef/clinical-trials-intelligence?fpr=youssef) | `clinical-trials-intelligence` | Scrape clinical trials from ClinicalTrials.gov via the official v2 API. Search 500,000+ studies by condition, sponsor, drug, phase, status... | [Guide](actors/clinical-trials-intelligence.md) |
| [11888.gr Scraper: Greek Business Phones, Emails & Websites](https://apify.com/fayoussef/11888-gr-scraper?fpr=youssef) | `11888-gr-scraper` | Scrape Greek businesses from the 11888.gr Yellow Pages by category and place: name, phones, mobile, email, website, address, GPS and... | [Guide](actors/11888-gr-scraper.md) |
| [AI Account Watch: Custom Sales Trigger Alerts](https://apify.com/fayoussef/ai-account-watch?fpr=youssef) | `ai-account-watch` | Watch a list of companies and get alerted when one does what you describe in plain English: raises funding, hires a CMO, opens a location... | [Guide](actors/ai-account-watch.md) |
| [New Business License Feed: Fresh Openings by City](https://apify.com/fayoussef/business-license-feed?fpr=youssef) | `business-license-feed` | Every business, food, liquor and trade license newly issued in Chicago, Los Angeles, New York, Seattle and New Orleans, filtered to the... | [Guide](actors/business-license-feed.md) |
| [Hiring Signal Alerts: New Jobs at Companies You Watch](https://apify.com/fayoussef/company-domain-to-job-postings?fpr=youssef) | `company-domain-to-job-postings` | Watch a list of company domains and get alerted when they post a new job matching your keywords. Finds each company's Greenhouse, Lever... | [Guide](actors/company-domain-to-job-postings.md) |
| [Reddit Scraper for Leads: Buying Intent Posts & Comments](https://apify.com/fayoussef/reddit-lead-finder?fpr=youssef) | `reddit-lead-finder` | Scrape Reddit posts and comments for buying intent: people asking for a tool, a recommendation, or an alternative to your competitor. Every... | [Guide](actors/reddit-lead-finder.md) |
| [Greek Business Leads: New Business Alerts from XO.gr](https://apify.com/fayoussef/xo-gr-scraper?fpr=youssef) | `xo-gr-scraper` | Get Greek business leads from xo.gr (Chrysos Odigos, the Greek Yellow Pages) by category and place, and get alerted when new businesses... | [Guide](actors/xo-gr-scraper.md) |

### Bulk AI Tools

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Bulk Text to Speech: MP3 + SRT Subtitles \| No API Key](https://apify.com/fayoussef/bulk-text-to-speech?fpr=youssef) | `bulk-text-to-speech` | Convert texts or an Excel/CSV file into MP3 voiceovers with perfectly timed SRT/VTT subtitles. 322 neural voices in 75 languages... | [Guide](actors/bulk-text-to-speech.md) |
| [Translate Excel, CSV & Websites in Bulk with AI \| No API Key](https://apify.com/fayoussef/bulk-ai-translator?fpr=youssef) | `bulk-ai-translator` | Translate Excel, CSV and Google Sheets files, whole websites, PDFs and SRT/VTT subtitles into 42 languages in one run, and get the same... | [Guide](actors/bulk-ai-translator.md) |

### SEO & AI Visibility

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [SEO, GEO & AEO Audit: AI Search Readiness Checker](https://apify.com/fayoussef/seo-geo-aeo-audit?fpr=youssef) | `seo-geo-aeo-audit` | Audit any website for Google SEO and AI search visibility in one run. Get 0-100 SEO, GEO and AEO scores per page, AI crawler and llms.txt... | [Guide](actors/seo-geo-aeo-audit.md) |
| [Google Maps Local Rank Tracker with Weekly Change Alerts](https://apify.com/fayoussef/geo-grid-local-rank-tracker?fpr=youssef) | `geo-grid-local-rank-tracker` | Track where a business ranks on Google Maps across a grid, week after week. Get alerted when your Share of Local Voice drops, see which... | [Guide](actors/geo-grid-local-rank-tracker.md) |
| [AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)](https://apify.com/fayoussef/ai-brand-visibility-tracker?fpr=youssef) | `ai-brand-visibility-tracker` | Is AI recommending you or your competitors? Track brand mentions, ranking position, sentiment, share of voice and cited sources in ChatGPT... | [Guide](actors/ai-brand-visibility-tracker.md) |
| [llms.txt Generator: llms-full.txt for Any Website (AI SEO)](https://apify.com/fayoussef/llms-txt-generator?fpr=youssef) | `llms-txt-generator` | Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every... | [Guide](actors/llms-txt-generator.md) |

### Developer Tools & APIs

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Dataset Diff & Change Monitor: Only New Items From Any Actor](https://apify.com/fayoussef/dataset-diff?fpr=youssef) | `dataset-diff` | Turn any Apify Actor, Task or dataset into a change monitor: get only the new, changed and removed items since the last run, deduplicated... | [Guide](actors/dataset-diff.md) |
| [VIES VAT Number Validator: Bulk EU VAT Check & Monitor](https://apify.com/fayoussef/eu-vat-compliance-monitor?fpr=youssef) | `eu-vat-compliance-monitor` | Bulk EU VAT number validation against VIES. Check a whole supplier or customer list, get the consultation number that proves you checked... | [Guide](actors/eu-vat-compliance-monitor.md) |
| [License Lookup & Verification: Bulk Contractor, Nurse, NPI](https://apify.com/fayoussef/license-roster-monitor?fpr=youssef) | `license-roster-monitor` | Bulk professional license lookup and verification for contractors, nurses, electricians, real estate agents and healthcare providers (NPI)... | [Guide](actors/license-roster-monitor.md) |
| [Website Change Monitor and Competitor Price Tracker](https://apify.com/fayoussef/website-change-monitor?fpr=youssef) | `website-change-monitor` | Monitor any web page for changes with a line-by-line diff, and track competitor prices: old price, new price and percent change for any... | [Guide](actors/website-change-monitor.md) |

## FAQ

### What are agentic payments on Apify?

A way for an AI agent to discover, run and pay for an Apify actor on its own, with no Apify account and no human sign-up. The agent pays per run with USDC on the Base blockchain through the open x402 protocol, or with a Skyfire PAY token.

### Which of these actors support it?

Every actor in the tables on this page. Apify flags them automatically: they are priced per event only, run with limited permissions and do not use Standby mode. The list is rebuilt weekly from the live Apify Store.

### What does a run cost?

The same per-event rate a normal Apify user pays, drawn from the prepaid x402 token or the Skyfire PAY token. The current rate is shown on each actor's Store page. You only pay for the events a run actually produces.

### Is there a minimum?

An x402 prepaid token is bought in one payment of at least 1 USDC and is valid for 14 days. A Skyfire PAY token needs at least 5 USD on it, and anything a run does not use stays on the token. Both are set by Apify and the payment provider, see the official docs for current terms.

### What does not work with agentic payments?

Schedules, webhooks and other integrations, and Standby runs. Start the actor through the API, then read the run and its dataset with the same token.

### I have an Apify account. Should I use this?

No need. A normal Apify API token is simpler and works with every actor in this catalog. Agentic payments are for agents that cannot sign up. A free account is at [apify.com](https://apify.com/?fpr=youssef).

## More

- Website version: [https://automationbyexperts.com/ai-agents](https://automationbyexperts.com/ai-agents?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Need a scraper for a site that is not listed? Email youssefarhan24@gmail.com or visit [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis).
