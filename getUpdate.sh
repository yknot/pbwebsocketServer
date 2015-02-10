#!/bin/bash


# get new pushes from modified date
http GET https://api.pushbullet.com/v2/pushes\?modified_after\=$(<latestPush) -a $(<api_key): --pretty=format > newPushes



# parse for new commands
cmds=$(node parseJSON.js command)

# for each command
if [ -z "$cmds" ]
then
	echo "No new commands"
else
	while read -r line; do
		echo "$line"
	done <<< "$cmds"
fi


# store latest push
latest=$(node parseJSON.js latest newPushes)
if [ -z "$latest" ]
then
	echo "No new latest push"
else
	echo ${latest} > latestPush
fi


# remove temp file
rm newPushes







