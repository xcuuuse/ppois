import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_queue():
    from Playback.queue import Queue
    from MainEntities.track import Track
    queue = Queue()
    track1 = Track("track1", None)
    track2 = Track("track2", None)
    track3 = Track("track3", None)
    queue.add_to_queue(track1)
    queue.add_to_queue(track3)
    assert queue.show_queue() == ["track1", "track3"]


