
from django.urls import path
# from .views import index,movie_detail
from . import views

urlpatterns = [
    path("",views.MoviesView.as_view()),
    path("<slug:slug>/",views.MovieDetailView.as_view(),name='movie_detail'),
    path("review/<int:pk>/",views.AddReview.as_view(),name='add_review'),


]
