from django.db import models
from django.contrib.auth.models import User


class League(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    is_public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    league = models.ForeignKey(League)
    summoner_id = models.BigIntegerField('Summoner ID')
    nickname = models.CharField(max_length=32, default=None)

    def __str__(self):
        if self.nickname is None:
            return self.summoner_id
        else:
            return '%s (%s)' % (self.summoner_id, self.nickname)