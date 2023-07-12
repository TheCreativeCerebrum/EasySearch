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
3. Enter the requested information when prompted:
LinkedIn Profile Link:
   a. https://www.linkedin.com/in/inesmontani/
Personal Information:
   a. FName LName
   b. (000)000-0000
   c. email@email.com
Search Query Parameters:
   a. San Antonio, TX
   b. $160,000+
   c. 401(k), Medical, Dental, Vision
   d. 10 years
4. This code will print the results of the search to the console and should save it as data.json file.
<!-- 5. To use inputted data to apply to "Easy Apply" run command, "python apply_to_easy_apply_jobs.py" -->
5. To test the code from the command line type, "python test_with_input.py"
<!-- "python -m unittest test_get_linkedin_data.py" -->

## Requirements

* Python 3.6 or higher
* The `joblib` library

## Author

SheaDLady & Bard

## License

This code is not yet licensed
