class Musician:
    def __init__(self, name: str, instruments: list[str], birth_year: int):
        self.__name = name
        self.__instruments = instruments
        self.__birth_year = birth_year

    @property
    def name(self):
        return self.__name

    @property
    def instruments(self):
        return self.__instruments

    @property
    def birth_year(self):
        return self.__birth_year

    def get_info(self):
        return\
            f"{self.__name}, born in {self.__birth_year}. {", ".join(str(i.title()) for i in self.__instruments)}\n"