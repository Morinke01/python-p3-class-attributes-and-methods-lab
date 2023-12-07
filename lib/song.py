class Song:
    all = []
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_all(self)
        Song.add_one_to_count()
        Song.add_genre(self.genre)
        Song.add_artist(self.artist)

    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)

    @classmethod
    def add_one_to_count(cls):
        cls.count += 1

    @classmethod
    def add_genre(cls, genre):
        cls.genres.add(genre)
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_artist(cls, artist):
        cls.artists.add(artist)
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
