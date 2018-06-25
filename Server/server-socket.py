#server script
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("YOUR_IP_ADDRESS",YOUR_PORT))
sock.listen(2)
(client,(ip,port))=sock.accept()

while True:
	gpsdata = client.recv(1204)
	file = open("file2","w")
	file.write(gpsdata)
	file.close()
