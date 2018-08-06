from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.contrib.auth.decorators import login_required
from boyoblue.media import songs, movies
from . import forms

def review_list_view(request):
  reviews = []
  for review in Review.objects.all().order_by('date')[:10][::-1]:
    reviews.append([review, 'reviews/mediacards/{}.html'.format(review.type)])
    if review.type == 'song':
      reviews[-1].append(songs.get(review.api_id))
    elif review.type == 'movie':
      reviews[-1].append(movies.get(review.api_id))
    else:
      return HttpResponseNotFound

  return render(request, 'reviews/list.html', {'reviews': reviews})

def review_detail_view(request, pk):
  review = get_object_or_404(Review, pk=pk)
  return render(request, 'reviews/detail.html', {'review': review})

@login_required(login_url='accounts:login')
def review_create_view(request, api_id="", type=None):
  if request.method == 'POST':
    form = forms.CreateReview(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('home')
  elif request.method == 'GET':
    form = forms.CreateReview({'api_id': api_id, 'type': type})
  return render(request, 'reviews/create.html', {'form': form})
