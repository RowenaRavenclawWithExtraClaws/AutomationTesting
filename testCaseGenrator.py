from testCase import TestCase


# A class for generating a single test case for the sign up form.
class TestCaseGenerator:

    @staticmethod
    def generateTestCase(isValidFirstName=True, isValidLastName=True, isValidPhone=True, isValidEmail=True, isValidPassword=True, isValidConfirmedPassword=True, registeredEmail=[]):

        fields = {}
        case = TestCase(isValidFirstName=isValidFirstName, isValidLastName=isValidLastName, isValidPhone=isValidPhone,
                        isValidEmail=isValidEmail, isValidPassword=isValidPassword, isValidConfirmedPassword=isValidConfirmedPassword, registeredEmail=registeredEmail)

        fields['firstname'] = case.firstName
        fields['lastname'] = case.lastName
        fields['phone'] = case.mobileNumber
        fields['email'] = case.emailAddress
        fields['password'] = case.password
        fields['confirmpassword'] = case.confirmedPassword

        return fields
