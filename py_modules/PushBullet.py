import simplejson
import json
import requests
import sys
import logging


class PushBullet:
    def __init__(self, name):
        """Open apiKey file to get the key for the right user"""
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

        logging.getLogger('requests').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING)


    def setIden(self, iden):
        """Set the identity of the device that the response will be sent to"""
        # set the iden to send response to
        self.iden = iden


    def pushNote(self, title, body):
        """Send the response back"""
        # form data for request
        data = json.dumps({'type':'note'
                           , 'title':title
                           , 'body': body
                           , 'device_iden': self.iden})

        # send push
        r = requests.post(self.url
                          , data
                          , auth=(self.apiKey, '')
                          , headers = {'content-type': 'application/json'})

    def deleteNote(self, pushIden):
        """Deletes the request note"""
        r = requests.delete(self.url + '/' + pushIden
                          , auth=(self.apiKey,'')
                          , headers = {'content-type': 'application/json'})



    def getPushes(self, since):
        """Pulls the list of pushes since the given date"""
        # get list of pushes since date provided or default
        data = requests.get(self.url + '?modified_after=' + str(since), auth=(self.apiKey, ''))
        return data.text
