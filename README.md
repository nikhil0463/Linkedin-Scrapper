# Linkedin-Scrapper

A small, easy-to-run Python script that uses the `jobspy` scraper to collect job postings (the example focuses on LinkedIn by default). This repository contains a single example (`Scrapper.py`) you can edit to customize searches and save results to CSV.

## What this does

- Uses the `jobspy` module to search job sites (the example targets LinkedIn).
- Returns structured job data (title, company, location, description, job URL, and more).
- The included example shows common options you can change: search terms, location, sites, how many results to fetch, and whether to fetch the full LinkedIn description.

## Prerequisites

- Python 3.10+ (this workspace used Python 3.11).
- The `jobspy` package (imported in `Scrapper.py`). If you don't already have it installed:

```pwsh
pip install jobspy
```

If `jobspy` is a local module in your environment, make sure it's discoverable on `PYTHONPATH` or installed into your virtual environment.

## Quick start

1. Open the repository in your terminal.
2. (Optional) Create and activate a virtual environment:

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies (if you create a `requirements.txt`) or install `jobspy` directly:

```pwsh
pip install jobspy
# or if you add a requirements file:
pip install -r requirements.txt
```

4. Run the example scraper:

```pwsh
python Scrapper.py
```

You should see output reporting how many jobs were found and a preview of the dataframe printed to the console. The script contains a commented line you can uncomment to save results to `jobs.csv`.

## How the example works

Open `Scrapper.py` to see a sample call to `jobspy.scrape_jobs(...)` with these key options:

- `site_name`: list of sites to search (e.g., `['linkedin']`, `['glassdoor']`, `['naukri']`).
- `search_term`: job title or keywords (e.g., `"Data engineer"`).
- `location`: location to search (e.g., `"United States"`).
- `results_wanted`: maximum number of job results to return.
- `hours_old`: how recent the jobs should be (e.g., `1` for last hour).
- `linkedin_fetch_description`: when True, the scraper tries to fetch the full LinkedIn job description (slower).
- `proxies`: optional list of proxies for requests (commented in the example).


## Customization tips

- Increase `results_wanted` to collect more listings, but be mindful of rate limiting.
- Set `linkedin_fetch_description=True` only when you need full descriptions (it makes runs slower).
- Change `site_name` or `country_indeed` to target different job boards or geographies.
- If scraping fails, ensure `jobspy` supports the target site or try rotating proxies.

## Credits

This project uses the JobSpy scraper created by the original author at:

https://github.com/speedyapply/JobSpy

Please see that repository for the upstream implementation, license, and contributors.
