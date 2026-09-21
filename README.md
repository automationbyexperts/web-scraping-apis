# Web Scraping APIs: 54 Ready-to-Run Scrapers and AI Tools (Apify)

> 54 ready-to-run Apify actors by AutomationByExperts (Youssef Farhan): car and real estate scrapers, e-commerce and price data, lead generation, bulk AI tools and SEO audits. No code and no servers: run them in the cloud and export to JSON, CSV or Excel.

**54 actors** | **2,429 users** | **114 ready-made use cases** | Updated 2026-09-21

[Website](https://automationbyexperts.com/apify?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis) | [All actors on Apify](https://apify.com/fayoussef?fpr=youssef) | [llms.txt for AI](llms.txt) | [JSON catalog](data/actors.json)

## What is this?

This repository is the open catalog of **AutomationByExperts**, the actor catalogue of Youssef Farhan, an independent Python developer who builds and maintains production web scrapers on the Apify platform. Every actor listed here is a hosted cloud tool: paste a URL or a search term, click Start, and download structured data. The catalog covers Car & Vehicle Scrapers, Real Estate Scrapers, E-commerce & Marketplace Scrapers, Price & Brand Monitoring, Lead Generation Actors, Bulk AI Tools, SEO & AI Visibility, Developer Tools & APIs. It is rebuilt every week from the live Apify Store, so the list stays current.

## Contents

- [Car & Vehicle Scrapers](#car--vehicle-scrapers) (12)
- [Real Estate Scrapers](#real-estate-scrapers) (4)
- [E-commerce & Marketplace Scrapers](#e-commerce--marketplace-scrapers) (7)
- [Price & Brand Monitoring](#price--brand-monitoring) (4)
- [Lead Generation Actors](#lead-generation-actors) (12)
- [Bulk AI Tools](#bulk-ai-tools) (4)
- [SEO & AI Visibility](#seo--ai-visibility) (5)
- [Developer Tools & APIs](#developer-tools--apis) (6)
- [How to run an Apify actor](#how-to-run-an-apify-actor)
- [FAQ](#faq)
- [Need a custom scraper?](#need-a-custom-scraper)

## Car & Vehicle Scrapers

Live car, RV and classifieds listings, dealer website inventory and dealer reviews.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [AutoTrader Canada Car Scraper: Prices, VIN, Mileage & Dealers](https://apify.com/fayoussef/autotrader-canada?fpr=youssef) | Our autotrader.ca scraper makes it simple to collect car listings at scale. It automatically gathers URLs from all available pages and extracts complete details for... | [Find used Toyota RAV4s for sale around Toronto](https://apify.com/fayoussef/autotrader-canada/examples/toyota-rav4-used-toronto?fpr=youssef)<br>[Export used pickup trucks under 40,000 CAD in Alberta](https://apify.com/fayoussef/autotrader-canada/examples/used-pickup-trucks-alberta-under-40000?fpr=youssef) | [Guide](actors/autotrader-canada.md) |
| [AutoScout24 All-Country Scraper](https://apify.com/fayoussef/autoscout24?fpr=youssef) | Our autoscout24 scraper makes it simple to collect listings at scale and in all countries. Works on autoscout24.de, .at, .fr, .it, .es, .nl, .be, .lu and .com | [Find used VW Golfs in Germany under 15,000 EUR](https://apify.com/fayoussef/autoscout24/examples/vw-golf-germany-under-15000?fpr=youssef)<br>[Export used electric cars in the Netherlands and Belgium](https://apify.com/fayoussef/autoscout24/examples/electric-cars-netherlands-belgium?fpr=youssef) | [Guide](actors/autoscout24.md) |
| [AutoTrader Canada Car Scraper](https://apify.com/fayoussef/autotrader-ca?fpr=youssef) | Our autotrader.ca scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing cars. | [Find used Honda Civics for sale around Montreal](https://apify.com/fayoussef/autotrader-ca/examples/honda-civic-used-montreal?fpr=youssef)<br>[Export used SUVs under 25,000 CAD around Ottawa](https://apify.com/fayoussef/autotrader-ca/examples/used-suvs-under-25000-ottawa?fpr=youssef) | [Guide](actors/autotrader-ca.md) |
| [Kijiji.ca Scraper: Autos, Real Estate & Classifieds](https://apify.com/fayoussef/kijiji-scraper?fpr=youssef) | Efficiently scrapes Kijiji.ca listings: vehicles, real estate, and more. Extracts detailed data including phone number, price, location, specs, and images from search... | [Scrape used cars and trucks in Calgary on Kijiji](https://apify.com/fayoussef/kijiji-scraper/examples/calgary-used-trucks-kijiji?fpr=youssef)<br>[Export apartments for rent in Ottawa from Kijiji](https://apify.com/fayoussef/kijiji-scraper/examples/ottawa-apartments-for-rent-kijiji?fpr=youssef) | [Guide](actors/kijiji-scraper.md) |
| [CarGurus Scraper (US, Canada & UK Car Listings)](https://apify.com/fayoussef/cargurus-listings-scraper?fpr=youssef) | Scrape CarGurus vehicle listings from .com, .ca and .co.uk. Returns price, mileage, VIN, specs, dealer info and all images per listing. | [Find the best used car deals near New York on CarGurus](https://apify.com/fayoussef/cargurus-listings-scraper/examples/used-car-deals-near-new-york?fpr=youssef)<br>[Export Toronto used car listings from CarGurus Canada](https://apify.com/fayoussef/cargurus-listings-scraper/examples/toronto-used-cars-cargurus-canada?fpr=youssef) | [Guide](actors/cargurus-listings-scraper.md) |
| [autotrader.co.za Car Scraper with Seller Phone Numbers](https://apify.com/fayoussef/autotrader-co-za-scraper?fpr=youssef) | Scrape autotrader.co.za car listings across every page: price, mileage, specs, dealer and location, plus the seller's phone number. | [Find used Toyota Hilux bakkies with seller phone numbers](https://apify.com/fayoussef/autotrader-co-za-scraper/examples/used-bakkies-with-seller-phone-numbers?fpr=youssef)<br>[Export nearly new automatic cars for sale in South Africa](https://apify.com/fayoussef/autotrader-co-za-scraper/examples/nearly-new-automatic-cars-south-africa?fpr=youssef) | [Guide](actors/autotrader-co-za-scraper.md) |
| [AutoTrader Australia Car Scraper: Prices, VIN & Dealers](https://apify.com/fayoussef/autotrader-au-scraper?fpr=youssef) | Scrape Autotrader Australia. Paste any autotrader.com.au search URL to export every vehicle: price, make, model, variant, year, odometer, transmission, fuel type... | [Export used Toyota HiLux listings across Australia](https://apify.com/fayoussef/autotrader-au-scraper/examples/used-toyota-hilux-australia?fpr=youssef)<br>[Scrape used car listings in Sydney from Autotrader](https://apify.com/fayoussef/autotrader-au-scraper/examples/sydney-used-cars-autotrader-au?fpr=youssef) | [Guide](actors/autotrader-au-scraper.md) |
| [PistonHeads Scraper: UK Used, Classic & Performance Cars](https://apify.com/fayoussef/pistonheads?fpr=youssef) | Our pistonheads.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each listing card. | [Track Porsche 911s for sale on PistonHeads](https://apify.com/fayoussef/pistonheads/examples/porsche-911-for-sale-uk?fpr=youssef)<br>[Find performance cars between 20,000 and 40,000 GBP](https://apify.com/fayoussef/pistonheads/examples/performance-cars-20k-to-40k-uk?fpr=youssef) | [Guide](actors/pistonheads.md) |
| [Car Dealer Website Inventory Scraper: VIN, Price & Stock](https://apify.com/fayoussef/dealer-inventory-scraper?fpr=youssef) | Scrape live vehicle inventory from any car dealership's own website, not a marketplace. Paste a dealer homepage and get every car at VIN level with price, mileage and... | [Export a dealership's used inventory from its own website](https://apify.com/fayoussef/dealer-inventory-scraper/examples/dealer-website-used-inventory-export?fpr=youssef)<br>[Track price drops on competing dealer lots](https://apify.com/fayoussef/dealer-inventory-scraper/examples/dealer-price-drop-tracker?fpr=youssef) | [Guide](actors/dealer-inventory-scraper.md) |
| [Kijiji Auto & Classifieds Scraper Actor](https://apify.com/fayoussef/kijiji-ca-scraper?fpr=youssef) | Kijiji.ca listings scraper. Extracts detailed data including phone number, price, location, specs, and images from search results (with pagination) or direct ad URLs... | [Scrape used cars for sale in Toronto on Kijiji](https://apify.com/fayoussef/kijiji-ca-scraper/examples/toronto-used-cars-kijiji?fpr=youssef)<br>[Export apartments for rent in Toronto from Kijiji](https://apify.com/fayoussef/kijiji-ca-scraper/examples/toronto-apartments-for-rent-kijiji?fpr=youssef) | [Guide](actors/kijiji-ca-scraper.md) |
| [RVTrader Scraper: RV Listings, Prices, VIN & Dealer Data](https://apify.com/fayoussef/rvtrader-scraper?fpr=youssef) | Scrape RV listings from RVTrader.com by search URL or by filters (type, make, model, price, year, mileage, ZIP radius). Returns 55+ fields per listing: price and full... | [Find used Class C motorhomes under 80,000 dollars](https://apify.com/fayoussef/rvtrader-scraper/examples/used-class-c-motorhomes-under-80k?fpr=youssef)<br>[Track price reduced travel trailers on RVTrader](https://apify.com/fayoussef/rvtrader-scraper/examples/travel-trailers-price-reduced?fpr=youssef) | [Guide](actors/rvtrader-scraper.md) |
| [Car Dealer Reviews & Reputation Monitor (DealerRater)](https://apify.com/fayoussef/dealer-reputation-monitor?fpr=youssef) | Pull every DealerRater review for any car dealership by name or URL. Get the star rating broken down by price transparency, trade-in, finance and service time, plus the... | [Export every DealerRater review for a dealership](https://apify.com/fayoussef/dealer-reputation-monitor/examples/dealerrater-reviews-export?fpr=youssef)<br>[Get alerted to new 1 and 2 star dealer reviews](https://apify.com/fayoussef/dealer-reputation-monitor/examples/negative-dealer-review-alerts?fpr=youssef) | [Guide](actors/dealer-reputation-monitor.md) |

More detail: [Car & Vehicle Scrapers guide](categories/vehicle-scrapers.md) | [on the website](https://automationbyexperts.com/apify/category/vehicle-scrapers?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## Real Estate Scrapers

Property listings, prices, agent contacts and GPS coordinates at scale.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [Spitogatos.gr Scraper: Greek Property Listings & Agent Phones](https://apify.com/fayoussef/spitogatos-scraper?fpr=youssef) | Scrape real estate listings and Agents from Spitogatos.gr in both English and Greek. Collect prices, photos, location, and more. Easy setup, fast results, ready for... | [Find apartments for sale in Kolonaki, Athens](https://apify.com/fayoussef/spitogatos-scraper/examples/kolonaki-apartments-for-sale?fpr=youssef)<br>[Find apartments for rent in Thessaloniki under 600 EUR](https://apify.com/fayoussef/spitogatos-scraper/examples/thessaloniki-apartments-for-rent-under-600?fpr=youssef) | [Guide](actors/spitogatos-scraper.md) |
| [Centris.ca Scraper: Quebec Real Estate Listings & Photos](https://apify.com/fayoussef/centris-property-scraper?fpr=youssef) | Scrape Centris.ca real estate listings into clean structured data: MLS number, price, full address, rooms, bedrooms, bathrooms, the full description and characteristics... | [Export houses and condos for sale on Montreal Island](https://apify.com/fayoussef/centris-property-scraper/examples/montreal-houses-for-sale-centris?fpr=youssef)<br>[Scrape apartments for rent on Montreal Island from Centris](https://apify.com/fayoussef/centris-property-scraper/examples/montreal-rentals-centris?fpr=youssef) | [Guide](actors/centris-property-scraper.md) |
| [XE.gr Greek Property Scraper](https://apify.com/fayoussef/xe-gr-scraper?fpr=youssef) | Scrape Greek real estate listings from XE.gr: prices, size, rooms, GPS coordinates, amenities, photos and advertiser phone numbers. Works in every language XE.gr... | [Find apartments for rent in Athens with phone numbers](https://apify.com/fayoussef/xe-gr-scraper/examples/athens-apartments-for-rent?fpr=youssef)<br>[Export homes for sale in Thessaloniki](https://apify.com/fayoussef/xe-gr-scraper/examples/thessaloniki-homes-for-sale?fpr=youssef) | [Guide](actors/xe-gr-scraper.md) |
| [Spitogatos Cyprus Scraper: Property Listings & Agent Phones](https://apify.com/fayoussef/spitogatos-cy-scraper?fpr=youssef) | Scrape property listings and estate agents from Spitogatos.com.cy in English or Greek. Paste any search, listing or agent URL, or search by town, price and property... | [Find apartments for rent in Limassol, Cyprus under 1500 EUR](https://apify.com/fayoussef/spitogatos-cy-scraper/examples/limassol-apartments-for-rent-under-1500?fpr=youssef)<br>[Export homes for sale in Paphos, Cyprus with agent phones](https://apify.com/fayoussef/spitogatos-cy-scraper/examples/paphos-homes-for-sale-cyprus?fpr=youssef) | [Guide](actors/spitogatos-cy-scraper.md) |

More detail: [Real Estate Scrapers guide](categories/real-estate-scrapers.md) | [on the website](https://automationbyexperts.com/apify/category/real-estate-scrapers?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## E-commerce & Marketplace Scrapers

Product data, prices, EAN/SKU, stock and seller info from major marketplaces.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [wallapop Scraper (Spain,Italy,Portugal)](https://apify.com/fayoussef/wallapop-scraper?fpr=youssef) | Scrape Wallapop listings at scale across Spain, Italy, and Portugal without writing a single line of code. Paste any Wallapop search URL or item URL, and this actor... | [Scrape used cars under 5,000 EUR on Wallapop Spain](https://apify.com/fayoussef/wallapop-scraper/examples/used-cars-spain-under-5000?fpr=youssef)<br>[Track used car listings on Wallapop Italy](https://apify.com/fayoussef/wallapop-scraper/examples/wallapop-italy-used-cars?fpr=youssef) | [Guide](actors/wallapop-scraper.md) |
| [Fnac.com Scraper: Prices, EAN, Stock, Sellers & Reviews](https://apify.com/fayoussef/fnac-data-scraping?fpr=youssef) | Scrape fnac.com products from any search, category or product URL, or by keyword with brand, category, price, seller and stock filters. Get price, list price, discount... | [Scrape Fnac laptop prices, EAN and stock in France](https://apify.com/fayoussef/fnac-data-scraping/examples/fnac-laptop-prices-france?fpr=youssef)<br>[Find Lenovo and HP laptops under 600 EUR sold by Fnac](https://apify.com/fayoussef/fnac-data-scraping/examples/fnac-lenovo-hp-laptops-under-600?fpr=youssef) | [Guide](actors/fnac-data-scraping.md) |
| [G2G Scraper: Extract G2G.com Prices, Sellers & Stock](https://apify.com/fayoussef/g2g-offer-scraper?fpr=youssef) | Scrape live G2G.com prices, sellers, stock and delivery times from any category or Trending URL. Export JSON, CSV or Excel. No G2G login or API key needed. | [Track WoW Classic gold prices and sellers on G2G](https://apify.com/fayoussef/g2g-offer-scraper/examples/wow-classic-gold-prices-g2g?fpr=youssef)<br>[Monitor FC 26 coin prices across G2G sellers](https://apify.com/fayoussef/g2g-offer-scraper/examples/fc-26-coins-price-tracker?fpr=youssef) | [Guide](actors/g2g-offer-scraper.md) |
| [Bike24 Scraper: Cycling Product Prices, Stock & Specs](https://apify.com/fayoussef/bike24-result-scraper?fpr=youssef) | Our bike24.com scraper effortlessly gathers URLs from all pages and extracts detailed information from each product page | [Track Bike24 prices and stock for a product category](https://apify.com/fayoussef/bike24-result-scraper/examples/bike24-category-price-and-stock-tracker?fpr=youssef) | [Guide](actors/bike24-result-scraper.md) |
| [FnacPro Scraper: Product, Price, EAN & Spec Extractor](https://apify.com/fayoussef/fnacpro-scraper?fpr=youssef) | Scrape fnacpro.com product data at scale: price, EAN, reference, brand, availability, condition, full specifications, ratings, images and video, from any product or... | - | [Guide](actors/fnacpro-scraper.md) |
| [Skroutz Scraper: Prices, Shop Offers & Price History](https://apify.com/fayoussef/skroutz-scraper?fpr=youssef) | Scrape Skroutz products from Greece, Cyprus, Bulgaria, Romania, Germany and Malta in English, Greek, Bulgarian, Romanian or German. Paste any category, brand, shop or... | [Compare iPhone 17 Pro prices across all Skroutz countries](https://apify.com/fayoussef/skroutz-scraper/examples/iphone-17-pro-prices-all-skroutz-countries?fpr=youssef)<br>[Τιμές πλυντηρίων ρούχων στο Skroutz με ιστορικό τιμών](https://apify.com/fayoussef/skroutz-scraper/examples/washing-machine-prices-greece-greek?fpr=youssef) | [Guide](actors/skroutz-scraper.md) |
| [Cheap Amazon Scraper: Extract Products, Offers, Prices](https://apify.com/fayoussef/cheap-amazon-scraper?fpr=youssef) | Fast, reliable Amazon scraper. Extract product details, search results, seller offers and raw HTML from 21 marketplaces with geo-targeting and ZIP-level pricing. | - | [Guide](actors/cheap-amazon-scraper.md) |

More detail: [E-commerce & Marketplace Scrapers guide](categories/ecommerce-scrapers.md) | [on the website](https://automationbyexperts.com/apify/category/ecommerce-scrapers?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## Price & Brand Monitoring

Know every retailer selling your product, at what price, and who is breaking MAP.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [Competitor Price Tracker & Price Comparison by Product URL](https://apify.com/fayoussef/competitor-price-tracker-price-comparison-by-product-url?fpr=youssef) | Paste any product URL to get every retailer selling the same item, live prices, your market rank, and a suggested pricing action. Matches are strictly verified by UPC... | [Compare AirPods Pro prices across every US retailer](https://apify.com/fayoussef/competitor-price-tracker-price-comparison-by-product-url/examples/airpods-pro-price-comparison-us?fpr=youssef)<br>[Compare a product's price across UK retailers](https://apify.com/fayoussef/competitor-price-tracker-price-comparison-by-product-url/examples/uk-product-price-comparison-by-url?fpr=youssef) | [Guide](actors/competitor-price-tracker-price-comparison-by-product-url.md) |
| [Brand Protection: Fake Shop, Counterfeit & Typosquat Finder](https://apify.com/fayoussef/brand-abuse-counterfeit-detector?fpr=youssef) | Find fake webshops, counterfeit marketplace listings, typosquatted domains and impersonation profiles abusing your brand. AI classifies every hit, scores the risk, saves... | [Find fake webshops selling your brand](https://apify.com/fayoussef/brand-abuse-counterfeit-detector/examples/fake-shops-selling-your-brand?fpr=youssef)<br>[Sweep for typosquat domains impersonating your brand](https://apify.com/fayoussef/brand-abuse-counterfeit-detector/examples/typosquat-domain-sweep?fpr=youssef) | [Guide](actors/brand-abuse-counterfeit-detector.md) |
| [MAP Price Monitor: Amazon, eBay Violations & Rogue Sellers](https://apify.com/fayoussef/map-violation-monitor?fpr=youssef) | Enter your products and MAP prices and get every public offer advertised below them on Amazon, eBay, Best Buy and Newegg. AI verifies each listing is your exact product... | [Check Amazon and eBay for MAP violations](https://apify.com/fayoussef/map-violation-monitor/examples/amazon-ebay-map-violation-check?fpr=youssef)<br>[Detect unauthorized sellers of your products](https://apify.com/fayoussef/map-violation-monitor/examples/unauthorized-seller-detection?fpr=youssef) | [Guide](actors/map-violation-monitor.md) |
| [Amazon, eBay, Best Buy & Newegg Price Checker by ASIN or UPC](https://apify.com/fayoussef/multi-marketplace-price-checker?fpr=youssef) | Paste ASINs, UPCs, model numbers or product names and get what that exact product sells for on Amazon, eBay, Best Buy and Newegg. AI verifies every match, so... | [Compare a product's price on Amazon, eBay, Best Buy and Newegg](https://apify.com/fayoussef/multi-marketplace-price-checker/examples/compare-prices-amazon-ebay-bestbuy-newegg?fpr=youssef)<br>[Price check an arbitrage sourcing list across marketplaces](https://apify.com/fayoussef/multi-marketplace-price-checker/examples/arbitrage-sourcing-list-price-check?fpr=youssef) | [Guide](actors/multi-marketplace-price-checker.md) |

More detail: [Price & Brand Monitoring guide](categories/price-monitoring.md) | [on the website](https://automationbyexperts.com/apify/category/price-monitoring?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## Lead Generation Actors

Verified business contacts, developer emails, buying-intent posts and PR leads.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [Canada411 Scraper: Business Phones, Addresses](https://apify.com/fayoussef/canada411-ca?fpr=youssef) | Our canada411.ca scraper effortlessly gathers URLs from all pages and extracts contact information from each listing. | [Find business phone numbers in Toronto](https://apify.com/fayoussef/canada411-ca/examples/find-business-phone-numbers-toronto?fpr=youssef)<br>[Look up people by name and city on Canada411](https://apify.com/fayoussef/canada411-ca/examples/lookup-people-by-name-canada411?fpr=youssef) | [Guide](actors/canada411-ca.md) |
| [Whop Content Rewards Scraper: Clipping & UGC Campaigns](https://apify.com/fayoussef/whop-clipping-campaigns-scraper?fpr=youssef) | Scrape the Whop Content Rewards directory: reward per 1K views, budget left, burn rate, platforms, payout type and campaign URLs. Builds a private archive of campaigns... | [Find the highest paying clipping campaigns on Whop](https://apify.com/fayoussef/whop-clipping-campaigns-scraper/examples/high-paying-clipping-campaigns?fpr=youssef)<br>[Find low competition TikTok clipping campaigns](https://apify.com/fayoussef/whop-clipping-campaigns-scraper/examples/low-competition-tiktok-clipping-campaigns?fpr=youssef) | [Guide](actors/whop-clipping-campaigns-scraper.md) |
| [Journalist Request Finder: HARO Alternative for Digital PR](https://apify.com/fayoussef/journalist-request-finder?fpr=youssef) | Find live journalist source requests in one feed, pulled from SourceBottle call-outs and #journorequest posts on Bluesky and Mastodon. Filter by your topics, sort by... | [Find journalist requests about SaaS and marketing](https://apify.com/fayoussef/journalist-request-finder/examples/journalist-requests-saas-marketing?fpr=youssef)<br>[Daily alerts for new media requests in your niche](https://apify.com/fayoussef/journalist-request-finder/examples/daily-new-media-request-alerts?fpr=youssef) | [Guide](actors/journalist-request-finder.md) |
| [thebluebook.com Scraper](https://apify.com/fayoussef/thebluebook-scraper?fpr=youssef) | Scrape verified contractor and subcontractor profiles from thebluebook.com - the largest US construction directory - into clean JSON, CSV or Excel. Get company names... | [Build a list of plumbing contractors with emails](https://apify.com/fayoussef/thebluebook-scraper/examples/plumbing-contractor-leads-with-emails?fpr=youssef)<br>[Pull electrical contractor profiles without the email step](https://apify.com/fayoussef/thebluebook-scraper/examples/electrical-contractor-leads-fast?fpr=youssef) | [Guide](actors/thebluebook-scraper.md) |
| [GitHub Developer Lead Finder & Email Enricher](https://apify.com/fayoussef/github-developer-leads?fpr=youssef) | Find developers on GitHub and enrich each one with verified email, company, location, skills, and social links for recruiting and B2B outreach. | [Build an outreach list of React contributors](https://apify.com/fayoussef/github-developer-leads/examples/react-contributors-outreach-list?fpr=youssef)<br>[Find TypeScript developers in London with emails](https://apify.com/fayoussef/github-developer-leads/examples/typescript-developers-london-with-emails?fpr=youssef) | [Guide](actors/github-developer-leads.md) |
| [Luma Events Scraper (lu.ma): Events, Hosts & Social Handles](https://apify.com/fayoussef/luma-events-scraper?fpr=youssef) | Scrape events from Luma (lu.ma / luma.com) by city, category, calendar or event URL. Get dates, venues with GPS, ticket prices, guest counts and full descriptions, plus... | [Find upcoming AI events in San Francisco](https://apify.com/fayoussef/luma-events-scraper/examples/ai-events-in-san-francisco?fpr=youssef)<br>[Build a lead list of startup event organizers in London](https://apify.com/fayoussef/luma-events-scraper/examples/london-startup-event-organizer-leads?fpr=youssef) | [Guide](actors/luma-events-scraper.md) |
| [ATS Job Scraper: Greenhouse, Lever & Ashby by Company Domain](https://apify.com/fayoussef/company-domain-to-job-postings?fpr=youssef) | Paste company domains, get their live job postings. Finds each company's ATS board across Greenhouse, Lever, Ashby, Recruitee, SmartRecruiters and Personio, verifies it... | [Get every engineering job at YC companies](https://apify.com/fayoussef/company-domain-to-job-postings/examples/engineering-jobs-at-yc-companies?fpr=youssef)<br>[Pull remote jobs from a list of company domains](https://apify.com/fayoussef/company-domain-to-job-postings/examples/remote-jobs-from-a-prospect-list?fpr=youssef) | [Guide](actors/company-domain-to-job-postings.md) |
| [Naukrigulf Scraper: Gulf Jobs in 12 Languages](https://apify.com/fayoussef/naukrigulf-scraper?fpr=youssef) | Scrape Naukrigulf.com jobs across the UAE, Saudi Arabia, Qatar, Kuwait, Bahrain and Oman. Search in Arabic, Hindi, Malayalam, Tagalog and 8 more, and read every result... | [Find nurse jobs across the Gulf posted this week](https://apify.com/fayoussef/naukrigulf-scraper/examples/nurse-jobs-gulf-last-7-days?fpr=youssef)<br>[Get Dubai accounting jobs that publish a salary](https://apify.com/fayoussef/naukrigulf-scraper/examples/dubai-accounting-jobs-with-salary?fpr=youssef) | [Guide](actors/naukrigulf-scraper.md) |
| [Podcast Guesting Lead Finder: Find Shows & Host Emails](https://apify.com/fayoussef/podcast-guest-finder?fpr=youssef) | Find active, on-topic podcasts that book guests, with the host's contact email, ready for outreach. Search any niche on Apple's podcast index, filter to shows with a... | [Find B2B SaaS podcasts with host emails](https://apify.com/fayoussef/podcast-guest-finder/examples/b2b-saas-podcasts-with-host-emails?fpr=youssef)<br>[Build a pitch list of real estate investing podcasts](https://apify.com/fayoussef/podcast-guest-finder/examples/real-estate-investing-podcast-pitch-list?fpr=youssef) | [Guide](actors/podcast-guest-finder.md) |
| [AI Account Watch: Custom Sales Trigger Alerts](https://apify.com/fayoussef/ai-account-watch?fpr=youssef) | Watch a list of companies and get alerted when one does what you describe in plain English: raises funding, hires a CMO, opens a location, gets sued. AI reads fresh... | - | [Guide](actors/ai-account-watch.md) |
| [ClinicalTrials.gov Scraper: Trials, Sponsors & Investigators](https://apify.com/fayoussef/clinical-trials-intelligence?fpr=youssef) | Scrape ClinicalTrials.gov through the official v2 API. Search 500,000+ studies by condition, sponsor, drug, phase, status and location, get 40+ clean fields per trial... | [Find recruiting breast cancer trials in the United States](https://apify.com/fayoussef/clinical-trials-intelligence/examples/recruiting-breast-cancer-trials-usa?fpr=youssef)<br>[Monitor a pharma company's clinical trial pipeline](https://apify.com/fayoussef/clinical-trials-intelligence/examples/pharma-pipeline-monitor?fpr=youssef) | [Guide](actors/clinical-trials-intelligence.md) |
| [Reddit Scraper for Leads: Buying Intent Posts & Comments](https://apify.com/fayoussef/reddit-lead-finder?fpr=youssef) | Scrape Reddit posts and comments for buying intent: people asking for a tool, a recommendation, or an alternative to your competitor. Every lead is scored 0-100, budget... | [Find Reddit users looking for an email marketing tool](https://apify.com/fayoussef/reddit-lead-finder/examples/reddit-leads-for-email-marketing-tools?fpr=youssef)<br>[Get alerted to 'alternative to' threads about your competitors](https://apify.com/fayoussef/reddit-lead-finder/examples/competitor-alternative-threads-alert?fpr=youssef) | [Guide](actors/reddit-lead-finder.md) |

More detail: [Lead Generation Actors guide](categories/lead-generation.md) | [on the website](https://automationbyexperts.com/apify/category/lead-generation?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## Bulk AI Tools

Run hundreds of prompts, images, voiceovers or translations in a single run.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [Bulk AI Image Generator: Nano Banana, GPT Image \| No API Key](https://apify.com/fayoussef/bulk-ai-image-generator?fpr=youssef) | Generate hundreds of AI images from a list of prompts or an Excel/CSV file with Nano Banana Pro, Nano Banana 2 and GPT Image. Any aspect ratio up to 4K, up to 10... | [Generate product photos for an online store](https://apify.com/fayoussef/bulk-ai-image-generator/examples/product-photos-for-online-store?fpr=youssef)<br>[Create social media ad creatives in bulk](https://apify.com/fayoussef/bulk-ai-image-generator/examples/social-media-ad-creatives?fpr=youssef) | [Guide](actors/bulk-ai-image-generator.md) |
| [Run ChatGPT, Claude, Gemini & DeepSeek in Bulk (No API Key)](https://apify.com/fayoussef/bulk-llm-runner?fpr=youssef) | Run hundreds of prompts in parallel across GPT, Claude, Gemini, Perplexity, DeepSeek, Qwen, Kimi and 350+ models, with web search, JSON columns and side-by-side model... | [Write SEO product descriptions in bulk](https://apify.com/fayoussef/bulk-llm-runner/examples/seo-product-descriptions-in-bulk?fpr=youssef)<br>[Classify and tag customer reviews at scale](https://apify.com/fayoussef/bulk-llm-runner/examples/classify-customer-reviews?fpr=youssef) | [Guide](actors/bulk-llm-runner.md) |
| [Bulk Text to Speech: MP3 + SRT Subtitles \| No API Key](https://apify.com/fayoussef/bulk-text-to-speech?fpr=youssef) | Convert texts or an Excel/CSV file into MP3 voiceovers with perfectly timed SRT/VTT subtitles. 322 neural voices in 75 languages, word-by-word TikTok captions... | [Generate TikTok voiceovers with word by word captions](https://apify.com/fayoussef/bulk-text-to-speech/examples/tiktok-voiceovers-word-captions?fpr=youssef)<br>[Create Spanish voiceovers for product videos](https://apify.com/fayoussef/bulk-text-to-speech/examples/spanish-voiceovers-for-product-videos?fpr=youssef) | [Guide](actors/bulk-text-to-speech.md) |
| [Translate Excel, CSV & Websites in Bulk with AI \| No API Key](https://apify.com/fayoussef/bulk-ai-translator?fpr=youssef) | Translate Excel, CSV and Google Sheets files, whole websites, PDFs and SRT/VTT subtitles into 42 languages in one run, and get the same file back translated. Brand... | [Translate a product catalog into 5 languages](https://apify.com/fayoussef/bulk-ai-translator/examples/translate-product-catalog-5-languages?fpr=youssef)<br>[Translate a whole website into German](https://apify.com/fayoussef/bulk-ai-translator/examples/translate-website-into-german?fpr=youssef) | [Guide](actors/bulk-ai-translator.md) |

More detail: [Bulk AI Tools guide](categories/ai-bulk-tools.md) | [on the website](https://automationbyexperts.com/apify/category/ai-bulk-tools?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## SEO & AI Visibility

Measure how you rank in Google - and whether ChatGPT recommends you at all.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [SEO, GEO & AEO Audit: AI Search Readiness Checker](https://apify.com/fayoussef/seo-geo-aeo-audit?fpr=youssef) | Audit any website for Google SEO and AI search visibility in one run. Get 0-100 SEO, GEO & AEO scores per page, AI-crawler & llms.txt checks, schema validation, and a... | [Audit a website for AI search readiness](https://apify.com/fayoussef/seo-geo-aeo-audit/examples/ai-search-readiness-audit?fpr=youssef)<br>[Run a quick 5 page SEO check on a small business site](https://apify.com/fayoussef/seo-geo-aeo-audit/examples/quick-5-page-seo-check?fpr=youssef) | [Guide](actors/seo-geo-aeo-audit.md) |
| [Google Maps Geo-Grid Local Rank Tracker](https://apify.com/fayoussef/geo-grid-local-rank-tracker?fpr=youssef) | Track where a business ranks in the Google Maps local pack across a grid of points around it. Per-point rank, average rank, coverage, Share of Local Voice, top... | [Track a dentist's Google Maps ranking across a city](https://apify.com/fayoussef/geo-grid-local-rank-tracker/examples/dentist-google-maps-ranking-grid?fpr=youssef)<br>[Measure a restaurant's local pack visibility by neighbourhood](https://apify.com/fayoussef/geo-grid-local-rank-tracker/examples/restaurant-local-pack-visibility?fpr=youssef) | [Guide](actors/geo-grid-local-rank-tracker.md) |
| [AI Brand Visibility Tracker (ChatGPT, Perplexity & Gemini)](https://apify.com/fayoussef/ai-brand-visibility-tracker?fpr=youssef) | Is AI recommending you or your competitors? Track brand mentions, ranking position, sentiment, share of voice and cited sources in ChatGPT, Perplexity, Gemini, Claude &... | [Check if AI recommends your CRM to small businesses](https://apify.com/fayoussef/ai-brand-visibility-tracker/examples/crm-brand-visibility-in-ai-answers?fpr=youssef)<br>[Measure an ecommerce platform's share of voice in AI search](https://apify.com/fayoussef/ai-brand-visibility-tracker/examples/ecommerce-platform-ai-share-of-voice?fpr=youssef) | [Guide](actors/ai-brand-visibility-tracker.md) |
| [llms.txt Generator: llms-full.txt for Any Website (AI SEO)](https://apify.com/fayoussef/llms-txt-generator?fpr=youssef) | Generate a spec-compliant llms.txt and llms-full.txt for any website in one run. Crawls your sitemap or internal links, extracts every page's title, meta description and... | [Generate llms.txt and llms-full.txt for any website](https://apify.com/fayoussef/llms-txt-generator/examples/generate-llms-txt-for-any-website?fpr=youssef)<br>[Build an llms-full.txt for a documentation site](https://apify.com/fayoussef/llms-txt-generator/examples/llms-full-txt-for-documentation-site?fpr=youssef) | [Guide](actors/llms-txt-generator.md) |
| [SPF, DKIM & DMARC Checker: Email Deliverability Auditor](https://apify.com/fayoussef/email-deliverability-auditor?fpr=youssef) | Audit any domain's email deliverability in seconds. Checks SPF, DKIM (around 30 selectors), DMARC, MX, MTA-STS, BIMI and DNSSEC, tests your mail servers against DNS... | [Check SPF, DKIM and DMARC for a list of domains](https://apify.com/fayoussef/email-deliverability-auditor/examples/spf-dkim-dmarc-check-for-domains?fpr=youssef)<br>[Audit email authentication for all agency clients at once](https://apify.com/fayoussef/email-deliverability-auditor/examples/agency-client-email-authentication-audit?fpr=youssef) | [Guide](actors/email-deliverability-auditor.md) |

More detail: [SEO & AI Visibility guide](categories/seo-ai-visibility.md) | [on the website](https://automationbyexperts.com/apify/category/seo-ai-visibility?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## Developer Tools & APIs

A universal scraping API plus change monitoring for pages and datasets.

| Actor | What it does | Example use cases | Guide |
|---|---|---|---|
| [New Business License Feed: Fresh Openings by City](https://apify.com/fayoussef/business-license-feed?fpr=youssef) | Every business, food, liquor and trade license newly issued in Chicago, Los Angeles, New York, Seattle and New Orleans, filtered to the trades you sell to, with only... | - | [Guide](actors/business-license-feed.md) |
| [Dataset Diff: Only New & Changed Items From Any Actor](https://apify.com/fayoussef/dataset-diff?fpr=youssef) | Point it at any Apify Actor, Task or dataset and get only what changed since its last run: new rows, edited rows, rows that disappeared. Push the delta to Slack... | [Get only new places from a Google Maps scraper run](https://apify.com/fayoussef/dataset-diff/examples/new-google-maps-places-only?fpr=youssef)<br>[Get price change alerts from any Actor's dataset](https://apify.com/fayoussef/dataset-diff/examples/price-change-alerts-from-any-dataset?fpr=youssef) | [Guide](actors/dataset-diff.md) |
| [EU VAT Number Validation: Bulk VIES Check & Supplier Monitor](https://apify.com/fayoussef/eu-vat-compliance-monitor?fpr=youssef) | Validate a whole supplier or customer list against VIES, get the consultation number that proves you checked, and be told the moment a VAT number goes invalid or its... | - | [Guide](actors/eu-vat-compliance-monitor.md) |
| [License Verification & Expiry Monitor: Bulk US License Lookup](https://apify.com/fayoussef/license-roster-monitor?fpr=youssef) | Re-verify a whole roster of contractors, nurses, agents or providers against official state registries, then get only what changed: expired, suspended, revoked, lapsed... | - | [Guide](actors/license-roster-monitor.md) |
| [Scrape any site, Anti-Bot Proxy, JS Render & AI](https://apify.com/fayoussef/scrape-any-site-anti-bot-proxy-js-render-ai?fpr=youssef) | Free web scraper API for any website. Rotating anti-bot proxies, JS rendering, screenshots, CSS + AI extraction. Clean HTML, Markdown and JSON. | - | [Guide](actors/scrape-any-site-anti-bot-proxy-js-render-ai.md) |
| [Website Change Detector: Page Diff, Price & Content Alerts](https://apify.com/fayoussef/website-change-monitor?fpr=youssef) | Monitor any web page for changes and get a line-by-line diff of what was added and removed. Track competitor pricing, product listings, terms of service and job boards... | [Monitor a competitor's pricing page for changes](https://apify.com/fayoussef/website-change-monitor/examples/competitor-pricing-page-monitor?fpr=youssef)<br>[Get alerts when a terms of service page changes](https://apify.com/fayoussef/website-change-monitor/examples/terms-of-service-change-alerts?fpr=youssef) | [Guide](actors/website-change-monitor.md) |

More detail: [Developer Tools & APIs guide](categories/developer-tools.md) | [on the website](https://automationbyexperts.com/apify/category/developer-tools?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## How to run an Apify actor

**No code:** open any actor above, sign in to Apify (a free account works), fill in the form and click Start. Results download as JSON, CSV, Excel, XML or HTML.

**Python:**

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("fayoussef/<actor-name>").call(run_input={})
items = client.dataset(run["defaultDatasetId"]).list_items().items
```

**JavaScript:**

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: '<YOUR_APIFY_TOKEN>' });
const run = await client.actor('fayoussef/<actor-name>').call({});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
```

**AI agents (MCP):** connect `https://mcp.apify.com?tools=fayoussef/<actor-name>` in Claude, ChatGPT, Cursor or any MCP client.

Every actor guide has a ready-to-paste example input and snippets with the real actor name.

## FAQ

### What is an Apify actor?

An actor is a cloud program that runs on the [Apify](https://apify.com/?fpr=youssef) platform. It takes an input (a URL, a search term, a list of products), does the scraping or automation, and stores the results in a dataset you can download or read through an API.

### Are these scrapers free to try?

Yes. Every actor can be started with a free Apify account. Free runs have usage limits, and bigger jobs need an [Apify plan](https://apify.com/pricing?fpr=youssef). Current rates are shown on each Store page.

### Do I need to know how to code?

No. Each actor has an input form in the Apify Console. Code is optional, for people who want to call the actors from their own apps.

### Can ChatGPT, Claude or other AI agents use these actors?

Yes, through the Apify MCP server. Add `https://mcp.apify.com?tools=fayoussef/<actor-name>` to any MCP client and the agent can run the actor and read the data.

### How do I schedule a scraper or send the data somewhere?

Save your input as a task in the Apify Console, add a schedule, and connect an integration such as Make, Zapier, n8n, Google Drive or a webhook.

### Can I get a scraper for a site that is not listed?

Yes. Youssef Farhan builds custom scrapers and automations. See below.

## Need a custom scraper?

- Email: youssefarhan24@gmail.com
- Website: [AutomationByExperts](https://automationbyexperts.com/?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)
- Got a site in mind? [Suggest it here](https://automationbyexperts.com/apify?utm_source=github&utm_medium=referral&utm_campaign=web-scraping-apis)

## License

The catalog text and code snippets are MIT licensed. Actor names and Store content belong to their author.
