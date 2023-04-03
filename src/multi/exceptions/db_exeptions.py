from typing import Any
from . import Error


class DataBaseErrors:
    def specificError(message: Any):
        Error(message)

    def idError():
        Error("Incorrect Format from ID")
