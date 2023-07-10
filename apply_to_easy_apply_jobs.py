#file apply_to_easy_apply_jobs.py

import requests
import json

with open("data.json", "r") as f:
  data = json.load(f)

def search_easy_apply_jobs(search_query_controls, data):
  """Searches for Easy Apply jobs that meet the given query controls and data.

  Args:
    search_query_controls: The query controls to use for the search.
    data: The data to use for the search.

  Returns:
    A list of Easy Apply jobs that meet the given criteria.
  """

  url = "https://www.linkedin.com/jobs/search/?easy_apply=true"
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"searchQueryControls": search_query_controls, "data": data})

  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
    return json.loads(response.content)["results"]
  else:
    return []

def apply_to_easy_apply_jobs(jobs):
  """Applies to the given Easy Apply jobs.

  Args:
    jobs: The Easy Apply jobs to apply to.

  Returns:
    The number of jobs that were applied to successfully.
  """

  success_count = 0
  for job in jobs:
    try:
      response = requests.post(job["applyUrl"])
      if response.status_code == 200:
        success_count += 1
    except requests.exceptions.RequestException:
      pass

  return success_count

if __name__ == "__main__":
  with open("get_linkedin_data.py") as f:
    data = json.load(f)

  search_query_controls = {
    "keywords": "Engineer Manager",
    "location": "San Antonio",
  }

  jobs = search_easy_apply_jobs(search_query_controls, data)

  success_count = apply_to_easy_apply_jobs(jobs)

  print("Successfully applied to {} jobs.".format(success_count))