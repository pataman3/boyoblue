import os
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = os.environ['TMDB_API_KEY']

movie = Movie()

class Movie:
  def __init__(self, title, api_id, poster_image):
    self.title = title
    self.api_id = api_id
    self.poster_image = poster_image


# converts the result of an API call to a Movie object
def parse_api_call(movie):
  return Movie(
    title=movie.title,
    api_id=movie.id,
    poster_image='https://image.tmdb.org/t/p/w200/' + movie.poster_path if movie.poster_path is not None else ''
  )


def search(query, limit, page):
  movies = []
  for result in movie.search(query, page=page)[:limit]:
    movies.append(parse_api_call(result))
  return movies


def get(api_key):
  return parse_api_call(movie.details(api_key))
