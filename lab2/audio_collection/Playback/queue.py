from Base.track import Track


class Queue:
    def __init__(self):
        self.__queue = []

    def add_to_queue(self, track: Track, current: Track | None):
        if current is None:
            self.__queue.append(track)
            return
        try:
            index = next(i for i, t in enumerate(self.__queue) if t.track_id == current.track_id)
            self.__queue.insert(index + 1, track)
        except StopIteration:
            self.__queue.insert(0, track)

    def remove_from_queue(self, track: Track):
        self.__queue = [i for i in self.__queue if i.track_id != track.track_id]

    def queue_next(self):
        if not self.__queue:
            return None
        return self.__queue.pop(0)

    def clear_queue(self):
        self.__queue.clear()

    def show_queue(self):
        return [i.title for i in self.__queue]

    def __len__(self):
        return len(self.__queue)