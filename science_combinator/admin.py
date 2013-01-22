from django.contrib import admin
from django.db import models
import inspect
from models import *

for key, model in globals().copy().iteritems():
    if inspect.isclass(model) and issubclass(model, models.Model) and model is not User and model is not BaseModel:
        admin.site.register(model)