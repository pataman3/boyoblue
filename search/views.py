from django.http import HttpResponseNotFound
from django.shortcuts import render
from boyoblue.media import medias

def search_view(request):
  media = request.GET.get("media")
  query = request.GET.get("q")
  results = medias.search(media, query)

  if results is None:
    return HttpResponseNotFound

  return render(request, 'search/{}.html'.format(media), {'results': results})
