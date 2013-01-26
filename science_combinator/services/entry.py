from base import BaseService
from youtube import YoutubeService
from science_combinator.models import Entry, SearchTerm
from random import shuffle


class EntryService(BaseService):

    entity = Entry
    _page_size = 10

    MAX_VISIBLE_COMMENTS = 4

    def _get_page_query(self, offset, limit, **kwargs):

        return self.order_by("-id")[offset:limit]

    def get_new_videos(self):

        videos = []

        terms = list(SearchTerm.objects.order_by("-weight")[0:50])
        shuffle(terms)

        for search_term in terms[0:5]:
            videos.extend(YoutubeService().search_videos(search_term.term))

        return videos

    def new_from_video(self, video):

        entry, created = self.get_or_create(remote_id=video["remote_id"])

        if created:
            for key, value in video.iteritems():
                setattr(entry, key, value)
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
