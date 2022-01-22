from django.shortcuts import render

# Create your views here.
from .models import SensorRecord
from django.views import generic

class RecordListView(generic.ListView):
    model = SensorRecord
    context_object_name = 'record_list'

def index(request):
    num_records = SensorRecord.objects.all().count()
    
    context = {'num_records': num_records,}

    return render(request, 'index.html', context=context)
