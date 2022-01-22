from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, db_column='name')
    bar_mat = models.CharField(max_length=200)
    tool_selected = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    unit_name = models.CharField(max_length=200)
    threshold_value = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    timestamps = models.JSONField()
    data_values = models.JSONField()
    tool_used = models.JSONField()

    class Meta:
        ordering = ["name"]