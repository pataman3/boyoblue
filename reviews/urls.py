from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.review_list_view, name='list'),
    path('create/', views.review_create_view, name="create"),
    path('create/<str:type>/<str:api_id>/', views.review_create_view, name="create"),
    path('detail/<int:pk>/', views.review_detail_view, name='detail'),
]
