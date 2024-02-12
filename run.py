from api import filter_movies, movies
from api import beautify


print(beautify(filter_movies(movies, 'de', 5)))