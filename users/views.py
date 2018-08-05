from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser

def user_detail_view(request, username):
  user = get_object_or_404(CustomUser, username=username)
  return render(request, 'users/detail.html', {'user': user})
