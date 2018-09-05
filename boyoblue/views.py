from django.shortcuts import render

def about(request):
  return render(request, 'boyoblue/about.html')
