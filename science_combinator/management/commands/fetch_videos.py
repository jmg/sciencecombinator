from django.core.management.base import BaseCommand, CommandError
from science_combinator.services.entry import EntryService
from science_combinator.services.config import ConfigService


class Command(BaseCommand):

    service = EntryService()

    def handle(self, *args, **options):

        videos = self.service.get_new_videos()
        for video in videos:
            self.service.new_from_video(video)

        ConfigService().update()