from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
# from .models import Sensor
# from .models import User
from . import counter

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(5000):
            # self.send(json.dumps({'message': randint(1,100)}))
            # forceVal = randint(1,100)

            tempVal = counter.get_temp()
            accxVal = counter.get_acc('x')
            accyVal = counter.get_acc('y')
            acczVal = counter.get_acc('z')

            self.send(json.dumps({'time': i, 'sensor': 'temp', 'value': tempVal, 'unit': 'C'}))
            self.send(json.dumps({'time': i, 'sensor': 'accx', 'value': accxVal, 'unit': 'm/ss'}))
            self.send(json.dumps({'time': i, 'sensor': 'accy', 'value': accyVal, 'unit': 'm/ss'}))
            self.send(json.dumps({'time': i, 'sensor': 'accz', 'value': acczVal, 'unit': 'm/ss'}))
            sleep(.2)
