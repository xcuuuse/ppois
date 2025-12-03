from MainEntities.track import Track

class Queue:
    """
    Queue class
    """
    def __init__(self):
        self.__queue = []

    def add_to_queue(self, track: Track):
        """
        Adds track to queue
        :param track: Track to add
        :return: Updated queue
        """
        self.__queue.append(track)

    def remove_from_queue(self, track: Track):
        """
        Removes track from queue
        :param track: Track to remove
        :return: Updated queue
        """
        self.__queue = [i for i in self.__queue if i.track_id != track.track_id]

    def queue_next(self):
        """
        Skips the track
        """
        if not self.__queue:
            return None
        return self.__queue.pop(0)

    def clear_queue(self):
        """
        Clears all queue
        :return: Updated queue
        """
        self.__queue.clear()

    def show_queue(self):
        """
        Shows tracks in queue
        :return: Updated queue
        """
        return [i.title for i in self.__queue]

    def __len__(self):
        return len(self.__queue)
