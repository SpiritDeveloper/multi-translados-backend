from . import Error


class SecurityException:
    def userExist():
        Error("email allready exist in the system")

    def notFoundUser():
        Error("incorrect email or password, verify your information")

    def notCreatedToken():
        Error("token could not be generated, contact administrator")

    def userNotCreated():
        Error("user not created, contact administrator")