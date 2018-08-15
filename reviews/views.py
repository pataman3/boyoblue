from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.contrib.auth.decorators import login_required
from boyoblue.media import medias
from . import forms

def review_list_view(request):
  reviews = []
  for review in Review.objects.all().order_by('date')[::-1][:10]:
    media = medias.get(review.type, review.api_id)
    if media is None:
      return HttpResponseNotFound
    reviews.append([
      review,  # review
      'reviews/media/{}.html'.format(review.type),  # review_card
      media,  # media
      review.body[:140] + ' ... (See full review)' if len(review.body) >= 140 else review.body  # body
    ])
  return render(request, 'reviews/list.html', {'reviews': reviews})

def review_detail_view(request, pk):
  review = get_object_or_404(Review, pk=pk)
  card = 'reviews/media/{}.html'.format(review.type)
  media = medias.get(review.type, review.api_id)
  if media is None:
    return HttpResponseNotFound
  return render(request, 'reviews/detail.html', {
    'review': review,
    'media': media,
    'card': card,
    'body': review.body
  })

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
