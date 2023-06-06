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
        Song.count += 1
        Song.genres.append(self.genre)
        Song.artists.append(self.artist)
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1
