class Duration:
    """
    Duration class
    """
    def __init__(self, duration: int):
        """
        Constructor
        :param duration: duration
        """
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration


