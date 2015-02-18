import json
import requests
import sys
from decimal import *



class PushBullet:
    def __init__(self):
        self.apiKey = apiKey = open('apiKey').readline().strip()
        self.url = "https://api.pushbullet.com/v2/pushes"

    def setIden(self, iden):
        self.iden = iden


    def pushNote(self, title, body):
        data = json.dumps({'type':'note'
                           , 'title':title
                           , 'body': body
                           , 'device_iden': self.iden})

        r = requests.post(self.url
                          , data
                          , auth=(self.apiKey,'')
                          , headers = {'content-type': 'application/json'})


    def getPushes(self, since = 1424233995691): # date is 2/17/2015
        data = requests.get(self.url + '?modified_after=' + str(since), auth=(self.apiKey, ''))
        return data.text
        
