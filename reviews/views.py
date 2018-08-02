from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.contrib.auth.decorators import login_required
from . import forms

def review_list_view(request):
  reviews = Review.objects.all().order_by('date')
  return render(request, 'reviews/list.html', {'reviews': reviews})

def review_detail_view(request, id):
  review = get_object_or_404(Review, pk=id)
  return render(request, 'reviews/detail.html', {'review': review})

@login_required(login_url='accounts:login')
def review_create_view(request):
  if request.method == 'POST':
    form = forms.CreateReview(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('home')
  elif request.method == 'GET':
    form = forms.CreateReview()
  return render(request, 'reviews/create.html', {'form': form})
