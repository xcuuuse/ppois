class Genre:
    def __init__(self, name: str): # 10
        self.__name = name

    @property
    def name(self):
        return self.__name


class Tag:
    def __init__(self, name: str): # 11
        self.__name = name

    @property
    def name(self):
        return self.__name
