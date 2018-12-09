# Lee Farretta's movie project
# version 1.0
# November 16, 2016
#
# Here we have 6 instances of the class Movie.  The class definition is defined
# in media.py.  These are some of Lee's favorite movies.  The 6 instances of
# class Movie are shown in the Python table below:
#
# movies=[french_connection,italian_job,the_good_the_bad_and_the_ugly,
# schindlers_list,star_wars,doctor_zhivago]
#
# After you run this code, you should be able to open the file
# fresh_tomatoes.html and see the movie posters, the names of the movies and
# their release dates on a fully functioning web page.  Their trailers should
# also play if you click on the movie posters.
#
# When this code runs it uses the class definition in media.py and the
# open_movies_page function in fresh_tomatoes.py along with the html styles and
# scripts found there to render the web page.  This is why we import
# fresh_tomatoes and media here.
#
import fresh_tomatoes
import media
#
# Here we define the 6 object intances for class Movie.  When __init__ runs in
# media.py, the constructor allocates memory space for the 6 sets of instance
# variables that will contain the data below.
#
french_connection = media.Movie(
    'The French Connection',
    'Violence, revenge, intrigue and $32 million in smuggled heroin!',
    'https://upload.wikimedia.org/wikipedia/en/b/b8/TheFrenchConnection.jpg',
    'https://https://www.youtube.com/watch?v=_CKuk_-cep0',
    'October 9, 1971')

the_good_the_bad_and_the_ugly = media.Movie(
    'The Good, the Bad and the Ugly',
    'A post-civil war, spaghetti western about three men after some gold.',
    'https://goo.gl/69LtYW',
    'https://www.youtube.com/watch?v=WCN5JJY_wiA',
    'December 29, 1967')

italian_job = media.Movie(
    'Italian Job',
    'A story of theft, murder, revenge and $35 million in gold.',
    'http://fontmeme.com/images/The-Italian-Job-Poster.jpg',
    'https://www.youtube.com/watch?v=5Eyw-Qiwpj0',
    'May 30, 2003')

schindlers_list = media.Movie(
    '''Schindler's List''',
    'Horror, exploitation and redemption in the face of Nazi deparvity.',
    'https://i.jeded.com/i/schindlers-list.22323.jpg',
    'https://www.youtube.com/watch?v=ShIjgYmYbWc',
    'December 15, 1993')

star_wars = media.Movie(
    'Star Wars',
    'A space adventure with heroes, villains, aliens and the force.',
    'https://www.cinemasterpieces.com/cinest5.jpg',
    'https://www.youtube.com/watch?v=1g3_CFmnU7k',
    'May 25, 1977')

doctor_zhivago = media.Movie(
    'Doctor Zhivago',
    'An epic love story set againts the chaos of the Russian revolution.',
    'https://upload.wikimedia.org/wikipedia/en/6/64/DrZhivago_Asheet.jpg',
    'https://www.youtube.com/watch?v=M1iQ5hQTR5s',
    'December 31, 1965')
#
# Here the movies table that is fed into the open_movies_page funtion in
# fresh_tomatoes.py is defined and opened.
#
movies = [
    french_connection,
    italian_job,
    the_good_the_bad_and_the_ugly,
    schindlers_list,
    star_wars,
    doctor_zhivago]
fresh_tomatoes.open_movies_page(movies)
