# Lee Farretta's movie project
# version 1.0
# November 16, 2016
#
# In this file, we define the class Movie. This class definition is used as the
# data structure for the movies table and the movies website.  Here we import
# webbrowser and use show_trailer in order to launch the trailer_youtube when the
# website is rendered.
#
import webbrowser
#
# This class provides a way to store movie related information.  When __init__
# runs it creates an instance of class Movie and sets aside instance variable space in
# memory to store the instance data from the movies table.  Since there are 6 movies
# defined in entertainment-center.py, 6 intances of intance variable space will be
# created.
#
class Movie():
    def __init__(self,movie_title,movie_storyline,poster,trailer_youtube,release):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer_youtube
        self.release_date=release

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
