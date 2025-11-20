import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MainEntities.genre import Genre
from MainEntities.Albums.album_definer import AlbumDefiner
from MainEntities.Artists.musician import Musician
from MainEntities.track import Track, TrackLyrics
from MainEntities.Albums.album import Album
from MainEntities.Albums.live_album import LiveAlbum
from MainEntities.Artists.band import Band
from MainEntities.Albums.single import Single
from MainEntities.label import Label
from MainEntities.duration import Duration


def test_city():
    from MainEntities.city import City
    first_city = City("Minsk")
    assert first_city.city == "Minsk"


def test_album():
    label = Label("Warner Records")
    track1 = Track("Papercut", Genre("nu metal"))
    track2 = Track("One Step Closer", Genre("nu metal"))
    album = Album("Hybrid Theory", [track1, track2], Genre("nu metal"), 2000, label)
    assert album.title == "Hybrid Theory"
    assert album.genre == "nu metal"
    assert [i.title for i in album.tracks] == ["Papercut", "One Step Closer"]
    assert album.year == 2000
    assert album.label.name == "Warner Records"

def test_album_definer():
    label = Label("Warner Records")
    track1 = Track("Papercut", Genre("nu metal"))
    track2 = Track("One Step Closer", Genre("nu metal"))
    track3 = Track("a", None)
    track4 = Track("b", None)
    album = Album("Hybrid Theory", [track1, track2], Genre("nu metal"), 2000, label)
    definer = AlbumDefiner.define(album)
    from MainEntities.Albums.single import Single
    assert isinstance(definer, Single)
    album2 = Album("album", [track1, track2, track3, track4], None, 2001, label)
    definer2 = AlbumDefiner.define(album2)
    from MainEntities.Albums.ep import Ep
    assert isinstance(definer2, Ep)


def test_genre():
    genre = Genre("nu metal")
    assert genre.genre_name == "nu metal"


def test_duration():
    duration = Duration(180)
    assert duration.duration == 180


def test_musician():
    musician = Musician("James Hetfield")
    assert musician.name == "James Hetfield"
    assert musician.birth_year == 0
    assert musician.instruments == []


def test_lyrics():
    lyrics = TrackLyrics()
    lyrics.upload_lyrics("abc")
    assert lyrics.lyrics == "abc"


def test_track():
    from Exceptions.equalizer_settings_error import EqualizerSettingsError
    track = Track("In the End", Genre("nu metal"))
    assert track.title == "In the End"
    assert track.genre.genre_name == "nu metal"
    track.add_lyrics("i tried so hard and got so far")
    assert track.lyrics == "i tried so hard and got so far"
    assert track.formated_duration() == "0:00"
    with pytest.raises(EqualizerSettingsError):
        track.adjust_equalizer(4, 2, -1)

def test_live_album():
    label = Label("Warner Records")
    track1 = Track("Papercut", Genre("nu metal"))
    track2 = Track("One Step Closer", Genre("nu metal"))
    live_album = LiveAlbum("Live in Texas", [track1, track2], Genre("nu metal"),
                           2004, label, "Dallas")
    assert live_album.title == "Live in Texas"
    assert live_album.year == 2004
    assert live_album.genre == "nu metal"
    assert [i.title for i in live_album.tracks] == ["Papercut", "One Step Closer"]
    assert live_album.city == "Dallas"


def test_band():
    label = Label("Warner Records")
    albums = [Album("Hybrid Theory", [], Genre("nu metal"), 2000, label)]
    band = Band("Linkin Park", albums, [Musician("Mike Shinoda")])
    assert band.name == "Linkin Park"
    assert band.albums == albums


def test_label():
    label = Label("Warner Records")
    assert label.name == "Warner Records"


def test_single():
    single = Single("Single", [Track("Papercut",  Genre("nu metal"))],
                    Genre("nu metal"), 2000, Label("Warner Records"))
    assert single.label.name == "Warner Records"
    assert [i.normalized_name for i in single.tracks] == ["papercut"]

def test_lives():
    from MainEntities.Artists.concert import Concert
    from MainEntities.Artists.artist import Artist
    from MainEntities import city, date
    from MainEntities.Artists.ticket import Ticket
    from MainEntities.Artists.tour import Tour
    artist = Artist("Name", [])
    concert = Concert(artist, 123, city.City("NY"), date.Date(12, 12, 2025))
    assert concert.date.month == 12
    assert concert.city.city == "NY"
    assert concert.artist.name == "Name"
    ticket = Ticket(concert)
    assert ticket.ticket_id == 1
    assert ticket.concert.artist == artist
    concert2 = Concert(artist, 124, city.City("LA"), date.Date(13, 12, 2025))
    tour = Tour(artist, [concert, concert2])
    assert tour.ticket_amount == 247
    assert [i.city for i in tour.cities] == ["NY", "LA"]

def test_track_types():
    from MainEntities.Artists.artist import Artist
    from MainEntities.collaboration import Collaboration
    from MainEntities.cover import Cover
    from MainEntities.genre import Genre
    from MainEntities.duration import Duration
    from MainEntities.remix import Remix
    artists = [Artist("1", []), Artist("2", [])]
    collab = Collaboration("Collab", Genre("rock"), artists)
    assert collab.genre.genre_name == "rock"
    assert collab.artists == artists
    assert collab.normalized_name == "collab"
    track = Track("title", Genre("metal"))
    cover = Cover("title cover", Genre("pop"), Artist("1", []))
    assert cover.cover_author.name == "1"
    assert cover.genre.genre_name == "pop"
    remix = Remix("title remix", Genre("metal"), Artist("2", []))
    assert remix.title == "title remix"
    assert remix.author.albums == []
