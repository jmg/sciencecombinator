from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User
from science_combinator.utils.date import get_time_since


class BaseModel(models.Model):

    TIME_FIELD = "submited"

    def object_age(self):
        return get_time_since(getattr(self, self.TIME_FIELD))

    class Meta:
        abstract = True


class Config(BaseModel):

    TIME_FIELD = "last_updated"
    last_updated = models.DateTimeField(default=datetime.utcnow())


class Profile(User):

    entries = models.ManyToManyField("Entry")


class Entry(BaseModel):

    title = models.CharField(max_length=300, null=True, blank=True)
    published = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=300, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)

    remote_id = models.CharField(max_length=300)

    user = models.ForeignKey("Profile", null=True)

    votes = models.PositiveIntegerField(default=0)
    voted_by = models.ManyToManyField("Profile", related_name="votes")
    submited = models.DateTimeField(default=datetime.utcnow())

    def get_duration(self):

        if self.duration:
            return str(timedelta(seconds=int(self.duration)))
        return ""


class Comment(BaseModel):

    content = models.TextField()
    entry = models.ForeignKey("Entry")
    submited = models.DateTimeField(null=True)

    user = models.ForeignKey("Profile", null=True)


class AcceptedCategory(BaseModel):

    name = models.CharField(max_length=300)


class SearchTerm(BaseModel):

    term = models.CharField(max_length=300)
    weight = models.DecimalField(decimal_places=2, max_digits=5, default=0)
