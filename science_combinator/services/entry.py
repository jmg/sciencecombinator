from base import BaseService
from youtube import YoutubeService
from science_combinator.models import Entry


class EntryService(BaseService):

    entity = Entry
    _page_size = 10

    MAX_VISIBLE_COMMENTS = 4

    def _get_page_query(self, offset, limit, **kwargs):

        return self.order_by("-id")[offset:limit]

    def get_entries(self):

        return YoutubeService().search_videos("Universe")

    def new_from_video(self, video):

        entry = self.new(**video)
        entry.save()
        return entry

    def visible_comments(self, entry):

        return entry.comment_set.order_by("-id")[0:self.MAX_VISIBLE_COMMENTS]

    def are_more_comments(self, entry):

        return entry.comment_set.count() > self.MAX_VISIBLE_COMMENTS


class TrendingEntryService(EntryService):

    def _get_page_query(self, offset, limit, **kwargs):

        mysql_query = "SELECT COALESCE(votes / pow(TIMESTAMPDIFF(MINUTE, submited, UTC_TIMESTAMP()), 1.8), 0) FROM science_combinator_entry h WHERE science_combinator_entry.id = h.id"
        qs = self.extra(select={"score": mysql_query }).order_by("-score", "-submited")[offset:limit]
        return qs

    def get_main_page(self, size=6):

        trendings = self.get_page(size=size)

        columns = [[], []]
        for i, trending in enumerate(trendings):
            columns[i%2].append(trending)

        return columns
