#!/bin/bash
while :
do
	cat /home/pi/Desktop/SmartHome/ServerSide/file | ./write_index.sh > /var/www/html/index.html
	sleep 10
done
