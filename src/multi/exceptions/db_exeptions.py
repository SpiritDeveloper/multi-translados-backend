from typing import Any
from . import Error


class DataBaseException:
    def specificError(message: Any):
        Error(message)

    def idError():
        Error("Incorrect Format from ID")
