class MoviesLibrary:
    def __init__(self, genres):
        self.data = {genre: [] for genre in genres}

    def add_movie(self, genre, title):
        self.data[genre].append(title)

    def recommend(self, genre):
        return self.data[genre]
