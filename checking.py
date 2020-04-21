import requests
from validate_email import validate_email


class ValidityCheck:

    @staticmethod
    # First Name must start with capital letter.
    def validateFirstName(firstName):
        if firstName[0].isupper():
            return True
        return False

    @staticmethod
    # Last Name must start with capital letter and can’t be equal First Name.
    def validateLastName(firstName, lastName):
        if ValidityCheck.validateFirstName(lastName):
            if lastName != firstName:
                return True
        return False

    @staticmethod
    # A valid Mobile Number should start with a country code.
    def validateMobileNumber(mobileNumber):
        url = 'http://apilayer.net/api/validate'
        params = {
            'access_key': 'f0c5a94867540173900ef9456dcd5eaa',
            'number': mobileNumber,
            'country_code': '',
            'format': 1
        }

        response = requests.get(url=url, params=params)
        info = response.json()

        if info['valid']:
            return True

        return False

    @staticmethod
    def isUnique(emailSet, emailAdress):
        if emailAdress in emailSet:
            return False
        return True

    @staticmethod
    # Valid E-mail that should be unique for every user.
    def validateEmailAddress(emailSet, emailAddress):
        if validate_email(emailAddress):
            if ValidityCheck.isUnique(emailSet, emailAddress):
                emailSet.add(emailAddress)
                return True
        return False

    @staticmethod
    # Password must have capital letter, small letter, with a limit of 8 characters and confirmed password must be the same.
    def validatePassword(password, confirmedPassword):
        if len(password) < 8:
            if password != password.lower() and password != password.upper() and confirmedPassword == password:
                return True
        return False
