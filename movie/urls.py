
from django.urls import path
from .views import index,movie_detail

urlpatterns = [
    path("",index),
    path("<slug:slug>/",movie_detail,name='movie_detail'),


]
