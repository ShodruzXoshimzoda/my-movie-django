from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Movie

'''  CBV  '''

def index(request):
    movie_list = Movie.objects.all()
    context= {'movie_list':movie_list}
    return render(request,'movie/movies.html',context)

def movie_detail(request,slug):
    movie = Movie.objects.get(url=slug)
    context = {'movie':movie}

    return render(request,'movie/moviesingle.html',context)

