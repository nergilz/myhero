from smtplib import  SMTPAuthenticationError
from django.core.management.base import  BaseCommand, CommandError
from django.contrib.auth.models import  User
from hero.models import Movie, Hero
from myhero.settings import  API_KEY, API_URL

import requests


class Command(BaseCommand): 
    help='This command get the data on "omdbapi.com" and save in db'

    def handle(self, *args, **options):

        try:
            heros_qs = Hero.objects.all()
            Movie.objects.all().delete()
        except Movie.DoesNotExist:
            raise CommandError('does not exist')

        for hero in heros_qs:
            payload = {
                "type" : 'movie',
                "s" : hero.name,
                "apikey" : API_KEY,
                }
            try:
                response = requests.get(API_URL, payload)
            except requests.exceptions.HTTPError as error:
                print(' Requests ERROR:', error)

            for data in response.json()['Search']:
                Movie.objects.create(
                    name = hero.name,
                    title = data['Title'],
                    year = data['Year']
                )
        print('*OK*')
