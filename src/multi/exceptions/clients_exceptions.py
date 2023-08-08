from . import Error


class ClientException:
    def notFound():
        Error("the client was not found or is disabled")

    def existingClient():
        Error("the client is already registered")

    def notCreated():
        Error("There was a problem creating the client. Please contact the administrator")

    def notUpdated():
        Error("there was a problem updating the client. Please contact the administrator")

    def notDeleted():
        Error("there was a problem deleting the client. Please contact the administrator")