class Audiofile:
    def __init__(self, name: str, file_path: str, duration: int, audio_format: str, size: int):
        self.__name = name
        self.__file_path = file_path
        self.__duration = duration
        self.__audio_format = audio_format
        self.__size = size

    @property
    def name(self):
        return self.__name

    @property
    def file_path(self):
        return self.__file_path

    @property
    def duration(self):
        return self.__duration

    @property
    def audio_format(self):
        return self.__audio_format

    @property
    def size(self):
        return self.__size

    def change_format(self, new_format):
        self.__audio_format = new_format

    def get_duration_formated(self):
        minutes = self.duration // 60
        seconds = self.duration - ((self.duration // 60) * 60)
        if seconds < 10:
            return f"{minutes}:0{seconds}"
        return f"{minutes}:{seconds}"

    def get_size_formated(self):
        if self.size < 1000:
            return f"{self.size}B"
        elif 1000 <= self.size <= 10 ** 6:
            return f"{self.size / 1000}Kb"
        else:
            return f"{self.size / 10 ** 6}Mb"

    def get_info(self):
        return (f"File: {self.name}, Duration: {self.get_duration_formated()}, "
                f"Format: {self.audio_format}, Size: {self.get_size_formated()}")


class Metadata:
    def __init__(self, title: str, artist: str, album: str, year: int): #9
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def artist(self):
        return self.__artist

    @property
    def album(self):
        return self.__album

    @property
    def year(self):
        return self.__year

    def get_info(self):
        return f"{self.title} - {self.artist} | {self.album} | {self.year}"




