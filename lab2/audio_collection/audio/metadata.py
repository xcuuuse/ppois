class Genre:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Tag:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name
