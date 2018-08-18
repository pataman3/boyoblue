import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
  client_id=os.environ['SPOTIFY_CLIENT_ID'],
  client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class Artist:
  def __init__(self, name, api_id):
    self.name = name
    self.api_id = api_id


# converts the result of an API call to Song
def parse_api_call(artist):
  return Artist(
    name=artist['name'],
    api_id=artist['id']
  )


def search(query, limit, page):
  artists = []
  for result in sp.search(q=query, limit=limit, type='artist', offset=(page - 1) * limit)['artists']['items']:
    artists.append(parse_api_call(result))
  return artists


def get(api_key):
  return parse_api_call(sp.artist(api_key))
