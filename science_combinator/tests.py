"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from science_combinator.services.youtube import YoutubeService


class SearchTest(TestCase):

    def test_youtube_search(self):
        
        videos = YoutubeService().search_videos("science")

        self.assertTrue(bool(videos))
        self.assertTrue(isinstance(videos, list))
