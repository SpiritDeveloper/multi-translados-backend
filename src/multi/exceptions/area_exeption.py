from . import Error


class AreaException:
    def notFound():
        Error("the area not found or are disable")

    def existingArea():
        Error("the area is already registered")

    def notCreated():
        Error("there was a problem when creating the area, contact the administrator")

    def notUpdated():
        Error("there was a problem when updating the area, contact the administrator")

    def notDeleted():
        Error("there was a problem when deleting the area, contact the administrator")

    