from MainEntities.track import Track


class History:
    """
    History class
    """
    def __init__(self):
        self.__tracks: list[Track] = []

    def append(self, track: Track):
        """
        Adds track to history
        :param track: Track to add
        :return: Updated history
        """
        self.__tracks.append(track)

    def __str__(self):
        return f"{[i.title for i in self.__tracks]}"
