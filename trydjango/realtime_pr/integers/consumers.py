from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from .models import Sensor
from .models import User
from . import counter

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        TempTimestamps = []
        TempDataValues = []
        TempTools = []

        NewUser = User(name='JP', bar_mat='wood', tool_selected='drill')
        NewUser.save()
        TempSensor = Sensor(name='temperature', unit_name='C', threshold_value=50, user=NewUser)

        for i in range(50):
            # self.send(json.dumps({'message': randint(1,100)}))
            # forceVal = randint(1,100)

            tempVal = counter.get_temp()
            accxVal = counter.get_accx()

            TempTimestamps.append(i)
            TempDataValues.append(tempVal)
            TempTools.append(NewUser.tool_selected)

            TempSensor.timestamps = TempTimestamps
            TempSensor.data_values = TempDataValues
            TempSensor.tool_used = TempTools

            TempSensor.save()
            

            self.send(json.dumps({'time': i, 'sensor': TempSensor.name, 'value': tempVal, 'unit': TempSensor.unit_name}))
            self.send(json.dumps({'time': i, 'sensor': 'accx', 'value': accxVal, 'unit': 'm/ss'}))
            sleep(1)
