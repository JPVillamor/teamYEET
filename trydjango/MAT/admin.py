from django.contrib import admin

# Register your models here.
from .models import SensorRecord

admin.site.register(SensorRecord)
