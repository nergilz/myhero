from django.views.generic.base import View
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie, Hero
from .serializers import MovieListSerializer, HeroCreateSerializer
from myhero.settings import API_KEY, API_URL


class MovieListView(APIView):
    """Вывод списка фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class HeroCreateView(generics.CreateAPIView):
    serializer_class = HeroCreateSerializer


class BaseView(View):
    def get(self, request):
        return render(request, "base.html", {"":""})