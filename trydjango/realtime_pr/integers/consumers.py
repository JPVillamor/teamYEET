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

        ForceTimestamps = []
        ForceDataValues = []
        ForceTools = []

        NewUser = User(name='JP', bar_mat='wood', tool_selected='drill')
        NewUser.save()
        ForceSensor = Sensor(name='force', unit_name='lbs', threshold_value=50, user=NewUser)

        for i in range(50):
            # self.send(json.dumps({'message': randint(1,100)}))
            # forceVal = randint(1,100)

            forceVal = counter.update()

            ForceTimestamps.append(i)
            ForceDataValues.append(forceVal)
            ForceTools.append(NewUser.tool_selected)

            ForceSensor.timestamps = ForceTimestamps
            ForceSensor.data_values = ForceDataValues
            ForceSensor.tool_used = ForceTools

            ForceSensor.save()
            

            self.send(json.dumps({'time': i, 'sensor': ForceSensor.name, 'value': forceVal, 'unit': ForceSensor.unit_name}))
            sleep(1)