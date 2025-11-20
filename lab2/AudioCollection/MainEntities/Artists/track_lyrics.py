class TrackLyrics:
    def __init__(self):
        """
        Track lyrics class
        """
        self.__lyrics: str = ""


    @property
    def lyrics(self):
        return self.__lyrics

    def upload_lyrics(self, lyrics: str):
        self.__lyrics = lyrics

