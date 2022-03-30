from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asyncio import sleep
from asgiref.sync import sync_to_async

from .models import Sensor
from .models import User
from .models import Record
from .models import UserInfo


from . import counter
#from . import IR
from . import PIR
from . import forcemux


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        # username = UserInfo.objects.get(pk = 1).name
        
        NewUser = await User.create("FREDWARD FUENTACLES", 'brick', 'jackhammer')
        await NewUser.save_to_db()
        
        TempSensor = await Sensor.create('temp', 'C', 50)
        await TempSensor.save_to_db() 
        AccelerometerX = await Sensor.create('accx', 'm/ss', 15)
        await AccelerometerX.save_to_db() 
        AccelerometerY = await Sensor.create('accy', 'm/ss', 15)
        await AccelerometerY.save_to_db() 
        AccelerometerZ = await Sensor.create('accz', 'm/ss', 15)
        await AccelerometerZ.save_to_db() 
        #IRSensor = await Sensor.create('ir', 'units', 10, NewUser)
        #await IRSensor.save_to_db() 
        PIRSensor = await Sensor.create('pir', '', 1)
        await PIRSensor.save_to_db() 
        ForceSensor1 = await Sensor.create('force1', 'lbs', 5)
        await ForceSensor1.save_to_db()
        ForceSensor2 = await Sensor.create('force2', 'lbs', 5)
        await ForceSensor2.save_to_db()
        ForceSensor3 = await Sensor.create('force3', 'lbs', 5)
        await ForceSensor3.save_to_db()
        ForceSensor4 = await Sensor.create('force4', 'lbs', 5)
        await ForceSensor4.save_to_db()

        for i in range(5000):
            # self.send(json.dumps({'message': randint(1,100)}))
            # forceVal = randint(1,100)
            
            tempVal = counter.get_temp()
            NewRecord = await Record.create(i*200, tempVal, NewUser.tool_selected, TempSensor)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            accxVal = counter.get_acc('x')
            NewRecord = await Record.create(i*200, accxVal, NewUser.tool_selected, AccelerometerX)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            accyVal = counter.get_acc('y')
            NewRecord = await Record.create(i*200, accyVal, NewUser.tool_selected, AccelerometerY)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            acczVal = counter.get_acc('z')
            NewRecord = await Record.create(i*200, acczVal, NewUser.tool_selected, AccelerometerZ)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            #irDataArray = IR.get_reading()
            
            PIRval = PIR.get_reading()
            NewRecord = await Record.create(i*200, PIRval, NewUser.tool_selected, PIRSensor)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            with forcemux.force1:
                forcemux.function(forcemux.force1, 1)
            Force1Val = forcemux.force_out1
            NewRecord = await Record.create(i*200, Force1Val, NewUser.tool_selected, ForceSensor1)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            with forcemux.force2:
                forcemux.function(forcemux.force2, 2)
            Force2Val = forcemux.force_out2
            NewRecord = await Record.create(i*200, Force2Val, NewUser.tool_selected, ForceSensor2)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            with forcemux.force3:
                forcemux.function(forcemux.force3, 3)
            Force3Val = forcemux.force_out3
            NewRecord = await Record.create(i*200, Force3Val, NewUser.tool_selected, ForceSensor3)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            with forcemux.force4:
                forcemux.function(forcemux.force4, 4)
            Force4Val = forcemux.force_out4
            NewRecord = await Record.create(i*200, Force4Val, NewUser.tool_selected, ForceSensor4)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            
            '''
            NewRecord = await Record.create(i*200, irDataArray, NewUser.tool_selected, IRSensor, NewUser)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            '''
            await self.send(json.dumps({'time': i, 'sensor': 'temp', 'value': tempVal, 'unit': 'C'}))
            await self.send(json.dumps({'time': i, 'sensor': 'accx', 'value': accxVal, 'unit': 'm/ss'}))
            await self.send(json.dumps({'time': i, 'sensor': 'accy', 'value': accyVal, 'unit': 'm/ss'}))
            await self.send(json.dumps({'time': i, 'sensor': 'accz', 'value': acczVal, 'unit': 'm/ss'}))
            #await self.send(json.dumps({'time': i, 'sensor': 'ir', 'value': irDataArray, 'unit': 'units'}))
            await self.send(json.dumps({'time': i, 'sensor': 'pir', 'value': PIRval, 'unit': ''}))
            await self.send(json.dumps({'time': i, 'sensor': 'force1', 'value': Force1Val, 'unit': 'lbs'}))
            await self.send(json.dumps({'time': i, 'sensor': 'force2', 'value': Force2Val, 'unit': 'lbs'}))
            await self.send(json.dumps({'time': i, 'sensor': 'force3', 'value': Force3Val, 'unit': 'lbs'}))
            await self.send(json.dumps({'time': i, 'sensor': 'force4', 'value': Force4Val, 'unit': 'lbs'}))
            await sleep(.2)
