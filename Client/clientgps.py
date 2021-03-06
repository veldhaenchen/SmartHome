import androidhelper
import socket
import time

droid = androidhelper.Android()

port=YOUR_PORT

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("YOUR_SERVERS_IP_ADDRESS",port)) #connecting to pi as client
droid.makeToast("Starting location fetch") #notify me
while True:
	location = droid.getLastKnownLocation().result
	location = location.get('network', location.get('gps'))	#fetch location
	data = str(location)
	print(data) #logging
	s.send(data) #send to server
	time.sleep(5) #wait for 5 seconds
