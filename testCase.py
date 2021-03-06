import random


# A class for generating test cases (text for the text fields of the sign up  form).
class TestCase:
    def __init__(self, isValidFirstName=True, isValidLastName=True, isValidPhone=True, isValidEmail=True, isValidPassword=True, isValidConfirmedPassword=True, registeredEmail=[]):
        self.charPool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/.~=_)(^%$#@!'
        self.numPool = '0123456789'
        self.validPhonePool = ['+201280099665',
                               '+201286845566', '+201005023056', '+201112569887']
        # These emails where generated by an online tool.
        self.validEmailPool = [
            'posotab886@homedepinst.com', 'jojorabbit1918@mailsac.com',
            'verydagger85@mailsac.com', 'themailman1997@mailsac.com',
            'chefcurry@mailsac.com', 'thebeard13@mailsac.com',
            'mjthegoat23@mailsac.com', 'hisairness23@mailsac.com',
            'hakeemthedream33@mailsac.com', 'timduncunfundamentals@mailsac.com',
            'kawhitheclaw@mailsac.com', 'isaacnewton1600@mailsac.com']
        self.firstName = self.generateFirstName(isValidFirstName)
        self.lastName = self.generateLastName(isValidLastName)
        self.mobileNumber = self.generatePhoneNumber(isValidPhone)
        self.emailAddress = self.generateEmail(isValidEmail, registeredEmail)
        self.password = self.generatePassword(isValidPassword)
        self.confirmedPassword = self.generateConfirmedPassword(
            isValidConfirmedPassword)

    def generateFirstName(self, isValid):
        # A list for building the text character by character.
        firstName = []
        firstNameAsString = ''
        indx = 0
        nameLen = random.randrange(3, 15)

        if isValid:
            # Must start with a capital letter.
            indx = random.randrange(0, 26)
            firstName.append(self.charPool[indx])
        else:
            # Must start with a non capital letter or any character.
            indx = random.randrange(26, len(self.charPool))
            firstName.append(self.charPool[indx])

        for i in range(nameLen - 1):
            indx = random.randrange(0, len(self.charPool))
            firstName.append(self.charPool[indx])

        firstNameAsString = ''.join(map(str, firstName))

        return firstNameAsString

    def generateLastName(self, isValid):
        lastName = ''
        # determines if the code would generate a different invalid format or exactly the same valid format to first name.
        coinFlip = random.randrange(0, 1)

        if isValid:
            lastName = self.generateFirstName(isValid)
        else:
            if coinFlip:
                lastName = self.firstName
                return lastName
            else:
                lastName = self.generateFirstName(isValid)

        return lastName

    def generatePhoneNumber(self, isValid):
        # A list for building the number digit by digit.
        # This generator sticks with the Egyption format.
        phoneNumber = []
        phoneNumberAsString = ''
        indx = 0

        if isValid:
            indx = random.randrange(0, len(self.validPhonePool))
            phoneNumberAsString = self.validPhonePool[indx]
            return phoneNumberAsString
        else:
            phoneNumber.append(random.randrange(0, len(self.numPool)))

        for i in range(11):
            indx = random.randrange(0, len(self.numPool))
            phoneNumber.append(self.numPool[indx])

        phoneNumberAsString = ''.join(map(str, phoneNumber))

        return phoneNumberAsString

    def generateEmail(self, isValid, registeredEmail):
        email = []
        emailAsString = ''
        indx = 0
        # determines if the code would generate a different invalid format or an existing email.
        coinFlip = random.randrange(0, 1)
        emailLen = random.randrange(8, 20)

        if isValid:
            for i in range(len(self.validEmailPool)):
                if self.validEmailPool[i] not in registeredEmail:
                    emailAsString = self.validEmailPool[i]
                    return emailAsString

        if coinFlip:
            emailAsString = registeredEmail[0]
            return emailAsString

        for i in range(emailLen):
            indx = random.randrange(0, len(self.charPool))
            email.append(self.charPool[indx])

        emailAsString = ''.join(map(str, email))

        return emailAsString

    def generatePassword(self, isValid):
        password = []
        passwordAsString = ''
        indx = 0
        passwordLen = 0

        if isValid:
            indx = random.randrange(0, 26)
            password.append(self.charPool[indx])
            indx = random.randrange(26, 52)
            password.append(self.charPool[indx])
            passwordLen = random.randrange(0, 7)
        else:
            passwordLen = random.randrange(9, 20)

        for i in range(passwordLen):
            indx = random.randrange(0, len(self.charPool))
            password.append(self.charPool[indx])

        passwordAsString = ''.join(map(str, password))

        return passwordAsString

    def generateConfirmedPassword(self, isValid):
        confirmedPassword = ''

        if isValid:
            confirmedPassword = self.password
        else:
            confirmedPassword = self.generatePassword(isValid)

        return confirmedPassword
