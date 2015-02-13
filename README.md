# websocketServer
websocket Server in node to monitor pushbullet traffic

##logMonitor.sh
* starts node server to monitor websocket
* starts inotifywait to monitor log file

##pushbulletWebsocket.js
* monitors websocket and logs events

##getCommands.sh
* gets new pushes and calls python script

##runCommands.py
* parses new pushes and executes commands (or at least will)

