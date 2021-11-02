from django.db import models

# Create your models here.

class SensorRecord(models.Model):
    time = models.IntegerField()
    sensor = models.CharField(max_length=200)
    value = models.FloatField()
    unit = models.CharField(max_length=200)
