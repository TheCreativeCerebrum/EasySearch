# file: main.py

import get_linkedin_data
import apply_to_easy_apply_jobs
import os

linkedin_url = "https://www.linkedin.com/in/johndoe/"
data = get_linkedin_data.get_linkedin_data(linkedin_url)

# Create the file data.json if it does not exist.
if not os.path.exists("data.json"):
    with open("data.json", "w") as f:
        json.dump({}, f)

# Search for Easy Apply jobs.
search_query_controls = {
    "keywords": "Engineer Manager",
    "location": "San Antonio",
}

jobs = apply_to_easy_apply_jobs.search_easy_apply_jobs(
    search_query_controls, data)

# Apply to the Easy Apply jobs.
success_count = apply_to_easy_apply_jobs.apply_to_easy_apply_jobs(jobs)

print("Successfully applied to {} jobs.".format(success_count))
