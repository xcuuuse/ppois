from Base.Albums.album import Album


class Artist:
    def __init__(self, name: str, albums: list[Album]):
        self._name = name
        self._albums = albums

    @property
    def name(self):
        return self._name

    @property
    def albums(self):
        return self._albums
