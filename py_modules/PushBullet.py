import json
import requests
import sys
from decimal import *



class Pushbullet:
    def __init__(self, iden):
        self.apiKey = apiKey = open('apiKey').readline().strip()
        self.url = "https://api.pushbullet.com/v2/pushes"
        self.iden = iden


    def pushNote(self, title, body):
        
        data = json.dumps({'type':'note'
                           , 'title':title
                           , 'body': body
                           , 'device_iden': self.iden})

        r = requests.post(url
                          , data
                          , auth=(apiKey,'')
                          , headers = {'content-type': 'application/json'})



        
