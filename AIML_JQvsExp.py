import re
import random
import joblib

def get_contact_info(first_name, last_name, phone_number, email, address, linkedin_url):
  """Returns a dictionary of contact information."""
  contact_info = {
    "first_name": first_name,
    "last_name": last_name,
    "phone_number": phone_number,
    "email": email,
    "address": address,
    "linkedin_url": linkedin_url,
  }
  return contact_info

def get_professional_summary(summary):
  """Returns a string of professional summary."""
  professional_summary = summary
  return professional_summary

def get_core_competencies(skills):
  """Returns a list of core competencies."""
  core_competencies = []
  for skill in skills:
    if skill:
      core_competencies.append(skill)
  return core_competencies

def get_education(school, degree, concentration, year_graduated, gpa):
  """Returns a dictionary of education."""
  education = {
    "school": school,
    "degree": degree,
    "concentration": concentration,
    "year_graduated": year_graduated,
    "gpa": gpa,
  }
  return education

def get_work_experience(employer, position, length_at_company, description):
  """Returns a dictionary of work experience."""
  work_experience = {
    "employer": employer,
    "position": position,
    "length_at_company": length_at_company,
    "description": description,
  }
  return work_experience

def get_job_query_controls(salary, benefits, years_of_experience):
  """Returns a dictionary of job query controls."""
  job_query_controls = {
    "salary": salary,
    "benefits": benefits,
    "years_of_experience": years_of_experience,
  }
  return job_query_controls

def main():
  """Takes inputted values and returns a dictionary of the 6 categories."""
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  phone_number = input("Enter your phone number: ")
  email = input("Enter your email address: ")
  address = input("Enter your address: ")
  linkedin_url = input("Enter your LinkedIn URL: ")
  summary = input("Enter your professional summary: ")
  skills = input("Enter your core competencies (separated by commas): ")
  skills = re.split(",", skills)
  school = input("Enter your school: ")
  degree = input("Enter your degree: ")
  concentration = input("Enter your concentration: ")
  year_graduated = input("Enter your year graduated: ")
  gpa = input("Enter your GPA (optional): ")
  employer = input("Enter your employer: ")
  position = input("Enter your position: ")
  length_at_company = input("Enter your length at company (mm/yyyy): ")
  description = input("Enter a description of your work experience: ")
  salary = input("Enter your desired salary: ")
  benefits = input("Enter your desired benefits: ")
  years_of_experience = input("Enter your desired years of experience: ")

  contact_info = get_contact_info(first_name, last_name, phone_number, email, address, linkedin_url)
  professional_summary = get_professional_summary(summary)
  core_competencies = get_core_competencies(skills)
  education = get_education(school, degree, concentration, year_graduated, gpa)
  work_experience = get_work_experience(employer, position, length_at_company, description)
  job_query_controls = get_job_query_controls(salary, benefits, years_of_experience)

  data = {
    "contact_info": contact_info,
    "professional_summary": professional_summary,
    "core_competencies": core_competencies,
    "education": education,
    "work_experience": work_experience,
    "job_query_controls": job_query_controls,
  }

  model = joblib.load("model.pkl")
  predictions = model.predict(data)

  for prediction in predictions:
    print(prediction)

if __name__ == "__main__":
  main()