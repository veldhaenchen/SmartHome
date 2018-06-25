#!/bin/bash

while :
do
  sed -e 's:{:\n:g' /home/pi/Desktop/SmartHome/ServerSide/file2 | sed -e 's:}: :g' | tr -d "u'longitude':" | tr -s " " | awk '{print $11,$7;}' | cut -d "," -f 1-2 | tail -1 > /home/pi/Desktop/SmartHome/ServerSide/file
  sleep 10
done
