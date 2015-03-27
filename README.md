# websocketServer
websocket server in node to monitor pushbullet commands with execution of commands in python

# Install

## Dependencies
* node
    * ws
* inotify-tools
* python-pip
    * simplejson

## Setup
* clone git repo
* run install script (future feature)
    * init script (need to fix for new json version)
      * create file for apiKey
      * create latestpush file
    * run as service (future developement)





# Files

## logMonitor.sh
* starts node server to monitor websockets
* starts inotifywait to monitor log file
    * run commands removes line from the socketLog file (queue)

## pushbulletWebsocket.js
* monitors websocket for each user and logs events

## runCommands.py
* parses new pushes and executes commands

## py_modules\PushBullet.py
* class for interacting with Pushbullet API

## py_modules\Pantry.py
* class for interacting with the Pantry

