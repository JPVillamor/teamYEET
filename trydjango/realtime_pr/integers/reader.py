import json
import requests
import websocket
import time

ws = websocket.WebSocket()

#ws.connect('ws://127.0.0.1:8000/ws/some_url/')
ws.connect('ws://10.155.60.15:8000/ws/some_url/')

def read_all():
	while True:
		time.sleep(.5)
		
		temperature_file = open('temp_output.txt', 'r')
		temp_val = temperature_file.readline()
		temperature_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'temp','value':temp_val}}))
		
		accx_file = open('accx_output.txt', 'r')
		accx_val = accx_file.readline()
		accx_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'accx','value':accx_val}}))
		
		accy_file = open('accy_output.txt', 'r')
		accy_val = accy_file.readline()
		accy_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'accy','value':accy_val}}))
		
		accz_file = open('accz_output.txt', 'r')
		accz_val = accz_file.readline()
		accz_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'accz','value':accz_val}}))
		
		bottomForce_file = open('bforce_output.txt', 'r')
		bottomForce_val = bottomForce_file.readline()
		bottomForce_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'bottomForce','value':bottomForce_val}}))
		
		topForce_file = open('tforce_output.txt', 'r')
		topForce_val = topForce_file.readline()
		topForce_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'topForce','value':topForce_val}}))
		
		leftForce_file = open('lforce_output.txt', 'r')
		leftForce_val = leftForce_file.readline()
		leftForce_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'leftForce','value':leftForce_val}}))
		
		rightForce_file = open('rforce_output.txt', 'r')
		rightForce_val = rightForce_file.readline()
		rightForce_file.close()
		ws.send(json.dumps({'type':'data','value':{'sensor':'rightForce','value':rightForce_val}}))

if __name__=='__main__':
	read_all()
