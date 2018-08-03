from django.shortcuts import render

def search_list_view(request):
  return render(request, 'search/list.html', {'results': []})
