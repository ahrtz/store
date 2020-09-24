from django.urls import path, include

from . import views
from rest_framework import routers

app_name = 'favorites'

urlpatterns = [
    path('', views.favorites_list),
    path('users/insert/', views.insert_favorites),
    path('users/list/', views.search_favorites),
]