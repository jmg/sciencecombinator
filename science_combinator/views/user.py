from base import BaseView
from science_combinator.services.profile import ProfileService
from science_combinator.services.entry import EntryService
from django.contrib.auth import logout, login, authenticate


class MyScienceView(BaseView):

    url = r"^myscience/$"
    login_exempt = False

    def get(self, *args, **kwargs):

        return self.render_to_response({})


class VoteView(BaseView):

    def post(self, *args, **kwargs):

        entry = EntryService().get(id=self.request.POST.get("entry"))

        entry.votes += 1
        entry.voted_by.add(self.request.user)
        entry.save()

        return self.json_response({"status": "ok", "votes": entry.votes })