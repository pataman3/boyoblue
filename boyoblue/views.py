from django.shortcuts import render

def about_us(request):
  return render(request, 'boyoblue/about-us.html')
