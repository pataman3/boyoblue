import os
from tmdbv3api import TMDb, TV

tmdb = TMDb()
tmdb.api_key = os.environ['TMDB_API_KEY']

tv = TV()

class Television:
  def __init__(self, title, api_id, poster_image):
    self.title = title
    self.api_id = api_id
    self.poster_image = poster_image


# converts the result of an API call to a Movie object
def parse_api_call(show):
  return Television(
    title=show.name,
    api_id=show.id,
    poster_image='https://image.tmdb.org/t/p/w200/' + show.poster_path if show.poster_path is not None else ''
  )


def search(query, limit, page):
  shows = []
  for result in tv.search(query, page=page)[:limit]:
    shows.append(parse_api_call(result))
  return shows


def get(api_key):
  return parse_api_call(tv.details(api_key))
