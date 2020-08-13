from django.db import models

# Create your models here.


class Room(models.Model):
    duration = models.IntegerField()