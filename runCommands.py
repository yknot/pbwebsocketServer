import simplejson
import sys
import requests
from decimal import *
import os

# import path for custom modules
sys.path.append(os.getcwd() + '/py_modules')


# custom modules
from PushBullet import *
from Pantry import *


def latestPush(newPushes):
    '''update file for latest push timestamp'''
    for p in newPushes['pushes']:
        # write updated latest push
        if 'created' in p:
            g = open('latestPush', 'w')
            g.write(repr(p['created']))
            g.close()
            return


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
# get user name from arguments        
name = sys.argv[-1]

# new pushbullet object
pb = PushBullet(name)
# get new pushes
try:
    # try to find file
    since = open('latestPush').readline().strip()
except:
    # if file not there use default
    since =  1424750589.433564

# get new pushes
rawJSON = pb.getPushes(since)
newPushes = simplejson.loads(rawJSON)


# if there are no newpushes
if 'pushes' not in newPushes:
    sys.exit(0)

# modify latest push file
latestPush(newPushes)



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
            
