#!/bin/bash

node pushBulletWebsocket.js > socketLog &

while inotifywait -e modify socketLog; do
	python runCommands.py &
done

