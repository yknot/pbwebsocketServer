#!/bin/bash

node pushBulletWebsocket.js > socketLog &

while inotifywait -e modify socketLog; do
	./getUpdate.sh
done

