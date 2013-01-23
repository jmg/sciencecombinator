from datetime import datetime

from base import BaseView
from science_combinator.services.comment import CommentService
from science_combinator.services.entry import EntryService


class NewView(BaseView):

    template_name = "entry/_comment.html"

    def post(self, *args, **kwargs):

        entry = EntryService().get(id=self.request.POST.get("entry"))
        content = self.request.POST.get("content")

        comment = CommentService().new(content=content, entry=entry, submited=datetime.utcnow(), user=self.request.user.profile)
        comment.save()        

        return self.render_to_response({"comment": comment })


class AllView(BaseView):

    template_name = "entry/_comments.html"

    def post(self, *args, **kwargs):

        comments = CommentService().filter(entry__id=self.request.POST.get("entry")).order_by("-id")

        return self.render_to_response({"comments": comments })