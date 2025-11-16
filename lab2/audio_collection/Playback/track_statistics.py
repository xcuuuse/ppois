from Community.comment import Comment
from Community.like import Like
from Community.rating import Rating


class TrackStatistics:
    """
    Track statistics class
    """
    def __init__(self):
        self.__streams = 0
        self.__likes: list[Like] = []
        self.__comments: list[Comment] = []
        self.__ratings: list[Rating] = []

    @property
    def streams(self): return self.__streams

    @property
    def likes(self): return self.__likes

    @property
    def comments(self): return self.__comments

    @property
    def ratings(self): return self.__ratings

    @property
    def rating(self): return sum(self.__ratings) / len(self.__ratings)

    @property
    def stats(self):
        """
        Shows the track stats
        :return: track statistics as str
        """
        return {"plays": self.__streams, "likes": self.__likes, "rating": self.rating,
                "comments": self.__comments}

