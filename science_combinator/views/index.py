from base import BaseView
from science_combinator.services.entry import TrendingEntryService
from science_combinator.services.youtube import YoutubeService
from science_combinator.services.auth import AuthService
from science_combinator.services.config import ConfigService

from sciencecombinator.settings import LOGIN_REDIRECT


class IndexView(BaseView):

    url = r"^$"

    def get(self, *args, **kwargs):

        context = {}

        context["entries_columns"] = TrendingEntryService().get_main_page()
        context["config"] = ConfigService().get_default()

        return self.render_to_response(context)


class LoginView(BaseView):

    url = r"^login/$"

    def post(self, *args, **kwargs):

        try:
            AuthService().login(self.request.POST, self.request)
        except Exception, e:
            return self.render_to_response({"login_error": str(e)})

        return self.redirect(LOGIN_REDIRECT)


class RegisterView(BaseView):

    url = r"^register/$"
    template_name = "index/login.html"

    def post(self, *args, **kwargs):

        try:            
            AuthService().register(self.request.POST, self.request)
        except Exception, e:
            return self.render_to_response({"register_error": str(e)})

        return self.redirect(LOGIN_REDIRECT)


class DonationsView(BaseView):

    url = r"^donations/$"