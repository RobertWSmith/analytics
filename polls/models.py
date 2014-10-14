
import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __repr__(self):
        return "<Poll: {0}>".format(self.question)

    def __str__(self):
        return str(self.__repr__())

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return "<Choice: {0}>".format(self.question)

    def __str__(self):
        return str(self.__repr__())

