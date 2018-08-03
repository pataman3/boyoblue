from django.shortcuts import render
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def search_list_view(request):
  media = request.GET.get("media")
  query = request.GET.get("q")

  results = []
  if media == 'Music':
    client_credentials_manager = SpotifyClientCredentials(
      client_id=os.environ['SPOTIFY_CLIENT_ID'],
      client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    for raw_result in sp.search(q=query, limit=10)['tracks']['items']:
      results.append({
        'name': raw_result['name'],
        'artist': raw_result['artists'][0]['name'],  # assuming every song has at least one artist
        'api_id': raw_result['id']
      })

  return render(request, 'search/list.html', {'media': media, 'results': results})
