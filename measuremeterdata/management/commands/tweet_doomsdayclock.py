from django.core.management.base import BaseCommand, CommandError
from measuremeterdata.tasks.socialmedia.tweet_doomsdayclock import tweet

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        tweet()

