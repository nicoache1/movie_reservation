class AuthException(Exception):
    """Exception raised when an User is not found or password is incorrect."""


class InvalidTokenException(Exception):
    """Exception raised when an invalid token is provided."""
