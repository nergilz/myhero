from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BaseView.as_view()),
    path("movies/", views.MovieListView.as_view()),
    path('create/', views.HeroCreateView.as_view()),
]