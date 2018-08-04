import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
  client_id=os.environ['SPOTIFY_CLIENT_ID'],
  client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class Song:
  def __init__(self, name, artist, api_id, album_image):
    self.name = name
    self.artist = artist
    self.api_id = api_id
    self.album_image = album_image


# converts the result of an API call to Song
def parse_api_call(song):
  return Song(
    name=song['name'],
    artist=song['artists'][0]['name'],  # assuming every song has at least one artist
    api_id=song['id'],
    album_image=song['album']['images'][1]['url']  # medium-sized image
  )


def search(query, limit):
  songs = []
  for result in sp.search(q=query, limit=limit)['tracks']['items']:
    songs.append(parse_api_call(result))
  return songs


def get(api_key):
  return parse_api_call(sp.track(api_key))
