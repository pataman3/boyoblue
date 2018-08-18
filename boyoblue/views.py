from django.shortcuts import render

def about(request):
  return render(request, 'boyoblue/about.html')

def terms(request):
  return render(request, 'boyoblue/terms.html')
