class Genre:
    def __init__(self, genre_name: str):
        self.__genre_name = genre_name

    @property
    def genre_name(self):
        return self.__genre_name

