from base import BaseView
from science_combinator.services.profile import ProfileService
from science_combinator.services.entry import EntryService
from django.contrib.auth import logout, login, authenticate


class MyScienceView(BaseView):

    url = r"^myscience/$"
    login_exempt = False

    def get(self, *args, **kwargs):

        context = {}
        context["entries"] = self.request.user.profile.entries.all()

        return self.render_to_response(context)


class FavoriteView(BaseView):

    def post(self, *args, **kwargs):

        entry = EntryService().get(id=self.request.POST.get("id"))
        self.request.user.profile.entries.add(entry)

        return self.json_response({"status": "ok"})


class VoteView(BaseView):

    def post(self, *args, **kwargs):

        entry = EntryService().get(id=self.request.POST.get("id"))

        entry.votes += 1
        entry.voted_by.add(self.request.user.profile)
        entry.save()

        return self.json_response({"status": "ok", "votes": entry.votes })