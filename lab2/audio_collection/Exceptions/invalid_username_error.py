class InvalidUsernameError(Exception):
    """
    Invalid username error exception
    """
    def __init__(self, message: str):
        super().__init__(message)