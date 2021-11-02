from django.shortcuts import render

# Create your views here.
from .models import SensorRecord

def index(request):
    num_records = SensorRecord.objects.all().count()
    
    context = {'num_records': num_records,}

    return render(request, 'index.html', context=context)
