# websocketServer
websocket server in node to monitor pushbullet commands

# Install

## Dependencies
* node ws
* mysql

# Main Files

## logMonitor.sh
* starts node server to monitor websocket
* starts inotifywait to monitor log file

## pushbulletWebsocket.js
* monitors websocket and logs events

## runCommands.py
* parses new pushes and executes commands

# User Python modules

## PushBullet.py
* API caller

## MySQLCursor.py
* interact with mysql

### Pantry.py
* interact with pantry

