import simplejson
import sys
import MySQLdb as mdb
import requests
from decimal import *
import os


sys.path.append(os.getcwd() + '/py_modules')


# custom modules
from PushBullet import *
from MySQLCursor import *
from Pantry import *


def latestPush(newPushes):
    """update file for latest push timestamp"""
    for p in newPushes['pushes']:
        # write updated latest push
        if 'created' in p:
            g = open('latestPush', 'w')
            g.write(repr(p['created']))
            g.close()
            return


def isRelevant(p):
    '''tests if note has all neccessary parts and is sent to server'''
    if ('title' in p 
        and 'body' in p 
        and 'target_device_iden' in p 
        and p['target_device_iden'] == 'ujA68FT1A28sjAyPxI9Aei'):
        return 1
    else:
        return 0
        

# open file based on argument
f = open(sys.argv[1])

# load as JSON
newPushes = simplejson.load(f)



if 'pushes' not in newPushes:
    sys.exit(0)

# modify latest push file
latestPush(newPushes)


# read in new pushes
# for each command do stuff
for p in newPushes['pushes'][:-1]:
    # if has title, body and target device is server
    if isRelevant(p):
        
        # send back to sender
        if 'source_device_iden' in p:
            iden = p['source_device_iden']
        else:
            iden = ''

        pb = PushBullet(iden)
        sql = MySQLCursor()
    
        # if about pantry
        if p['title'].lower() == 'pantry':            
            pantry = Pantry(pb, sql)

            pantry.cmd(p['body'].split())
            
        
