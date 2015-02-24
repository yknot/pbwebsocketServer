import json
import requests
import sys
from decimal import *



class PushBullet:
    def __init__(self):
        # try to open apiKey
        try:
            self.apiKey = apiKey = open('apiKey').readline().strip()
        except:
            sys.exit('no apiKey file')
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


    def getPushes(self, since = 1424233995691): # date is 2/17/2015
        # get list of pushes since date provided or default
        data = requests.get(self.url + '?modified_after=' + str(since), auth=(self.apiKey, ''))
        return data.text
        
