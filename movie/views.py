from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.views.generic import ListView,DetailView
from .models import Movie
from .forms import ReviewForm


'''  CBV  '''

# def index(request):
#     movie_list = Movie.objects.all()
#     context= {'movie_list':movie_list}
#     return render(request,'movie/movies.html',context)

# def movie_detail(request,slug):
#     movie = Movie.objects.get(url=slug)
#     context = {'movie':movie}

#     return render(request,'movie/moviesingle.html',context)

class MoviesView(ListView):
    ''' Список фильмов '''
    model = Movie
    queryset = Movie.objects.filter(draft = False)
    template_name = 'movie/movies.html'

class MovieDetailView(DetailView):
    ''' Класс для одного фильма  '''
    model = Movie
    slug_field = 'url'

class AddReview(View):
    ''' Отзывы '''

    def post(self,request,pk):
        # print(request.POST)
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie  # Привязываем отзыв к опредедному фильму
            form.save()
            print("Всё Окей")
        # print(request.POST)
        return redirect(movie.get_absolute_url())
    