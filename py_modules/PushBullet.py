import simplejson
import json
import requests
import sys
from decimal import *



class PushBullet:
    def __init__(self, name):
        # try to open apiKey
        try:
            rawConfig = open('pbwebsocketServer.config').read()
            config = simplejson.loads(rawConfig)
            self.apiKey = config[name]['APIKey']
            self.device_iden = config[name]['DeviceId']
        except:
            sys.exit('no config file')
        # url for pushes
        self.url = "https://api.pushbullet.com/v2/pushes"

        
    def setIden(self, iden):
        # set the iden to send response to
        self.iden = iden


    def pushNote(self, title, body):
        # form data for request
        data = json.dumps({'type':'note'
                           , 'title':title
                           , 'body': body
                           , 'device_iden': self.iden})

        # send push
        r = requests.post(self.url
                          , data
                          , auth=(self.apiKey,'')
                          , headers = {'content-type': 'application/json'})

    def deleteNote(self, pushIden):
        r = requests.delete(self.url + '/' + pushIden
                          , auth=(self.apiKey,'')
                          , headers = {'content-type': 'application/json'})
                    


    def getPushes(self, since = 1424750589.433564): 
        # get list of pushes since date provided or default
        data = requests.get(self.url + '?modified_after=' + str(since), auth=(self.apiKey, ''))
        return data.text
        
