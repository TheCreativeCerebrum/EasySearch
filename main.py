import get_linkedin_data
import apply_to_easy_apply_jobs

linkedin_url = "https://www.linkedin.com/in/johndoe/"
data = get_linkedin_data.get_linkedin_data(linkedin_url)

# Search for Easy Apply jobs.
query_controls = {
    "keywords": "software engineer",
    "location": "San Francisco",
}

jobs = apply_to_easy_apply_jobs.search_easy_apply_jobs(query_controls, data)

# Apply to the Easy Apply jobs.
success_count = apply_to_easy_apply_jobs.apply_to_easy_apply_jobs(jobs)

print("Successfully applied to {} jobs.".format(success_count))