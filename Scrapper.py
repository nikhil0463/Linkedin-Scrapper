import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin"], # "glassdoor", "bayt", "naukri", "bdjobs"
    search_term="Data engineer",
    google_search_term="software engineer jobs near San Francisco, CA since yesterday",
    job_type = "fulltime", # "internship", "parttime", "contract", "temporary"
    # experience_level = "mid_level", # "mid_level", "senior_level", "internship"
    linkedin_fetch_description = True,
    location="United States",
    results_wanted=20,
    hours_old=1,
    country_indeed='USA',
    
    # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)
print(f"Found {len(jobs)} jobs")
selected_columns = ['job_url','title', 'company', 'location', 'description', 'job_level']
jobs = jobs[selected_columns]
print(jobs.head())
print(jobs.columns)
# jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel