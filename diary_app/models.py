from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)
    
    class Meta:
       abstract = True


class Diary(TimeStampedModel):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)


class Notes(TimeStampedModel):
    note_date = models.DateTimeField()
    note = models.TextField()
    image = models.ImageField(default = None, null = True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class ToDo(TimeStampedModel):
    title = models.CharField(max_length=100)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE) 
    done = models.BooleanField(default=False)


class Events(TimeStampedModel):
    event_time = models.DateTimeField()
    event_name = models.CharField(max_length=50)
    remind = models.BooleanField(default=False)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
