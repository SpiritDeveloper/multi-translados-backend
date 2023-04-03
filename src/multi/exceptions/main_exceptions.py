from . import Error


class CrmError:
    def notFoundConfigurationBussinesUnit():
        Error("Bussines unit setting not found")

    def invalidCredentialsOrUrl():
        Error("Invalid credentials or url to crm settings")

    def notInsert():
        Error("Crm not inserted")

    def requestError():
        Error("Request or service sent to the crm had a problem")

    def requestErrors(message: str):
        Error(message)
