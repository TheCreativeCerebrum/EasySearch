import random
import unittest

from ResumeDeets import get_contact_info, get_professional_summary, get_core_competencies, get_education, get_work_experience, get_job_query_controls


class TestJobSearch(unittest.TestCase):

    def test_get_contact_info(self):
        first_name = "John"
        last_name = "Doe"
        phone_number = "123-456-7890"
        email = "john.doe@example.com"
        address = "123 Main Street, Anytown, CA 12345"
        linkedin_url = "https://www.linkedin.com/in/johndoe/"

        contact_info = get_contact_info(first_name, last_name, phone_number, email, address, linkedin_url)

        self.assertEqual(contact_info["first_name"], first_name)
        self.assertEqual(contact_info["last_name"], last_name)
        self.assertEqual(contact_info["phone_number"], phone_number)
        self.assertEqual(contact_info["email"], email)
        self.assertEqual(contact_info["address"], address)
        self.assertEqual(contact_info["linkedin_url"], linkedin_url)

    def test_get_professional_summary(self):
        professional_summary = "I am a highly skilled and experienced software engineer with a passion for building innovative products. I have a proven track record of success in leading and delivering projects on time and within budget. I am also a team player and have a strong ability to work cross-functionally. I am confident that I can make a significant contribution to your team."

        self.assertEqual(get_professional_summary(), professional_summary)

    def test_get_core_competencies(self):
        skills = ["Python", "Java", "JavaScript", "SQL", "AWS"]

        core_competencies = get_core_competencies(skills)

        self.assertEqual(core_competencies, skills)

    def test_get_education(self):
        school = "Stanford University"
        degree = "Master of Science in Computer Science"
        concentration = "Machine Learning"
        year_graduated = "2020"
        gpa = "3.9"

        education = get_education(school, degree, concentration, year_graduated, gpa)

        self.assertEqual(education["school"], school)
        self.assertEqual(education["degree"], degree)
        self.assertEqual(education["concentration"], concentration)
        self.assertEqual(education["year_graduated"], year_graduated)
        self.assertEqual(education["gpa"], gpa)

    def test_get_work_experience(self):
        employer = "Google"
        position = "Software Engineer"
        length_at_company = "12/2018 - Present"
        work_experience = """
        I am a software engineer at Google, where I have been working for the past 3 years. I am responsible for developing and maintaining software for Google's search engine. I have a strong track record of success in delivering high-quality software on time and within budget. I am also a team player and have a strong ability to work cross-functionally.
        """

        self.assertEqual(get_work_experience(employer, position, length_at_company), work_experience)

    def test_get_job_query_controls(self):
        salary = 100000
        benefits = "Health insurance, dental insurance, vision insurance, 401k, paid time off"
        years_of_experience = 5

        job_query_controls = get_job_query_controls(salary, benefits, years_of_experience)

        self.assertEqual(job_query_controls["salary"], salary)
        self.assertEqual(job_query_controls["benefits"], benefits)
        self.assertEqual(job_query_controls["years_of_experience"], years_of_experience)


if __name__ == "__main__":
    unittest.main()