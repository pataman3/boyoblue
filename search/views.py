from django.http import HttpResponseNotFound
from django.shortcuts import render
from boyoblue.media import medias

def search_view(request):
  media = request.GET.get("media")
  query = request.GET.get("q")
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    page = 1

  results = medias.search(media, query, page)

  if results is None:
    return HttpResponseNotFound

  return render(request, 'search/{}.html'.format(media), {
    'results': results,
    'media': media,
    'query': query,
    'page': page,
    'previous_page': page - 1,
    'next_page': page + 1
  })
