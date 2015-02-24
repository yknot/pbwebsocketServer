#!/bin/bash


# if apiKey exists
if [ -e apiKey ]
then
	# do you want to overwrite?
	read -r -p "Do you want to overwrite 'apiKey'?" response
	case $response in
		[yY][eE][sS]|[yY]) 
			read -r -p "Enter API Key:" apiKey

			# write file
			echo $apiKey > apiKey
			echo "Writing 'apiKey'"
        ;;
		*)
			echo "Keeping 'apiKey'"
        ;;
	esac 
	
else
	read -r -p "Enter API Key:" apiKey
	
	# write file
	echo $apiKey > apiKey
	echo "Writing 'apiKey'"
fi






# check for latest push file
# if apiKey exists
if [ -e latestPush ]
then
	# do you want to overwrite?
	read -r -p "Do you want to overwrite 'latestPush'?" response
	case $response in
		[yY][eE][sS]|[yY]) 
			# write file
			echo $(($(date +%s%N)/1000000)) > latestPush
			echo "Writing 'latestPush'"
        ;;
		*)
			echo "Keeping 'latestPush'"
        ;;
	esac 
	
else
	# write file
	echo  $(($(date +%s%N)/1000000)) > latestPush
	echo "Writing 'latestPush'"
fi




# create service?
