from base import BaseService
from science_combinator.models import Entry


class EntryService(BaseService):

    entity = Entry
    _page_size = 30

    def _get_page_query(self, offset, limit, **kwargs):

        return self.order_by("-id")[offset:limit]


class TrendingEntryService(EntryService):

    def _get_page_query(self, offset, limit, **kwargs):

        mysql_query = "SELECT COALESCE(votes / pow(TIMESTAMPDIFF(MINUTE, submited, UTC_TIMESTAMP()), 1.8), 0) FROM science_combinator_entry h WHERE science_combinator_entry.id = h.id"
        qs = self.extra(select={"score": mysql_query }).order_by("-score", "-submited")[offset:limit]
        return qs