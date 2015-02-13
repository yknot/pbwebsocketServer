#!/bin/bash


# get new pushes from modified date
http GET https://api.pushbullet.com/v2/pushes\?modified_after\=$(<latestPush) -a $(<apiKey): --pretty=format > newPushes


# run commands and return latest push
latest=$(python runCommands.py newPushes)
if [ -z "$latest" ]
then
 	echo "No new latest push"
else
 	echo ${latest} > latestPush
fi





# parse for new commands
#cmds=$(node parseJSON.js command newPushes)

# # if not new commands
# if [ -z "$cmds" ]
# then
# 	echo "No new commands"
# else
# 	# for each command
# 	while read -r line; do
# 		# do something with command !!!!!!!!
# 		echo "$line"

# 	done <<< "$cmds"
# fi


# store latest push
# latest=$(node parseJSON.js latest newPushes)


# remove temp file
rm newPushes







