#!/bin/bash


# get new pushes from modified date
http GET https://api.pushbullet.com/v2/pushes\?modified_after\=$(<latestPush) -a $(<apiKey): --pretty=format > newPushes


# run commands
python runCommands.py newPushes


# push back data
http POST https://api.pushbullet.com/v2/pushes



