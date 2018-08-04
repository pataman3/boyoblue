from django.http import HttpResponseNotFound
from django.shortcuts import render
from boyoblue.media import songs, movies

def search_view(request):
  media = request.GET.get("media")
  query = request.GET.get("q")

  if media == 'songs':
    return render(request, 'search/songs.html', {'songs': songs.search(query, limit=10)})
  elif media == 'movies':
    return render(request, 'search/movies.html', {'movies': movies.search(query, limit=10)})
  else:
    return HttpResponseNotFound
