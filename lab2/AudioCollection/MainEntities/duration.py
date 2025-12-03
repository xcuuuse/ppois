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

    def __int__(self):
        return self.__duration


