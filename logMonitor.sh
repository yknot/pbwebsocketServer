#!/bin/bash

node pushBulletWebsocket.js > socketLog &

while inotifywait -e modify socketLog; do
	./getCommands.sh &
done

