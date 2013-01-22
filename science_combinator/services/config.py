from datetime import datetime

from base import BaseService
from science_combinator.models import Config


class ConfigService(BaseService):

    entity = Config

    def get_default(self):

        return self.get_one(id=1)

    def update(self):

        config = self.get_default()
        config.last_updated = datetime.utcnow()
        config.save()