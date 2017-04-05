import webbrowser


class Movie():
    """Here we are using a class Movie for Movie Trailer"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Here we are using a __init__ function" +
          "in which we are passing a parameters"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This show_trailer will show the web site"""
        webbrowser.open(self.trailer_youtube_url)
