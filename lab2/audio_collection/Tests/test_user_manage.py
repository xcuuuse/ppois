import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_username():
    from UserManage.username import Username
    name = Username("first_user")
    assert name.username == "first_user"


def test_username_validator():
    from UserManage.username import Username
    from UserManage.username_validator import UsernameValidator
    wrong_username = Username("third_user!@")
    valid = UsernameValidator(wrong_username)
    assert not valid.is_valid(wrong_username)


def test_user_profile():
    from UserManage.user_profile import UserProfile
    from MainEntities.date import Date
    profile = UserProfile("bio", Date(2000, 1, 1), "Belarus")
    assert profile.birthdate.month == 1
    assert profile.bio == "bio"
    assert str(profile) == "bio. Belarus. 1.1.2000"


def test_password():
    from UserManage.password import Password
    password = Password("my_password_123!")
    assert str(password) == "****************" #16 symbols
    password.change("my_password_123!", "n3w_password$$")
    assert str(password) == "**************" #14 symbols


def test_user():
    from UserManage.user import User
    from UserManage.username import Username
    from MainEntities.Artists.artist import Artist
    from UserManage.user_profile import UserProfile
    from MainEntities.date import Date
    from MainEntities.track import Track
    from Exceptions.rating_error import RatingError
    username = Username("fourth_user")
    profile = UserProfile("bio", Date(2000, 1, 1), "Belarus")
    user = User(username, profile)
    artist = Artist("artist", [])
    user.like(artist)
    assert user.media.artists == [artist]
    track = Track("track", None)
    user.like(track)
    assert user.favourite_tracks == [track]
    user.add_to_amount(100)
    assert user.amount == 100
    import pytest
    with pytest.raises(RatingError):
        user.rate_track(track, -1)


def test_premium_user():
    from UserManage.user import User
    from UserManage.username import Username
    from UserManage.user_profile import UserProfile
    from MainEntities.date import Date
    from UserManage.premium_user import PremiumUser
    username = Username("fourth_user")
    profile = UserProfile("bio", Date(2000, 1, 1), "Belarus")
    user = User(username, profile)
    user.add_to_amount(1000)
    prem_user = user.buy_subscription(6)
    assert isinstance(prem_user, PremiumUser)

