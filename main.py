# file: main.py

import get_linkedin_data

linkedin_url = "https://www.linkedin.com/in/johndoe/"
data = get_linkedin_data.get_linkedin_data(linkedin_url)
print(data)