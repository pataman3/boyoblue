from django.urls import include, path
from django.contrib import admin
from reviews import views as review_views
from . import views

app_name = "boyoblue"

urlpatterns = [
    path('', review_views.review_list_view, name="home"),

    # admin
    path('admin/', admin.site.urls),

    # about
    path('about/', views.about),
    
    # account management
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),

    path('reviews/', include('reviews.urls')),
    path('search/', include('search.urls')),
]
