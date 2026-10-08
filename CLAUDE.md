# CLAUDE.md

GitHub catalog of every public Apify actor by `fayoussef` (Youssef Farhan, AutomationByExperts),
published as `github.com/automationbyexperts/web-scraping-apis` (local folder `APIFY/web-scraping-apis`).
The repo name deliberately leaves out "Apify": it targets what people search for, and "Apify" stays in
the description, topics and page text. It is a discovery surface for Google
and AI assistants: every Apify link carries `?fpr=youssef` and every actor links back to
`https://automationbyexperts.com/apify/<slug>`.

This folder is **not an actor** and lives outside `all_public_actors` on purpose. Never run
`apify push` here and never edit actor folders from here.

## Writing rules

- Never use em dashes anywhere. `build.py` converts them in Store text and fails if one survives.
- Never state a price. Prices live in the Apify Console. The build fails on `$<digit>` outside code blocks.
- No credentials: the build fails on `dataimpulse`, `sk-or-v1-`, `CAP-`, `apify_api_`.

## Everything except `data/overrides.json`, `data/tasks.json` and the scripts is generated

Do not hand-edit `README.md`, `actors/`, `categories/`, `llms.txt`, `llms-full.txt` or
`data/actors.json`: the next build overwrites them. Change `scripts/build.py` instead.

| File | Source |
|---|---|
| Actor list, titles, descriptions, users, rating | Apify Store API `store?username=fayoussef` (public) |
| Actors the Store search omits (rentals) | `data/overrides.json` `extraActors` |
| Categories | website `https://automationbyexperts.com/llms.txt`, `### Category` sections |
| Use cases, example inputs | `data/tasks.json`, snapshot of the published task landing pages |
| Agent-payable flag (`agenticPayments`) | Store API `store?username=fayoussef&allowsAgenticUsers=true`; drives `agentic-payments.md`, the x402/Skyfire block in each eligible guide and the `[agent-payable]` tag in `llms.txt` |

## Commands

```bash
python scripts/build.py          # rebuild everything, public data only, no token
python scripts/refresh_tasks.py  # local only: re-snapshot public tasks (token from APIFY_TOKEN or apify login)
```

Run `refresh_tasks.py` after publishing new task landing pages, then `build.py`, then commit both.
It must never run in CI: no Apify token is stored on GitHub.

## Weekly refresh

`.github/workflows/refresh.yml` runs `build.py` every Monday and commits only when content changed.
The "Updated" date only moves when something else changed, so quiet weeks make no commit.
If the Store API returns under 80% of the previous actor count the build refuses to run, and if the
website `llms.txt` is down it reuses the previous categories.

## Actors not on the website

An actor missing from the website `llms.txt` is filed under "Developer Tools & APIs" with a NOTE in
the build log. Fix it by adding the actor to the website, or pin a category in
`data/overrides.json` `category`.
