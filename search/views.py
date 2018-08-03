from django.http import HttpResponseNotFound
from django.shortcuts import render
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def search_view(request):
  media = request.GET.get("media")
  query = request.GET.get("q")

  if media == 'Music':
    return search_songs_view(request, query)
  elif media == 'movies':
    return search_movies_view(request, query)
  else:
    return HttpResponseNotFound

def search_songs_view(request, query):

  songs = []

  client_credentials_manager = SpotifyClientCredentials(
    client_id=os.environ['SPOTIFY_CLIENT_ID'],
    client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
  )

  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
  for raw_result in sp.search(q=query, limit=10)['tracks']['items']:
    songs.append({
      'name': raw_result['name'],
      'artist': raw_result['artists'][0]['name'],  # assuming every song has at least one artist
      'api_id': raw_result['id']
    })

  return render(request, 'search/songs.html', {'songs': songs})


def search_movies_view(request, query):
  return render(request, 'search/movies.html')

