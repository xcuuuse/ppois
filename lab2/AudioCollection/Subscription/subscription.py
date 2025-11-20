class Subscription:
    """
    Subscription class
    """
    def __init__(self, months: int):
        """
        Constructor
        :param months: Subscription months
        """
        self.__months = months
        self.__month_cost = 10

    @property
    def months(self):
        return self.__months

    @property
    def month_cost(self):
        return self.__month_cost

    def extend_subscription(self, months: int):
        """
        Extend subscription
        :param months: Months to extend subscription
        :return:
        """
        self.__months += months

    def stop_subscription(self):
        """
        Stops the subscription
        """
        self.__months = 0


