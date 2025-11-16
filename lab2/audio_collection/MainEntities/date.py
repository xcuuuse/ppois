class Date:
    """
    Date class
    """
    def __init__(self, year: int, month: int, day: int):
        """
        Constructor
        :param year: Year
        :param month: Month
        :param day: Day
        """
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
