from django.db import models
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, db_column='name')
    bar_mat = models.CharField(max_length=200)
    tool_selected = models.CharField(max_length=200)

    @database_sync_to_async
    def save_to_db(self):
        self.save()

    @classmethod
    @sync_to_async
    def create(cls, name, bar_mat, tool_selected):
        user = cls(name=name, bar_mat=bar_mat, tool_selected=tool_selected)
        return user

    class Meta:
        ordering = ["name"]

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    unit_name = models.CharField(max_length=200)
    threshold_value = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    @database_sync_to_async
    def save_to_db(self):
        self.save()

    @classmethod
    @sync_to_async
    def create(cls, name, unit_name, threshold_value, user):
        sensor = cls(name=name, unit_name=unit_name, threshold_value=threshold_value, user=user)
        return sensor

    class Meta:
        ordering = ["name"]

class Record(models.Model):
    timestamp = models.IntegerField()
    data_value = models.DecimalField(max_digits=5, decimal_places=2)
    tool_used = models.CharField(max_length=200)
    sensor = models.ForeignKey(Sensor, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    @database_sync_to_async
    def save_to_db(self):
        self.save()

    @classmethod
    @sync_to_async
    def create(cls, timestamp, data_value, tool_used, sensor, user):
        record = cls(timestamp=timestamp, data_value=data_value, tool_used=tool_used, sensor=sensor, user=user)
        return record

    class Meta:
        ordering = ["timestamp"]
