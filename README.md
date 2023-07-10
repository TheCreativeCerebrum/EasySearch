# EasySearch
Quick &amp; Easy Job Search and Apploication Process

### Prerequisites

Python must be installed locally; Click [here](https://www.python.org/downloads/) to install specifying your OS

# Job Search Code

This code takes inputted values from the user and then creates a dictionary of the 6 categories:

* Contact information
* Professional summary
* Core competencies
* Education
* Work experience
* Job query controls

The dictionary is then used to find jobs that use Job Query Controls against Work Experience.

## How to use the code

1. Save the code as a Python file.
2. Run the code from the command line with, "python main.py"
   a. $185,000
   b. 401K, Health, Dental, Vision
   c. 10 years
   d. https://www.linkedin.com/in/sheadahl/
    1d. Still doesn't grab name
    2d. Asks for phone number (expected) | (XXX)000-0000
    3d. Asks for email (expected) | thecreativecerebrum@gmail.com
    4d. Asks for address (expected) | San Antonio, Texas 78240
3. Enter the requested information when prompted.
4. The code will print the results of the search to the console.
5. To use inputted data to apply to "Easy Apply" run command, "python apply_to_easy_apply_jobs.py"
6. To test the code from the command line type, "python test_with_input.py"
<!-- "python -m unittest test_get_linkedin_data.py" -->

## Requirements

* Python 3.6 or higher
* The `joblib` library

## Author

SheaDLady & Bard

## License

This code is not yet licensed
