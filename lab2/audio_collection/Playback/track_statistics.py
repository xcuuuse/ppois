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

    def add_stream(self):
        """Increment stream count by 1"""
        self.__streams += 1

    def add_like(self, like: Like):
        """Add a like to the track"""
        self.__likes.append(like)

    def remove_like(self, like: Like):
        """Remove a like from the track"""
        if like in self.__likes:
            self.__likes.remove(like)

    def add_comment(self, comment: Comment):
        """Add a comment to the track"""
        self.__comments.append(comment)

    def remove_comment(self, comment: Comment):
        """Remove a comment from the track"""
        if comment in self.__comments:
            self.__comments.remove(comment)

    def add_rating(self, rating: Rating):
        """Add a rating to the track"""
        self.__ratings.append(rating)

    def clear_stats(self):
        """Reset all statistics"""
        self.__streams = 0
        self.__likes.clear()
        self.__comments.clear()
        self.__ratings.clear()

    def most_recent_comment(self):
        """Return the most recent comment, if any"""
        return self.__comments[-1] if self.__comments else None

    def total_likes(self):
        """Return total number of likes"""
        return len(self.__likes)

    def total_comments(self):
        """Return total number of comments"""
        return len(self.__comments)

    def total_ratings(self):
        """Return total number of ratings"""
        return len(self.__ratings)