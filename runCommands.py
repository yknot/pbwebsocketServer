import simplejson
import json
import sys
import requests
from decimal import *
import os
import time

# import path for custom modules
sys.path.append(os.getcwd() + '/py_modules')


# custom modules
from PushBullet import *
from Pantry import *

def getLatestPushDateTimeJSON():
    ''' if it exists, open the json file containing the last datetime stamp for all users '''
    try:
        # open the json file containing last update datetime by user name 
        jsonFile = open("latestPush.json", "r")
        json_data = json.load(jsonFile)
        jsonFile.close()
        return json_data

    except:
        # if file not there use default
        json_data = json.loads('{}')
        return json_data

def getLastPushDatetimeForUser(name):
    ''' find last update datetime for this user or return a default '''
    json_data = getLatestPushDateTimeJSON()
    if 'name' in json_data:
        return json_data[name]
    else:
        # return 24 hours prior in seconds
        return time.time()-86400


def saveLatestPushDatetime(name, datetimestamp):
    '''update file for latest push timestamp'''
    # write updated latest push for this user
    json_data = getLatestPushDateTimeJSON()
        
    # create or update the last update datetime for this user 
    json_data[name] = datetimestamp
    
    # save the json back to the file 
    jsonFile = open("latestPush.json", "w")
    jsonFile.write(json.dumps(json_data))
    jsonFile.close()


def isRelevant(p, pb):
    '''tests if note has all neccessary parts and is sent to server'''
    # title and body mean note
    # target device iden is server
    if ('title' in p 
        and 'body' in p 
        and 'target_device_iden' in p 
        and p['target_device_iden'] == pb.device_iden):
        return 1
    else:
        return 0
        

def updatePantryContents(name, newPushes):
    '''Reads the push messages and updates pantry'''
    # for each command do stuff 
    for p in newPushes['pushes'][:-1]:

        # if has title, body and target device is server
        if isRelevant(p, pb):
            
            # set to send back to sender
            if 'source_device_iden' in p:
                iden = p['source_device_iden']
            else:
                iden = ''

            # sets the reciever
            pb.setIden(iden)
        
            # if about pantry
            if p['title'].lower() == 'pantry':
                # create pantry
                pantry = Pantry(pb)
                # run commands
                pantry.cmd(p['body'].splitlines())
                # save the pantry
                pantry.save()

                pb.deleteNote(p['iden'])

                # save this datetime stamp ("created") for this user to the lastPush file
                saveLatestPushDatetime(name, p['created'])

def main():
    # get user name from arguments
    if sys.argv[-1] == 'runCommands.py':
        sys.exit('missing name argument')
    name = sys.argv[-1]

    # new pushbullet object
    pb = PushBullet(name)

    # get last datetime saved for this user name
    since = getLastPushDatetimeForUser(name)

    # get new pushes for this user name
    rawJSON = pb.getPushes(since)
    newPushes = simplejson.loads(rawJSON)

    # if there are no new pushes
    if 'pushes' not in newPushes:
        sys.exit(0)

    updatePantryContents(name, newPushes)
            

    # modify latest push file
    saveLatestPushDatetime(name, newPushes['pushes'][0]['created'])



if __name__ == "__main__":
    main()
