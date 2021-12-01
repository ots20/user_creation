import random
import string
import unittest
import requests


def validate_string():
    while True:
        value = input('How many users do you want to create? (from 1 to 5): ')
        try:
            number = int(value)
            assert 5 >= number > 0
            return number
        except ValueError:
            print("type a number equal or below 5")
        except AssertionError:
            print("Assertion type a number equal or below 5")


class TestUserManagement(unittest.TestCase):

    def setUp(self):
        # REMEMBER THE ENVIRONMENT!!!!
        self.environment = 'xss'
        self.endpoint = 'https://staging:IdQUaMsyRMBO@dev.z-dn.net/graphql/{}?content-type=application/json'.format(self.environment)

    def test_create_user(self):
        letters = string.digits
        email_number = ''.join(random.choice(letters) for i in range(3))
        body = {
            "operationName": "registerUser",
            "variables": {
                "nick": "xanovaut{}".format(email_number),
                "country": "US",
                "entry": "1",
                "email": "otsfake7+xanovaut{}@gmail.com".format(email_number),
                "password": "test123",
                "dateOfBirth": "2000-01-01",
                "acceptedTermsOfService": True,
                "accountType": "STUDENT"
            },
            "query": "mutation registerUser($nick: String!, $dateOfBirth: String!, $country: String!, $email: String, "
                     "$password: String, $parentEmail: String, $acceptedTermsOfService: Boolean, $referrer: String, "
                     "$entry: String, $accountType: AccountType) {\n register(input: {nick: $nick, dateOfBirth: "
                     "$dateOfBirth, country: $country, email: $email, password: $password, parentEmail: $parentEmail, "
                     "acceptedTermsOfService: $acceptedTermsOfService, referrer: $referrer, entry: $entry, "
                     "accountType: $accountType}) {\n token\n pendingToken\n validationErrors {\n type\n error\n "
                     "path\n __typename\n }\n __typename\n }\n}\n "
        }
        response = requests.post(self.endpoint, json=body)
        if response.status_code == 200:
            self.created_user = body["variables"]["nick"]
            # print(self.created_user)
            return self.created_user
        else:
            print("Request failed, response code: {}".format(response.status_code))
            print(response.content)

    def test_bulk_user_creation_alternative_B(self):
        user_list = []
        validation = validate_string()
        print("Creating {} user(s)".format(validation))
        for x in range(validation):
            self.test_create_user()
            user_list.append(self.created_user)
        print(user_list)

    def test_method(self):
        print("just a test")
