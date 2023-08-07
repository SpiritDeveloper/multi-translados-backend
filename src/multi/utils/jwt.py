from dotenv import load_dotenv
from jwt import encode, decode, exceptions
from os import getenv
from ..exceptions.auth_exeptions import AuthException
import logging

load_dotenv()


class Jwt:
    def __init__(self):
        self.secret = getenv("SECRET_KEY")
        self.algorith = getenv("ALGORITHM")

    def encode(self, user):
        try:
            if not self.secret or not self.algorith:
                AuthException.environmentVariablesNotFound()
            return encode(user, self.secret, algorithm=self.algorith)
        except exceptions.InvalidTokenError as error:
            logging.warning(str(error))

    def decode(self, token: str):
        try:
            if not self.secret or not self.algorith:
                AuthException.environmentVariablesNotFound()
            return decode(token, self.secret, algorithms=[self.algorith])
        except exceptions.DecodeError as error:
            logging.warning(str(error))
