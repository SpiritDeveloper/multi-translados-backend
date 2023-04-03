from . import Error


class AuthErrors:
    def tokenNotFound():
        Error("no valid token was found in the request")

    def invalidToken():
        Error("your token is invalid, please log in again")

    def bearerNotFound():
        Error("it is necessary to send the word bearer before the token")

    def environmentVariablesNotFound():
        Error("no environment variables were set, contact your administrator")
