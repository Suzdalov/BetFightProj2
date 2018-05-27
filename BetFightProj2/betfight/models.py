from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class resultModel(models.Model):
    teamHomeScore = models.IntegerField
    teamGuestScore = models.IntegerField
    class Meta:
        abstract = True

class event(models.Model):
    code = models.CharField(max_length=36)
    short_name = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    descr = models.TextField()


    def __str__(self):
        return self.name

class team(models.Model):
    event_ref = models.ForeignKey('event', related_name='fromTeam')
    shortName = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    groupLetter = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.shortName

class match (models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    dateStart = models.DateTimeField (default=timezone.now)
    event_ref = models.ForeignKey('event' , related_name='fromMatch')
    teamHome = models.ForeignKey('team',related_name='teamA')
    teamGuest = models.ForeignKey('team',related_name='teamB')
    baseHomeScore = models.IntegerField(null=True, blank=True)
    baseGuestScore = models.IntegerField(null=True, blank=True)
    totalHomeScore = models.IntegerField(null=True, blank=True)
    totalGuestScore = models.IntegerField(null=True, blank=True)
    koeffHome = models.FloatField(null=True, blank=True)
    koeffDraw = models.FloatField(null=True, blank=True)
    koeffGuest = models.FloatField(null=True, blank=True)
    isOver = models.BooleanField(default=False)

    def __str__(self):
        return self.teamHome.shortName+' vs '+self.teamGuest.shortName