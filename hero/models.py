from django.db import models


class Hero(models.Model):

    name = models.CharField("персонаж", max_length=100)

    def __str__(self):
        return str(self.name)


class Movie(models.Model):

    title = models.CharField("название", max_length=100)
    name = models.CharField("персонаж", max_length=100)
    title_ru = models.CharField("название_рус", max_length=100, default="")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2020)

    def __str__(self):
        return self.name




