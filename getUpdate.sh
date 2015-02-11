#!/bin/bash


# get new pushes from modified date
http GET https://api.pushbullet.com/v2/pushes\?modified_after\=$(<latestPush) -a $(<api_key): --pretty=format > newPushes



# parse for new commands
cmds=$(node parseJSON.js command newPushes)

# if not new commands
if [ -z "$cmds" ]
then
	echo "No new commands"
else
	# for each command
	while read -r line; do
		# do something with command !!!!!!!!
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







