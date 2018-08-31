from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from boyoblue.media import medias

from reviews.models import Review
from .models import CustomUser

def user_detail_view(request, username):
  user = get_object_or_404(CustomUser, username=username)

  reviews = []
  page_number = request.GET.get('page', 1)

  reviews_by_user = Review.objects.filter(author=user)
  paginator = Paginator(reviews_by_user.order_by('date')[::-1], 10)

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

  return render(request, 'users/detail.html', {'user': user, 'reviews': reviews, 'paginator': page})
