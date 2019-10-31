from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import ugettext


class User(models.Model):
    username = models.CharField('Username', max_length=255,)

    class Meta:
        app_label = 'users'
