class RatingError(Exception):
    """
    Rating error exception
    """
    def __init__(self, message: str):
        super().__init__(message)