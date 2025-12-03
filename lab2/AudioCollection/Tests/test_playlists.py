import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_playlist():
    from Playlists.playlist import Playlist
    from MainEntities.track import Track
    track1 = Track("In the end", None)
    track2 = Track("Numb", None)
    playlist = Playlist("LP Tracks")
    playlist.add_track(track2)
    playlist.add_track(track1)
    assert playlist.playlist_tracks() == ["Numb", "In the end"]
    playlist.delete_track(track1)
    assert playlist.playlist_tracks() == ["Numb"]
    assert playlist.get_formated_duration() == "0:00"

def test_favourite():
    from Playlists.favourite import Favourite
    from MainEntities.Artists.artist import Artist
    from MainEntities.Albums.album import Album

    fav = Favourite()
    album = Album("Meteora", [], None, 2003, None)
    fav.add(album)
    fav.add(Artist("Linkin Park", [album]))


def test_media():
    from Playlists.media_library import MediaLibrary
    from MainEntities.Albums.album import Album
    from MainEntities.track import Track
    track1 = Track("Dont stay", None)
    album = Album("Meteora", [track1], None, 2003, None)
    media = MediaLibrary()
    media.add_to_library(album)
    media.add_favourite_track(track1)
    assert media.albums == [album]
    assert media.favourite_tracks == [track1]
    album2 = Album("Nevermind", [], None, 1991, None)
    album3 = Album("Fallen", [], None, 2003, None)
    media.add_to_library(album2)
    media.add_to_library(album3)
    media.pin_album(album2)
    assert media.albums == [album2, album, album3]

def test_genre_collection():
    from MainEntities.genre import Genre
    from Playlists.playlist import Playlist
    from MainEntities.track import Track
    from Playlists.Collections.genre_collection import GenreCollection
    track1 = Track("track1", Genre("rock"))
    track2 = Track("track2", Genre("pop"))
    track3 = Track("track3", Genre("rock"))

    playlist = Playlist("Tracks")
    playlist.add_track(track1)
    playlist.add_track(track2)
    playlist.add_track(track3)

    collection = GenreCollection(playlist, Genre("rock"))
    assert collection.tracks == [track1, track3]
    assert collection.genre.genre_name == "rock"

