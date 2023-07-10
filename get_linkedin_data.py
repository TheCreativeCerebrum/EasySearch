# file: get_linkedin_data.py

import requests
import bs4
import json
import os

def get_linkedin_data(linkedin_url):
  """Returns a dictionary of data from the LinkedIn URL."""

  # Get the LinkedIn URL from the user.

  linkedin_url = input("Enter your LinkedIn URL: ")

  response = requests.get(linkedin_url)
  soup = bs4.BeautifulSoup(response.content, "html.parser")

  data = {}

  # Check if the soup object is None.

  if soup is None:
    raise ValueError("Invalid LinkedIn URL")

  # Get personal contact information.

  full_name = soup.find("h1", class_="text-heading-xlarge inline t-24 v-align-middle break-words")
  if full_name is not None:
    full_name = full_name.text
  # else:
  #   full_name = input("Enter your full name: ")


  tblack = soup.find("tblack", class_="text-body-small inline t-black--light break-words")
  phone_number = soup.find("tblack", class_="t-14 t-black t-normal")
  # if phone_number is None:
  #   phone_number = input("Enter your phone number: ")
  #   data["phone_number"] = phone_number

  pv = soup.find("a", class_="pv-contact-info__contact-link link-without-visited-state t-14")
  email = soup.find("pv", class_="pv-contact-info__ci-container t-14")
  # if email is None:
  #   email = input("Enter your email address: ")
  #   data["email"] = email

  tlight = soup.find("tlight", class_="text-body-small inline t-black--light break-words")
  address = soup.find("tlight", class_="pv-text-details__left-panel mt2")
# Manual enter of address
  # address = soup.find("li", class_="pv-contact-info__address")
  # if address is None:
  #   address = input("Enter your address: ")
  #   data["address"] = address

  # Get professional summary.

  headline = soup.find("h2", class_="pv-profile-top-card__headline")
  if headline is not None:
    headline = headline.text
  # else:
  #   headline = None

  # Get core competencies

  data["skills"] = [
      skill.text for skill in soup.find_all("li", class_="pv-skills-section__skill-item")
  ]
# each skills is in "liClass", class_="artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"

  # Get education.
    #Dates in "dateClass", class_= "block data-test-date-dropdown__dropdowns="" class="display-flex"
  data["education"] = []
  for education_item in soup.find_all("div", class_="pv-education-summary__item"):
    school = education_item.find("h3", class_="pv-education-summary__school").text
    degree = education_item.find("h4", class_="pv-education-summary__degree").text
    concentration = education_item.find("span", class_="pv-education-summary__field-of-study").text
    year_graduated = education_item.find("span", class_="pv-education-summary__year").text
    data["education"].append({
        "school": school,
        "degree": degree,
        "fieldOfStudy": fieldOfStudy,
        "concentration": concentration,
        "year_graduated": year_graduated,
    })

  # Get work experience.

  data["experience"] = []
  for experience_item in soup.find_all("div", class_="pv-work-experience-entity"):
    companyName = experience_item.find("h3", class_="pv-work-experience-entity__company").text
    title = experience_item.find("h4", class_="pv-work-experience-entity__position").text
    start_date = experience_item.find("span", class_="pv-work-experience-entity__dates").text.split("–")[0]
    end_date = experience_item.find("span", class_="pv-work-experience-entity__dates").text.split("–")[1]
    description = experience_item.find("div", class_="pv-work-experience-entity__description").text
    data["experience"].append({
        "companyName": companyName,
        "title": title,
        "start_date": start_date,
        "end_date": end_date,
        "description": description,
    })


#get query_controls

  salary = input("Enter your desired salary: ")
  benefits = input("Enter your desired benefits: ")
  years_of_experience = input("Enter your desired years of experience: ")
  data["salary"] = salary
  data["benefits"] = benefits
  data["years_of_experience"] = years_of_experience

  return data

def save_data_as_json(data):
  """Saves the data as a JSON file.

  Args:
    data: The data to be saved.
  """

  if not os.path.exists("data.json"):
    with open("data.json", "w+") as f:
      json.dump({}, f)

  with open("data.json", "w+") as f:
    json.dump(data, f)

if __name__ == "__main__":
  data = get_linkedin_data()
  save_data_as_json(data)