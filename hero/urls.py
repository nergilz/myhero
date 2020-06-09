from django.urls import path, include
from . import views


urlpatterns = [
    path("movies/", views.MovieListView.as_view()),
    path('create/', views.HeroCreateView.as_view()),
]