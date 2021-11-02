import datetime
from MAT.models import SensorRecord

INCREMENT = 200

start_time = datetime.datetime.now()
one_time = False
p = 0

while True:
    d = datetime.datetime.now() - start_time
    t = d / datetime.timedelta(microseconds=1) // 1000
    
    if t % INCREMENT == 0 and p != t:
        one_time = True
    if one_time:
        one_time = False
        p = t
        
        new_record = SensorRecord(time=int(p),sensor='force',value=int(222),unit='lbs')
        new_record.save()

        print(p)
    if t >= 10000:
        break
