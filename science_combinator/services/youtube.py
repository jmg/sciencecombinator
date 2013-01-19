import gdata.youtube
import gdata.youtube.service

from urlparse import parse_qs, urlsplit
from sciencecombinator.settings import YOUTUBE_SECRET_KEY


class YoutubeService(object):    

    def search_videos(self, needle):

        service = gdata.youtube.service.YouTubeService()
        service.developer_key = YOUTUBE_SECRET_KEY
        service.client_id = "Science Combinator"

        query = gdata.youtube.service.YouTubeVideoQuery()
        query.vq = needle
        feed = service.YouTubeQuery(query)
            
        videos = []
        for entry in feed.entry:

            url = entry.media.player.url
            qs = parse_qs(urlsplit(url).query)

            video = {
                "remote_id": qs["v"][0],
                "title": entry.media.title.text,
                "description": entry.media.description.text,
                "category": entry.media.category[0].text,
                "published": entry.published.text,
                "thumbnail": entry.media.thumbnail[0].url,
                "duration": entry.media.duration.seconds,
            }

            self._normalize(video)
            videos.append(video)

        return videos

    def _normalize(self, video):

        for key, value in video.iteritems():
            try:
                video[key] = value.encode("utf-8")
            except:
                video[key] = ""