from django.core.management.base import BaseCommand, CommandError
from science_combinator.services.entry import EntryService


class Command(BaseCommand):

    service = EntryService()

    def handle(self, *args, **options):

        videos = self.service.get_entries()
        for video in videos:
            self.service.new_from_video(video)


