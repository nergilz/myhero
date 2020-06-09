from rest_framework import serializers
from .models import Movie, Hero


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""
    class Meta:
        model = Movie
        fields = ("title", "name", "title_ru", "year")


class HeroCreateSerializer(serializers.ModelSerializer):
    """Добавление персонажа"""
    class Meta:
        model = Hero
        fields = "__all__"
