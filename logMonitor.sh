#!/bin/bash

# spawns node web server to monitor websocket
node pushBulletWebsocket.js > socketLog &

# infite while loop
# waits until file modified then calls python script
# spawns script so that multiple instances can run at once
while inotifywait -e modify socketLog; do
	python runCommands.py &
done

