from django.shortcuts import render, redirect
from .models import Record, User, Sensor
from django.http import HttpResponse

import csv

# Create your views here.
def index(request):
    return render(request, 'index.html', context={'text': 'Hello World'})
    
def exportcsv(request):
    records = Record.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=readings_' + User.objects.get(id=1).name + '.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Timestamp', 'Data', 'Tool'])
    recs = records.values_list('id', 'timestamp', 'data_value', 'tool_used')
    
    for rec in recs:
        writer.writerow(rec)
    
    return response
