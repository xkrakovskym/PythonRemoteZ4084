import random

class Credentials:
    def get_credentials(self, user_id):
        pass


class AWSSignature(Credentials):
    def get_credentials(self, user_id):
        return "98f895231-5145-4556-9887-51f5191"


class BearerToken(Credentials):
    def get_credentials(self, user_id):
        return "1/hkjiah1289124412kaaff123512512jh1521215"


class UserNameAndPasswordCredentials(Credentials):
    def get_credentials(self, user_id):
        return "michalk:mypass123"


class AuthenticationHandler:
    def authenticate(self, credentials):
        pass

    def supports(self, credentials):
        pass


class AWSAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.authenticate_in_aws(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, AWSSignature)

    def authenticate_in_aws(self, credentials):
        return random.randint(1, 3) == 1


class BearerTokenAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_token_valid(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, BearerToken)

    def is_token_valid(self, credentials):
        return random.randint(1, 3) == 1


class UserNameAndPasswordAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_password_valid(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, UserNameAndPasswordCredentials)

    def is_password_valid(self, credentials):
        return random.randint(1, 3) == 1


class ChainAuthenticationElement:
    def __init__(self, authentication_handler, next_handler=None):
        self._authentication_handler = authentication_handler
        self._next_handler = next_handler

    def authenticate(self, credentials):
        if self._authentication_handler.authenticate(credentials):
            print(f"Authenticated by {self._authentication_handler}")
            return True
        elif self._next_handler:
            return self._next_handler.authenticate(credentials)
        else:
            print("All authentication methods used, credentials not authentificated")
            return False

user_name_pass_handler = UserNameAndPasswordAuthenticationHandler()
bear_token_handler = BearerTokenAuthenticationHandler()
aws_signature_handler = AWSAuthenticationHandler()

last_element = ChainAuthenticationElement(aws_signature_handler)
middle_element = ChainAuthenticationElement(bear_token_handler, last_element)
first_element = ChainAuthenticationElement(user_name_pass_handler, middle_element)

request = AWSSignature()

first_element.authenticate(request)