from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from boyoblue.media import medias
from . import forms

def review_list_view(request):
  reviews = []
  page_number = request.GET.get('page', 1)

  paginator = Paginator(Review.objects.all().order_by('date')[::-1], 10)
  try:
    page = paginator.page(page_number)
  except PageNotAnInteger:
    page = paginator.page(1)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)

  for review in page:
    media = medias.get(review.type, review.api_id)
    if media is None:
      return HttpResponseNotFound
    truncate_body = len(review.body) > 140
    reviews.append([
      review,  # review
      'reviews/media/{}.html'.format(review.type),  # review_card
      media,  # media
      review.body[:140] if truncate_body else review.body,  # body
      truncate_body  # truncate_body
    ])
  return render(request, 'reviews/list.html', {'reviews': reviews, 'paginator': page})

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
  return render(request, 'reviews/create.html', {'api_id': api_id, 'type': type})
