import unittest

from get_linkedin_data import get_linkedin_data


class TestGetLinkedInData(unittest.TestCase):

  def test_get_linkedin_data_with_valid_url(self):
    linkedin_url = "https://www.linkedin.com/in/johndoe/"
    data = get_linkedin_data(linkedin_url)
    self.assertIn("first_name", data)
    self.assertIn("last_name", data)
    self.assertIn("phone_number", data)
    self.assertIn("email", data)
    self.assertIn("address", data)
    self.assertIn("headline", data)
    self.assertIn("skills", data)
    self.assertIn("education", data)
    self.assertIn("experience", data)

  def test_get_linkedin_data_with_invalid_url(self):
    with self.assertRaises(ValueError):
      get_linkedin_data("https://www.linkedin.com/invalid_url/")


if __name__ == "__main__":
  unittest.main()