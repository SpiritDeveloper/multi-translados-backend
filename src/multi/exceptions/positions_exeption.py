from . import Error


class PositionException:
    def notFound():
        Error("the position not found or are disable")

    def existingArea():
        Error("the position is already registered")

    def notCreated():
        Error("there was a problem when creating the position, contact the administrator")

    def notUpdated():
        Error("there was a problem when updating the position, contact the administrator")

    def notDeleted():
        Error("there was a problem when deleting the position, contact the administrator")

    