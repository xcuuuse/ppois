import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_comment():
    from Community.comment import Comment
    comment = Comment("abc")
    assert str(comment) == "abc"
    comment.edit_comment("xyz")
    assert str(comment) == "xyz"

def test_rating():
    from Community.rating import Rating
    rating = Rating(4)
    assert int(rating) == 4
