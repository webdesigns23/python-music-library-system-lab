class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            return
        
    @classmethod
    def add_to_artists(cls):
        pass

    @classmethod
    def add_to_genre_count(cls):
        pass

    @classmethod
    def add_to_artists_count(cls):
        pass

