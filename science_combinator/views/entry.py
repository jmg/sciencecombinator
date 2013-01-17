from base import BaseView
from science_combinator.services.entry import EntryService, TrendingEntryService


class BaseEntryView(BaseView):

    def get(self, *args, **kwargs):

        page = self.request.GET.get("page", 0)

        context = {}
        projects = self.service.get_page(page=page)
        context["entries"] = projects
        context["view_name"] = self.view_name
        context["next_page"] = int(page) + 1

        return self.render_to_response(context)


class TrendingView(BaseEntryView):

    service = TrendingEntryService()
    view_name = "trending"
    url = r"^{0}/$".format(view_name)


class NewView(BaseEntryView):

    service = EntryService()
    view_name = "new"
    url = r"^{0}/$".format(view_name)


class EntryView(BaseEntryView):

    url = r"^entries/(?P<entry_id>\d+)"

    def get(self, *args, **kwargs):

        context = {"entry": EntryService().get(id=self.kwargs["entry_id"])}
        return self.render_to_response(context)


class Comments(BaseView):

    url = r"^entries/(?P<entry_id>\d+)/comments/$"

    def get(self, *args, **kwargs):

        context = {}

        entry = EntryService().get(id=self.kwargs["entry_id"])
        context["entry"] = entry
        context["comments"] = entry.comment_set.all()

        return self.render_to_response(context)