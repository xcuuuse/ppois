from audio.base import Audiofile
from audio.base import Metadata
"""class Track(Audiofile):
    def __init__(self, name: str, file_path: str, duration: int, audio_format: str, size: int,
                 title: str, artist: str, album: str, year: int, genre: str):
        super().__init__(name, file_path, duration, audio_format, size)
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre

    def get_info(self):
        return f"{self.title}({self.artist}) | {self.album} | {self.year} | {self.genre}"


class Podcast(Audiofile):
    def __init__(self, name: str, file_path: str, duration: int, audio_format: str, size: int,
                 podcaster: str, episode: int, title: str):
        super().__init__(name, file_path, duration, audio_format, size)
        self.podcaster = podcaster
        self.episode = episode
        self.title = title

    def get_info(self):
        return f"{self.podcaster}, {self.episode}: {self.title}"""

file = Audiofile("a", "a/a", 123, ".mp3", 1024)
print(file.get_info())
file.change_format(".wav")
print(file.get_info())