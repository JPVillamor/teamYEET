from django.shortcuts import render, redirect
from .models import Record, User, Sensor
from django.http import HttpResponse
from .models import UserInfo, UserInfoForm

import csv

# Create your views here.
def index(request):
	return render(request, 'index.html', context={'text': 'Hello World'})

def index(request):
    return render(request, 'index.html', context={'text': 'Hello World'})

def home(request):
    '''print(request.method)
    if(request.method == 'POST'):
        print("IM HEREEREE NOW")
        u = UserInfo()
        u.fname = request.Post.get('fname')
        u.lname = request.Post.get('lname')
        print(u.fname)
        u.save()
    return render(request, 'home.html')'''
    if request.POST:
        form = UserInfoForm(request.POST)
        #print(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'home.html', {'form' : form})
    else:
        return render(request, 'home.html')
    
def force_setup(request):
    return render(request, 'force_setup.html')    


def exportcsv(request):
    records = Record.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=readings_' + UserInfo.objects.latest('id').fname + UserInfo.objects.latest('id').lname + '.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Timestamp', 'Data', 'Tool'])
    recs = records.values_list('id', 'timestamp', 'data_value', 'tool_used')
    for rec in recs:
        writer.writerow(rec)
    #UserInfo.objects.all().delete()
    return response
