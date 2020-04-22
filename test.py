import unittest
from automate import AutomateRegistration
from testCaseGenrator import TestCaseGenerator
from httpInterceptor import HttpInterceptor
from report import Report
from datetime import datetime


# A class for constructing test cases using the unittest package.
class Test(unittest.TestCase):
    def setUp(self):
        self.automateRegister = AutomateRegistration()
        self.testCase = {}
        # A list for keeping track of the so-far registered emails in during the testing process.
        self.registeredEmail = ['boodnasser96@outlook.com']
        self.url = "https://www.phptravels.net/register"

    def testRegister1(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        # Saves the response to this request.
        HttpInterceptor.intercept(self.url)

        id = 1
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            # Asserts that the write page is opened in the browser.
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:  # Typing the test case entities into the form text fields.
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            # Asserts that the sign up process was a success.
            self.assertIn(
                'account', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Wrong password validation'
            summary = 'a prompt shows The Password field must meet its conditions'
            expectedResult = 'page tile should contain account'
            actualResult = 'page tile contains register'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister2(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            isValidFirstName=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        HttpInterceptor.intercept(self.url)

        id = 2
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'First name in wrong format'
            summary = 'First name must start with capital letter'
            expectedResult = 'a prompt shows that first name is invalid'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister3(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            isValidLastName=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        HttpInterceptor.intercept(self.url)

        id = 3
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Last name in wrong format'
            summary = 'Last name must start with capital letter and differ from first name'
            expectedResult = 'a prompt shows that last name is invalid'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister4(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            isValidEmail=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        HttpInterceptor.intercept(self.url)

        id = 4
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Email address in wrong format'
            summary = 'Email address should be valid'
            expectedResult = 'a prompt shows that email is invalid'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister5(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            isValidPassword=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        HttpInterceptor.intercept(self.url)

        id = 5
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Password in wrong format'
            summary = 'Password must have capital letter, small letter, with a limit of 8 characters'
            expectedResult = 'a prompt show that password is invalid'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister6(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            isValidConfirmedPassword=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        HttpInterceptor.intercept(self.url)

        id = 6
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register but failed'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Confirmed password is wrong'
            summary = 'Confirmed assword must be exactly the same as password'
            expectedResult = 'a prompt show that the entered confirmed password is wrong'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister7(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(isValidFirstName=False, isValidLastName=False, isValidPhone=False,
                                                           isValidEmail=False, isValidPassword=False, isValidConfirmedPassword=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        HttpInterceptor.intercept(self.url)

        id = 7
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register but failed'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Every field is wrong'
            summary = 'All fields have wrong formats or values at the same time'
            expectedResult = 'a prompt show that at least one field is in a wrong format'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister8(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            isValidFirstName=False, isValidEmail=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        id = 8
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register but failed'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'First name and email are invalid'
            summary = 'First name must start with capital letter, email must be valid'
            expectedResult = 'a prompt show either first name or email is in the wrong format'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()

    def testRegister9(self):
        print('first test is running...')

        self.testCase = TestCaseGenerator.generateTestCase(
            isValidLastName=False, isValidEmail=False, isValidPassword=False, registeredEmail=self.registeredEmail)
        self.registeredEmail.append(self.testCase['email'])
        self.automateRegister.driver.get(self.url)

        id = 9
        bugName = ''
        summary = ''
        expectedResult = ''
        actualResult = ''

        try:
            self.assertIn('Register', self.automateRegister.driver.title)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Unreachable site'
            summary = 'Trying to reach https://www.phptravels.net/register but failed'
            expectedResult = 'page tile should contain register'
            actualResult = 'page not found (400 HTTP Error)'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        for name in self.testCase:
            self.automateRegister.automateTextField(
                name, self.testCase[name])

        self.automateRegister.automateButtonClick('signupbtn')

        try:
            self.assertIn('register', self.automateRegister.driver.current_url)
        except:
            self.automateRegister.driver.save_screenshot(
                'bugReports/screenshots/test' + str(id) + '.png')
            bugName = 'Last name and email are invalid'
            summary = 'Last name must start with capital letter and\ndiffer from first name, email must be valid'
            expectedResult = 'a prompt show either last name or email is in the wrong format'
            actualResult = 'the next page after registration'
            Report.genrateBugReport(id, bugName, datetime.now(
            ), summary, expectedResult, actualResult)
            self.automateRegister.driver.close()
            return

        self.automateRegister.driver.close()
