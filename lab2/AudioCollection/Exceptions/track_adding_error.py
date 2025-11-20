class TrackAddingError(Exception):
    """
    Track adding error exception
    """
    def __init__(self, message: str):
        super().__init__(message)

