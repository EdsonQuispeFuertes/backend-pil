"""This module contains a enum class."""
from enum import Enum


class StatusCode(Enum):
    """This class gives value to status codes."""
    OK = 200  # exists
    CREATED = 201  # when something is created
    BAD_REQUEST = 400  # incorrect request
    NOT_FOUND = 404
    UNAUTHORIZED = 401  # Unauthorized


class AccountStatus(Enum):
    """This class gives value from tables."""
    BANNED = 0
    NORMAL = 1
