from base import BaseView
from science_combinator.services.entry import TrendingEntryService
from science_combinator.services.youtube import YoutubeService


class IndexView(BaseView):

    url = r"^$"

    def get(self, *args, **kwargs):

        context = {}

        trendings = TrendingEntryService().get_page(size=6)

        context["entries_columns"] = [trendings[0:3], trendings[3:6]]

        return self.render_to_response(context)


class AboutView(BaseView):

    url = r"^about/$"


class DonationsView(BaseView):

    url = r"^donations/$"