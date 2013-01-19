from datetime import datetime

from base import BaseView
from science_combinator.services.comment import CommentService


class NewView(BaseView):

    template_name = "entries/_comment.html"

    def post(self, *args, **kwargs):

        entry = self.request.POST.get("entry")
        content = self.request.POST.get("comment")

        comment = CommentService().new(content=content, entry_id=entry, submited=datetime.utcnow(), user=self.request.user)
        comment.save()

        return self.render_to_response({"comment": comment })