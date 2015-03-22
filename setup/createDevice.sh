#!/bin/bash

# creates a stream device 
# first argument is apikey 
# second argument is name
head='Authorization: Bearer '$1
curl --header "$head" -X POST https://api.pushbullet.com/v2/devices -d nickname=$2 -d type=stream
