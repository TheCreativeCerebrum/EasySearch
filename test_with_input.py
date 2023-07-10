import get_linkedin_data
import apply_to_easy_apply_jobs
import main

import json

with open("test_data.json", "r") as f:
  data = json.load(f)

def test_get_linkedin_data():
  assert get_linkedin_data.get_data_from_json(data) == data

def test_apply_to_easy_apply():
  assert apply_to_easy_apply.apply_to_easy_apply(data) == True

def test_main():
  assert main.main(data) == True

# def test_get_linkedin_data_with_input():
#   """Tests the get_linkedin_data() function with input values."""
#   linkedin_url = "https://www.linkedin.com/in/johndoe/"
#   desired_salary = data["salary"]
#   benefits = data["benefits"]
#   years_of_experience = data["years_of_experience"]
#   experience = data["experience"][0]
#   skills = data["skills"]
#   education = data["education"][0]


#   data = get_linkedin_data.get_linkedin_data(linkedin_url)
#   assert data is not None
#   assert data["skills"] == ["Python", "Java", "JavaScript"]
#   assert data["full_name"] == "John Doe"
#   assert data["phone_number"] == "123-456-7890"
#   assert data["email"] == "johndoe@gmail.com"
#   assert data["address"] == "123 Main Street, Anytown, CA 12345"
#   assert data["headline"] == "Software Engineer"
#   assert data["education"][0]["school"] == "Stanford University"
#   assert data["education"][0]["degree"] == "Bachelor of Science in Computer Science"
#   assert data["education"][0]["concentration"] == "Software Engineering"
#   assert data["education"][0]["year_graduated"] == "2022"
#   assert data["experience"][0]["companyName"] == "Google"
#   assert data["experience"][0]["title"] == "Software Engineer"
#   assert data["experience"][0]["start_date"] == "2022-01-01"
#   assert data["experience"][0]["end_date"] == "2023-01-01"
#   assert data["experience"][0]["description"] == "Developed software for Google's search engine."
#   assert data["salary"] == "$200,000"
#   assert data["benefits"] == ["Health insurance", "Dental insurance", "Vision insurance"]
#   assert data["years_of_experience"] == 8

# def test_apply_to_easy_apply_jobs_with_input():
#   """Tests the apply_to_easy_apply_jobs() function with input values."""
#   linkedin_url = "https://www.linkedin.com/in/johndoe/"

#   data = get_linkedin_data.get_linkedin_data(linkedin_url)
#   jobs = apply_to_easy_apply_jobs.apply_to_easy_apply_jobs(data)
#   assert len(jobs) > 0

# if __name__ == "__main__":
#   test_get_linkedin_data_with_input()
#   test_apply_to_easy_apply_jobs_with_input()