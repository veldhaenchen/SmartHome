# SmartHome


The server-socket.py file acts as a TCP server listening on a port of your choice. Make sure to edit that.

The file clientgps.py file sits on the Android device and sends network data and GPS co-ordinates, of which, Latitude and Longitude are later parsed by the Raspberry Pi server using parsedata.sh file.

The file, 'file2' received from the server-socket.py will have a lot of redundant data which will need to be removed. This will be done by parsedata.sh file which uses a linux golf command - a one liner. Later, we have infinite_index.sh file that runs the write_index.sh file every 10 seconds and update the html web page with the latest obtained location from 'file'.
