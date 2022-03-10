from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asyncio import sleep
from asgiref.sync import sync_to_async

from .models import Sensor
from .models import User
from .models import Record

#from . import counter
#from . import IR
from . import PIR

class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        NewUser = await User.create('Fredy Fuentes', 'brick', 'jackhammer')
        await NewUser.save_to_db()
        
        TempSensor = await Sensor.create('temp', 'C', 50, NewUser)
        await TempSensor.save_to_db() 
        AccelerometerX = await Sensor.create('accx', 'm/ss', 15, NewUser)
        await AccelerometerX.save_to_db() 
        AccelerometerY = await Sensor.create('accy', 'm/ss', 15, NewUser)
        await AccelerometerY.save_to_db() 
        AccelerometerZ = await Sensor.create('accz', 'm/ss', 15, NewUser)
        await AccelerometerZ.save_to_db() 
        #IRSensor = await Sensor.create('ir', 'units', 10, NewUser)
        #await IRSensor.save_to_db() 
        PIRSensor = await Sensor.create('pir', '', 1, NewUser)
        await PIRSensor.save_to_db() 

        for i in range(5000):
            # self.send(json.dumps({'message': randint(1,100)}))
            # forceVal = randint(1,100)
            '''
            tempVal = counter.get_temp()
            NewRecord = await Record.create(i*200, tempVal, NewUser.tool_selected, TempSensor, NewUser)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            accxVal = counter.get_acc('x')
            NewRecord = await Record.create(i*200, accxVal, NewUser.tool_selected, AccelerometerX, NewUser)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            accyVal = counter.get_acc('y')
            NewRecord = await Record.create(i*200, accyVal, NewUser.tool_selected, AccelerometerY, NewUser)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            acczVal = counter.get_acc('z')
            NewRecord = await Record.create(i*200, acczVal, NewUser.tool_selected, AccelerometerZ, NewUser)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            irDataArray = IR.get_reading()
            '''
            PIRval = PIR.get_reading()
            NewRecord = await Record.create(i*200, PIRval, NewUser.tool_selected, PIRSensor, NewUser)
            NewRecord.pk = None
            await NewRecord.save_to_db()

            '''
            NewRecord = await Record.create(i*200, irDataArray, NewUser.tool_selected, IRSensor, NewUser)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            '''
            #await self.send(json.dumps({'time': i, 'sensor': 'temp', 'value': tempVal, 'unit': 'C'}))
            #await self.send(json.dumps({'time': i, 'sensor': 'accx', 'value': accxVal, 'unit': 'm/ss'}))
            #await self.send(json.dumps({'time': i, 'sensor': 'accy', 'value': accyVal, 'unit': 'm/ss'}))
            #await self.send(json.dumps({'time': i, 'sensor': 'accz', 'value': acczVal, 'unit': 'm/ss'}))
            #await self.send(json.dumps({'time': i, 'sensor': 'ir', 'value': irDataArray, 'unit': 'units'}))
            await self.send(json.dumps({'time': i, 'sensor': 'pir', 'value': PIRval, 'unit': ''}))
            await sleep(.2)
