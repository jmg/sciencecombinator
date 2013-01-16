from datetime import datetime

from django.db import models
from science_combinator.utils.date import get_time_since


class BaseModel(models.Model):

    def object_age(self):
        return get_time_since(self.submited)

    class Meta:
        abstract = True


class Profile(BaseModel):

    username = models.CharField(max_length=300)
    email = models.CharField(max_length=300, null=True, blank=True)
    remote_id = models.CharField(max_length=300)
    url = models.CharField(max_length=300, null=True, blank=True)
    access_token = models.CharField(max_length=300, blank=True, null=True)


class Entry(BaseModel):

    title = models.CharField(max_length=300, null=True, blank=True)
    published = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    remote_id = models.CharField(max_length=300)

    user = models.ForeignKey("Profile", null=True)

    votes = models.PositiveIntegerField(default=0)
    voted_by = models.ManyToManyField("Profile", related_name="votes")
    submited = models.DateTimeField(default=datetime.utcnow())


class Comment(BaseModel):

    content = models.TextField()
    entry = models.ForeignKey("Entry")
    submited = models.DateTimeField(null=True)

    user = models.ForeignKey("Profile", null=True)