# Web Scraping APIs for AI Agents: Pay per Run with x402 (USDC) or Skyfire, No Account

> 41 ready-to-run scrapers by AutomationByExperts that an AI agent can discover, run and pay for on its own: no Apify account, no API key sign-up, no subscription. The agent pays per run with USDC on Base through the x402 protocol, or with a Skyfire PAY token, and gets structured JSON back in the same HTTP call.

**41 agent-payable actors** | Updated 2026-10-08 | [Full catalog](README.md) | [llms.txt](llms.txt)

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
| [AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers](https://apify.com/fayoussef/autotrader-canada?fpr=youssef) | `autotrader-canada` | Scrape AutoTrader.ca car listings: price, mileage, VIN, specs, dealer phone and photos from any search or the filter form. Optional Find... | [Guide](actors/autotrader-canada.md) |
| [AutoTrader.ca Price Drop Monitor & Car Scraper](https://apify.com/fayoussef/autotrader-ca?fpr=youssef) | `autotrader-ca` | Monitor AutoTrader Canada searches and get only new listings, price drops and sold cars since the last run, with price history. Schedule it... | [Guide](actors/autotrader-ca.md) |
| [CarGurus Scraper (US, Canada & UK Car Listings)](https://apify.com/fayoussef/cargurus-listings-scraper?fpr=youssef) | `cargurus-listings-scraper` | Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing. | [Guide](actors/cargurus-listings-scraper.md) |
| [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](https://apify.com/fayoussef/kijiji-scraper?fpr=youssef) | `kijiji-scraper` | Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location... | [Guide](actors/kijiji-scraper.md) |
| [autotrader.co.za Car Scraper with Seller Phone Numbers](https://apify.com/fayoussef/autotrader-co-za-scraper?fpr=youssef) | `autotrader-co-za-scraper` | Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number. | [Guide](actors/autotrader-co-za-scraper.md) |
| [AutoTrader Australia Car Scraper: Prices, VIN & Dealers](https://apify.com/fayoussef/autotrader-au-scraper?fpr=youssef) | `autotrader-au-scraper` | Scrape Autotrader Australia. Paste any autotrader.com.au search URL to export every vehicle: price, make, model, variant, year, odometer... | [Guide](actors/autotrader-au-scraper.md) |
| [Car Dealer Website Inventory Scraper: VIN, Price & Stock](https://apify.com/fayoussef/dealer-inventory-scraper?fpr=youssef) | `dealer-inventory-scraper` | Scrape live vehicle inventory from any car dealership's own website, not a marketplace. Paste a dealer homepage and get every car at VIN... | [Guide](actors/dealer-inventory-scraper.md) |
| [PistonHeads Scraper: UK Used, Classic & Performance Cars](https://apify.com/fayoussef/pistonheads?fpr=youssef) | `pistonheads` | Our pistonheads.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing card. | [Guide](actors/pistonheads.md) |
| [Clutch.ca Car Scraper: Used Car Prices, VIN & Carfax](https://apify.com/fayoussef/clutch-ca-scraper?fpr=youssef) | `clutch-ca-scraper` | Scrape used cars from Clutch.ca, Canada's online car retailer. Filter by make, model, price, biweekly or monthly payment, year, mileage... | [Guide](actors/clutch-ca-scraper.md) |
| [coches.net Scraper: Spain Used Car Prices, Deals & Dealers](https://apify.com/fayoussef/coches-net-scraper?fpr=youssef) | `coches-net-scraper` | Scrape used cars from coches.net, Spain's largest car marketplace. Filter by make, model, price, year, km, province or radius, fuel, DGT... | [Guide](actors/coches-net-scraper.md) |
| [Car Dealer Reviews & Reputation Monitor (DealerRater)](https://apify.com/fayoussef/dealer-reputation-monitor?fpr=youssef) | `dealer-reputation-monitor` | Pull every DealerRater review for any car dealership by name or URL. Get the star rating broken down by price transparency, trade-in... | [Guide](actors/dealer-reputation-monitor.md) |

### Real Estate Scrapers

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Spitogatos Real Estate Scraper: Greece Listings & Agent Phones](https://apify.com/fayoussef/spitogatos-scraper?fpr=youssef) | `spitogatos-scraper` | Scrape Greece real estate listings from Spitogatos.gr, the country's largest property portal. Homes, land and commercial property for sale... | [Guide](actors/spitogatos-scraper.md) |
| [XE.gr Greek Property Scraper](https://apify.com/fayoussef/xe-gr-scraper?fpr=youssef) | `xe-gr-scraper` | Scrape Greek real estate listings from XE.gr: prices, size, rooms, GPS coordinates, amenities, photos and advertiser phone numbers. Works... | [Guide](actors/xe-gr-scraper.md) |
| [Centris.ca Scraper: Quebec Real Estate Listings & Photos](https://apify.com/fayoussef/centris-property-scraper?fpr=youssef) | `centris-property-scraper` | Scrape Centris.ca real estate listings into clean structured data: MLS number, price, full address, rooms, bedrooms, bathrooms, the full... | [Guide](actors/centris-property-scraper.md) |
| [RentFaster Scraper: Canada Rentals, Rents & Landlord Phones](https://apify.com/fayoussef/rentfaster-scraper?fpr=youssef) | `rentfaster-scraper` | Scrape Canadian rental listings from RentFaster.ca in 105 cities (Calgary, Edmonton, Toronto, Montreal...). Filter by type, bedrooms, rent... | [Guide](actors/rentfaster-scraper.md) |
| [Cyprus Property Scraper: Spitogatos.com.cy Listings & Agents](https://apify.com/fayoussef/spitogatos-cy-scraper?fpr=youssef) | `spitogatos-cy-scraper` | Scrape Cyprus real estate listings and estate agents from Spitogatos.com.cy, in English or Greek. Search by town, price and property type... | [Guide](actors/spitogatos-cy-scraper.md) |

### E-commerce & Marketplace Scrapers

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [wallapop Scraper (Spain,Italy,Portugal)](https://apify.com/fayoussef/wallapop-scraper?fpr=youssef) | `wallapop-scraper` | Scrape Wallapop listings at scale across Spain, Italy, and Portugal without writing a single line of code. Paste any Wallapop search URL or... | [Guide](actors/wallapop-scraper.md) |
| [G2G Scraper: Extract G2G.com Prices, Sellers & Stock](https://apify.com/fayoussef/g2g-offer-scraper?fpr=youssef) | `g2g-offer-scraper` | Scrape live G2G.com prices, sellers, stock and delivery times from any category or Trending URL. Export JSON, CSV or Excel. No G2G login or... | [Guide](actors/g2g-offer-scraper.md) |
| [Bike24 Scraper: Cycling Product Prices, Stock & Specs](https://apify.com/fayoussef/bike24-result-scraper?fpr=youssef) | `bike24-result-scraper` | Our bike24.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each product page | [Guide](actors/bike24-result-scraper.md) |
| [Skroutz Scraper: Greek Price Comparison, Offers & History](https://apify.com/fayoussef/skroutz-scraper?fpr=youssef) | `skroutz-scraper` | Scrape Skroutz, Greece's largest price comparison site, plus Skroutz Cyprus, Bulgaria, Romania, Germany and Malta. Paste any category... | [Guide](actors/skroutz-scraper.md) |
| [RONA Scraper: Canada Home Improvement Prices, Stock & Specs](https://apify.com/fayoussef/rona-scraper?fpr=youssef) | `rona-scraper` | Scrape RONA.ca products in English and French from any category, search or product URL. Export price, sale price, regular price, stock by... | [Guide](actors/rona-scraper.md) |
| [Smyths Toys Scraper: Prices, EAN Codes, Stock & Product Data](https://apify.com/fayoussef/smythstoys-scraper?fpr=youssef) | `smythstoys-scraper` | Scrape Smyths Toys UK and Ireland by category, search or product URL. Get prices, was prices, discounts, EAN barcodes, brand, ratings... | [Guide](actors/smythstoys-scraper.md) |

### Price & Brand Monitoring

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Brand Protection: Fake Shop, Counterfeit & Typosquat Finder](https://apify.com/fayoussef/brand-abuse-counterfeit-detector?fpr=youssef) | `brand-abuse-counterfeit-detector` | Find fake webshops, counterfeit marketplace listings, typosquatted domains and impersonation profiles abusing your brand. AI classifies... | [Guide](actors/brand-abuse-counterfeit-detector.md) |

### Lead Generation Actors

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Canada411 Scraper: Business Phones, Addresses](https://apify.com/fayoussef/canada411-ca?fpr=youssef) | `canada411-ca` | Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing. | [Guide](actors/canada411-ca.md) |
| [Journalist Request Finder: HARO Alternative for Digital PR](https://apify.com/fayoussef/journalist-request-finder?fpr=youssef) | `journalist-request-finder` | Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon... | [Guide](actors/journalist-request-finder.md) |
| [GitHub Developer Lead Finder & Email Enricher](https://apify.com/fayoussef/github-developer-leads?fpr=youssef) | `github-developer-leads` | Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B... | [Guide](actors/github-developer-leads.md) |
| [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](https://apify.com/fayoussef/luma-events-scraper?fpr=youssef) | `luma-events-scraper` | Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest... | [Guide](actors/luma-events-scraper.md) |
| [11888.gr Scraper: Greek Business Phones, Emails & Websites](https://apify.com/fayoussef/11888-gr-scraper?fpr=youssef) | `11888-gr-scraper` | Scrape Greek businesses from the 11888.gr Yellow Pages by category and place: name, phones, mobile, email, website, address, GPS and... | [Guide](actors/11888-gr-scraper.md) |
| [New Business License Feed: Fresh Openings by City](https://apify.com/fayoussef/business-license-feed?fpr=youssef) | `business-license-feed` | Every business, food, liquor and trade license newly issued in Chicago, Los Angeles, New York, Seattle and New Orleans, filtered to the... | [Guide](actors/business-license-feed.md) |
| [Clinical Trials Scraper: ClinicalTrials.gov Data & Monitor](https://apify.com/fayoussef/clinical-trials-intelligence?fpr=youssef) | `clinical-trials-intelligence` | Scrape clinical trials from ClinicalTrials.gov via the official v2 API. Search 500,000+ studies by condition, sponsor, drug, phase, status... | [Guide](actors/clinical-trials-intelligence.md) |
| [XO.gr Scraper: Greek Business Directory, Phones & Emails](https://apify.com/fayoussef/xo-gr-scraper?fpr=youssef) | `xo-gr-scraper` | Scrape Greek business leads from xo.gr (Χρυσός Οδηγός, the Greek Yellow Pages) by category and place: name, phones, mobile, email, website... | [Guide](actors/xo-gr-scraper.md) |
| [Greenhouse & Lever Jobs Scraper: ATS Job Postings by Domain](https://apify.com/fayoussef/company-domain-to-job-postings?fpr=youssef) | `company-domain-to-job-postings` | Scrape Greenhouse, Lever, Ashby, Recruitee, SmartRecruiters and Personio jobs from just a company domain. Finds each company's ATS job... | [Guide](actors/company-domain-to-job-postings.md) |
| [Naukrigulf Jobs Scraper: UAE, Saudi & Gulf Jobs, 12 Languages](https://apify.com/fayoussef/naukrigulf-scraper?fpr=youssef) | `naukrigulf-scraper` | Scrape Naukrigulf jobs in Dubai, the UAE, Saudi Arabia, Qatar, Kuwait, Bahrain and Oman. Search in Arabic, Hindi, Malayalam, Tagalog and 8... | [Guide](actors/naukrigulf-scraper.md) |
| [Podcast Scraper for Guest Booking: Shows & Host Emails](https://apify.com/fayoussef/podcast-guest-finder?fpr=youssef) | `podcast-guest-finder` | Find podcasts that book guests, with the host's contact email. Search any niche across Apple Podcasts, keep active, guest-friendly shows... | [Guide](actors/podcast-guest-finder.md) |
| [Reddit Scraper for Leads: Buying Intent Posts & Comments](https://apify.com/fayoussef/reddit-lead-finder?fpr=youssef) | `reddit-lead-finder` | Scrape Reddit posts and comments for buying intent: people asking for a tool, a recommendation, or an alternative to your competitor. Every... | [Guide](actors/reddit-lead-finder.md) |

### SEO & AI Visibility

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Google Maps Geo-Grid Local Rank Tracker](https://apify.com/fayoussef/geo-grid-local-rank-tracker?fpr=youssef) | `geo-grid-local-rank-tracker` | Track where a business ranks in the Google Maps local pack across a grid of points around it. Per-point rank, average rank, coverage, Share... | [Guide](actors/geo-grid-local-rank-tracker.md) |
| [llms.txt Generator: llms-full.txt for Any Website (AI SEO)](https://apify.com/fayoussef/llms-txt-generator?fpr=youssef) | `llms-txt-generator` | Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every... | [Guide](actors/llms-txt-generator.md) |

### Developer Tools & APIs

| Actor | Actor name for the API | What it does | Guide |
|---|---|---|---|
| [Dataset Diff & Change Monitor: Only New Items From Any Actor](https://apify.com/fayoussef/dataset-diff?fpr=youssef) | `dataset-diff` | Turn any Apify Actor, Task or dataset into a change monitor: get only the new, changed and removed items since the last run, deduplicated... | [Guide](actors/dataset-diff.md) |
| [VIES VAT Number Validator: Bulk EU VAT Check & Monitor](https://apify.com/fayoussef/eu-vat-compliance-monitor?fpr=youssef) | `eu-vat-compliance-monitor` | Bulk EU VAT number validation against VIES. Check a whole supplier or customer list, get the consultation number that proves you checked... | [Guide](actors/eu-vat-compliance-monitor.md) |
| [License Lookup & Verification: Bulk Contractor, Nurse, NPI](https://apify.com/fayoussef/license-roster-monitor?fpr=youssef) | `license-roster-monitor` | Bulk professional license lookup and verification for contractors, nurses, electricians, real estate agents and healthcare providers (NPI)... | [Guide](actors/license-roster-monitor.md) |
| [Website Change Monitor: Page Diff & Change Detection Alerts](https://apify.com/fayoussef/website-change-monitor?fpr=youssef) | `website-change-monitor` | Monitor any web page for changes and get a line-by-line diff of what was added and removed. Website change detection for competitor... | [Guide](actors/website-change-monitor.md) |

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
