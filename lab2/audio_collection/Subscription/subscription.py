class Subscription:
    def __init__(self):
        self.__months = 0

    @property
    def months(self):
        return self.__months

    def extend_subscription(self, months: int):
        self.__months += months

    def stop_subscription(self):
        self.__months = 0

