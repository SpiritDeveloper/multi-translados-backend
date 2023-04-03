from . import Error


class SignInErrors:
    def notFoundUser():
        Error("incorrect email or password, verify your information")

    def notCreatedToken():
        Error("token could not be generated, contact administrator")