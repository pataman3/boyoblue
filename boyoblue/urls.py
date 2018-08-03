from django.urls import include, path
from django.contrib import admin
from reviews import views as review_views

app_name = "boyoblue"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', include('reviews.urls')),
    path('search/', include('search.urls')),
    path('accounts/', include('accounts.urls')),
    path('', review_views.review_list_view, name="home"),
]
