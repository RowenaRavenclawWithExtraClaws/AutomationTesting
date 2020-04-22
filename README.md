# Automation Testing
This project automates and tests the registeration page for the phptravels website. 
It is a little bit primitive but still elegant.
# Motivation
As a part of Pixelogic interview process, this project is a solution to thier assignment.
Assignment details is included in project files.
# Technologies and third-party packages
* [Python 3.7](https://www.python.org/downloads/release/python-370/) for object oriented design.
* [Selenium 3.141](https://pypi.org/project/selenium/) for driving Firefox natively.
* [Firefox geckodriver Linux64](https://github.com/mozilla/geckodriver/releases) for using Firefox as the main browser for testing. 
* [Request 2019.4.13](https://pypi.org/project/request/) for making http requests.
* [Validate_email 1.3 ](https://pypi.org/project/validate_email/) for email validation.
* [fpdf 1.7.2 ](https://pypi.org/project/fpdf/) for creating and constructing pdf files.
# Components
### This project is built with object oriented design, it has five main classes and six main files:
* __main.py:__ acts as the entry point and the excution script for the project.
* __test.py:__ where all the test cases are written.
* __testCase.py:__ generates all fields required for the sign up form in random fashion.
* __testCaseGenerator.py:__ generates a single test case (registration instance).
* __automate.py:__ automates browser actions like filling the sign up form.
* __report.py:__ constructs bug reports with basic information and screenshots.
### Other files:
* __checking.py:__ implements the text fields criteria stated in the assignment statement.
* __logs.txt:__ saves the http responses for every request to the registration page.
* __statement.txt:__ contains the main guide lines for this project.
* __bugReports:__ A folder which contains pdfs, text files and screenshots for the detected bugs.
# Installation
Just clone the repo and run the main.py script (assume having the required packages stated above).
# How it works
### by running the main.py script in terminal (python main.py):
* The unittest python package seaches for any method that starts with "test" and executes it.
* There is nine such methods located in the test.py script, each contains a single test case with certain conditions like all fields must be valid or last name and email must be invalid and the rest is valid.
* Each method uses the selenium webdriver to automate the registration page for the phptravels website on Firefox using the geckodriver.
* An http interceptor script is run for every request and the response is saved in the logs file.
* each method asserts two main conditions (successful and unsuccessful sign up process) based on the conditions available for the available test case.
* if any of the assertions failed, a screenshot is taken and a full bug report is produced accordingly.
# Limitations
* It's reports is primitive (a table contains basic information and a screenshot shows the browser state when the bug occured).
* Generation of valid phones and emails is not dynamic.
