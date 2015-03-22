#!/bin/bash

# spawns node web server to monitor websocket
node pushBulletWebsocket.js >> socketLog &

# infite while loop
# waits until file modified then calls python script
# spawns script so that multiple instances can run at once
while inotifywait -e modify socketLog
do
	while : 
	do
		line=$(head -n1 socketLog)
		if [ -z "$line" ]; then
			break
		fi
		python runCommands.py $line 
		sed '1d' socketLog > socketLog
	done
done

