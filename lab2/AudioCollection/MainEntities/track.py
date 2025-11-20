from MainEntities.genre import Genre
from IdManage.track_id import TrackId
from MainEntities.Artists.track_lyrics import TrackLyrics
from Community.rating import Rating
from MainEntities.duration import Duration
from Playback.equalizer import Equalizer
from Playback.track_statistics import TrackStatistics


class Track:
    """
    Track base class
    """
    def __init__(self, title: str, genre: Genre):
        """
        Constructor
        :param title: Track title
        :param genre: Track genre
        """
        self.__title = title
        self.__duration: Duration = Duration(0)
        self.__genre = genre
        self.__track_id = TrackId.generate_id()
        self.__lyrics = TrackLyrics()
        self.__statistics = TrackStatistics()
        self.__equalizer = Equalizer()

    @property
    def title(self):
        return self.__title

    @property
    def duration(self):
        return self.__duration.duration

    @property
    def genre(self):
        return self.__genre

    @property
    def track_id(self):
        return self.__track_id

    @property
    def lyrics(self):
        return self.__lyrics.lyrics

    @property
    def normalized_name(self):
        """
        A method to get track name as:
        "Track Name" -> "trackname"
        :return: Normalized track name
        """
        import re
        return re.sub(r'[^a-zA-Z0-9]', '', self.__title).lower()

    @property
    def statistics(self):
        return self.__statistics.stats

    @property
    def equalizer(self):
        return self.__equalizer

    @property
    def likes(self): return len(self.__statistics.likes)

    def adjust_equalizer(self, bass=None, mid=None, treble=None):
        """
        A method to set the equalizer settings
        :param bass: Bass
        :param mid: Mid
        :param treble: Treble
        :return: Equalizer with set settings
        """
        self.__equalizer.adjust(bass, mid, treble)

    def formated_duration(self):
        """
        A method to get track duration as minutes:seconds
        :return: track formated duration
        """
        total_seconds = self.__duration.duration
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"

    def add_lyrics(self, lyrics: str):
        """
        Adds track lyrics
        :param lyrics: Lyrics to add
        :return: Updated track lyrics
        """
        self.__lyrics.upload_lyrics(lyrics)

    def add_comment(self, text):
        """
        Adds comment to the track
        :param text: Comment
        :return: Updated statistics
        """
        from Community.comment import Comment
        self.__statistics.comments.append(Comment(text))

    def add_rate(self, rate: int):
        """
        Adds a rate to track
        :param rate: Rate from 1 to 5
        :return: Track rating
        """
        self.__statistics.ratings.append(Rating(rate))

    def play(self):
        """
        Simulates playing the track
        :return: String with track playback info
        """
        return f"Playing track: {self.__title}"

    def add_like(self):
        """
        Adds a like to the track
        """
        self.__statistics.likes.append(1)

    def get_total_comments(self):
        """
        Returns the total number of comments for the track
        :return: Number of comments
        """
        return len(self.__statistics.comments)