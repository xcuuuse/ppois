# Аудио коллекция

**LogIn** 4 1 -> User, Password

**Authentication** 2 2 -> User

**Comment** 1 1-> 

**Like** 1 0 -> 

**Rating** 1 0 ->

**IdGenerator** 1 1 ->

**AlbumId** 1 1 -> 

**TicketId** 1 1 -> 

**TrackId** 1 1 -> 

**UserId** 1 1 -> 

**Album** 10 1 -> Track, Genre, Label дописать get info

**AlbumDefiner** 0 1 -> Album

**Ep** 5 0 -> Track, Genre, Label

**LiveAlbum** 6 0 -> Track, Genre, Label, City

**Single** 5 0 -> Track, Genre, Label

**StudioAlbum** 5 0 -> Track, Genre, Label

**Artist** 3 2 -> Album

**Band** 3 1 -> Album, Musician

**Concert** 5 1 -> City, Date

**Musician** 3 1 -> 

**Ticket** 2 0 -> Concert, TicketId

**Tour** 4 0 -> Artist, Concert

**TrackLyrics** 1 1 ->

**City** 1 0 ->

**Collaboration** 3 0 -> Genre, Artist

**Cover** 3 0 -> Genre, Artist

**Date** 3 0 ->

**Duration** 1 0 ->

**Genre** 1 1 ->

**Label** 4 1 -> Artist

**Remix** 3 1 -> Genre, Artist

**Track** 7 5 -> Genre, Duration, TrackLyrics, TrackStatistics, Equalizer

**Equalizer** 3 1 -> 

**Queue** 1 5 -> Track

**TrackStatistics** 4 0 -> Like, Comment, Rating

**Collection** 1 1 -> Playlist

**GenreCollection** 3 0 -> Playlist, Genre

**Favourite** 1 2 -> 

**FavouriteTracks** 2 2 -> Playlist, Favourite

**History** 1 1 -> Track

**MediaLibrary** 4 5 -> Playlist, Artist, Album, FavouriteTracks

**Playlist** 6 5 -> Track, History, Queue

**PersonalAccount** 1 2 -> 

**Subscription** 2 2 -> 

**Password** 1 4 -> 

**Username** 1 0 -> 

**UsernameValidator** 1 2 -> Username

**UserProfile** 3 0 -> Date

**User** 11 9 -> Username, Userprofile, MediaLibrary, PersonalAccount, Subscription, Comment, UserId, Like

**PremiumUser** 6 2 -> Username, UserProfile, Subscription, Collection





## Exceptions(12):

**DateError** 1 0 -> 

**EqualizerSettingserror** 1 0 -> 

**InvalidUsernameError** 1 0 -> 

**LogInError** 1 0 -> 

**PlaylistDeletingError** 1 0 -> 

**RatingError** 1 0 -> 

**RegisterError** 1 0 -> 

**ResourcesError** 1 0 -> 

**TicketSellingError** 1 0 -> 

**TrackAddingError** 1 0 -> 

**TypeError** 1 0 -> 

**WeakPasswordError** 1 0 -> 
=======
**LogIn** 4 1 -> User, Password  

**Authentication** 2 2 -> User  

**Comment** 1 1 ->  

**Like** 1 0 ->  

**Rating** 1 0 ->  

**IdGenerator** 1 1 ->  

**AlbumId** 1 1 ->  

**TicketId** 1 1 ->  

**TrackId** 1 1 ->  

**UserId** 1 1 ->  

**Album** 10 5 -> Track, Genre, Label, get info  

**AlbumDefiner** 0 1 -> Album  

**Ep** 5 0 -> Track, Genre, Label  

**LiveAlbum** 6 0 -> Track, Genre, Label, City  

**Single** 5 0 -> Track, Genre, Label  

**StudioAlbum** 5 0 -> Track, Genre, Label  

**Artist** 3 7 -> Album  

**Band** 3 1 -> Album, Musician  

**Concert** 5 1 -> City, Date  

**Musician** 3 1 ->  

**Ticket** 2 3 -> Concert, TicketId  

**Tour** 4 0 -> Artist, Concert  

**TrackLyrics** 1 1 ->  

**City** 1 0 ->  

**Collaboration** 3 0 -> Genre, Artist  

**Cover** 3 0 -> Genre, Artist  

**Date** 3 0 ->  

**Duration** 1 0 ->  

**Genre** 1 1 ->  

**Label** 4 3 -> Artist  

**Remix** 3 1 -> Genre, Artist  

**Track** 7 8 -> Genre, Duration, TrackLyrics, TrackStatistics, Equalizer  

**Equalizer** 3 1 ->  

**Queue** 1 5 -> Track  

**TrackStatistics** 4 11 -> Like, Comment, Rating  

**Collection** 1 1 -> Playlist  

**GenreCollection** 3 0 -> Playlist, Genre  

**Favourite** 1 2 ->  

**FavouriteTracks** 2 2 -> Playlist, Favourite  

**History** 1 1 -> Track  

**MediaLibrary** 4 5 -> Playlist, Artist, Album, FavouriteTracks  

**Playlist** 6 5 -> Track, History, Queue  

**PersonalAccount** 1 2 ->  

**Subscription** 2 2 ->  

**Password** 1 4 ->  

**Username** 1 0 ->  

**UsernameValidator** 1 2 -> Username  

**UserProfile** 3 0 -> Date  

**User** 11 9 -> Username, UserProfile, MediaLibrary, PersonalAccount, Subscription, Comment, UserId, Like  

**PremiumUser** 6 2 -> Username, UserProfile, Subscription, Collection  

## Exceptions (12):

**DateError** 1 0 ->  

**EqualizerSettingserror** 1 0 ->  

**InvalidUsernameError** 1 0 ->  

**LogInError** 1 0 ->  

**PlaylistDeletingError** 1 0 ->  

**RatingError** 1 0 ->  

**RegisterError** 1 0 ->  

**ResourcesError** 1 0 ->  

**TicketSellingError** 1 0 ->  

**TrackAddingError** 1 0 ->  

**TypeError** 1 0 ->  

**WeakPasswordError** 1 0 ->  

**Поля**: 157

**Поведения**: 100

**Ассоциации**: 70

**Исключения**: 12
