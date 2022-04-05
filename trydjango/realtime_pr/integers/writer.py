import time, threading

import counter
import forcemux

def write_temp():
	while True:
		output = counter.get_temp()
		temp_output_file = open('temp_output.txt', 'wt')
		temp_output_file.write(str(output))
		temp_output_file.close()
		time.sleep(.2)

def write_accx():
	while True:
		output = counter.get_acc('x')
		accx_output_file = open('accx_output.txt', 'wt')
		accx_output_file.write(str(output))
		accx_output_file.close()
		time.sleep(.2)
		
def write_accy():
	while True:
		output = counter.get_acc('y')
		accy_output_file = open('accy_output.txt', 'wt')
		accy_output_file.write(str(output))
		accy_output_file.close()
		time.sleep(.2)

def write_accz():
	while True:
		output = counter.get_acc('z')
		accz_output_file = open('accz_output.txt', 'wt')
		accz_output_file.write(str(output))
		accz_output_file.close()
		time.sleep(.2)
		
def write_bottomForce():
	while True:
		with forcemux.force1:
			forcemux.function(forcemux.force1, 1)
		output = forcemux.force_out1
		bforce_output_file = open('bforce_output.txt', 'wt')
		bforce_output_file.write(str(round(output, 2)))
		bforce_output_file.close()
		time.sleep(.1)

def write_topForce():
	while True:
		with forcemux.force3:
			forcemux.function(forcemux.force3, 3)
		output = forcemux.force_out3
		tforce_output_file = open('tforce_output.txt', 'wt')
		tforce_output_file.write(str(round(output, 2)))
		tforce_output_file.close()
		time.sleep(.1)

def write_leftForce():
	while True:
		with forcemux.force4:
			forcemux.function(forcemux.force4, 4)
		output = forcemux.force_out4
		lforce_output_file = open('lforce_output.txt', 'wt')
		lforce_output_file.write(str(round(output, 2)))
		lforce_output_file.close()
		time.sleep(.1)
		
def write_rightForce():
	while True:
		with forcemux.force2:
			forcemux.function(forcemux.force2, 2)
		output = forcemux.force_out2
		rforce_output_file = open('rforce_output.txt', 'wt')
		rforce_output_file.write(str(round(output, 2)))
		rforce_output_file.close()
		time.sleep(.1)

temp_thread = threading.Thread(target=write_temp)
accx_thread = threading.Thread(target=write_accx)
accy_thread = threading.Thread(target=write_accy)
accz_thread = threading.Thread(target=write_accz)
bottomForce_thread = threading.Thread(target=write_bottomForce)
topForce_thread = threading.Thread(target=write_topForce)
leftForce_thread = threading.Thread(target=write_leftForce)
rightForce_thread = threading.Thread(target=write_rightForce)

if __name__=='__main__':
	temp_thread.start()
	accx_thread.start()
	accy_thread.start()
	accz_thread.start()
	bottomForce_thread.start()
	topForce_thread.start()
	leftForce_thread.start()
	rightForce_thread.start()
