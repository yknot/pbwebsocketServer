import json
import sys
import MySQLdb as mdb
import requests
from decimal import *


# open file based on argument
f = open(sys.argv[1])
# get static passwds
apiKey = open('apiKey').readline()[:-1]
mysqlpasswd = open('mysqlpasswd').readline()[:-1]
# load as JSON
newPushes = json.load(f)

if 'pushes' not in newPushes:
    sys.exit(0)


# modify latest push
for p in newPushes['pushes']:
    # write updated latest push
    if 'created' in p:
        g = open('latestPush', 'w')
        g.write(repr(p['created']))
        g.close()
        
        break



# read in new pushes
# for each command do stuff
for p in newPushes['pushes'][:-1]:
    # if has title, body and target device is server
    if ('title' in p 
        and 'body' in p 
        and 'target_device_iden' in p 
        and p['target_device_iden'] == 'ujA68FT1A28sjAyPxI9Aei'):
        
    
    
        # if about pantry
        if p['title'].lower() == 'pantry':
            # api url
            url = "https://api.pushbullet.com/v2/pushes"
            
            # mysql connection
            con = mdb.connect('localhost', 'PBuser', mysqlpasswd,'PushBullet')
            # cursor
            cur = con.cursor()
            
            # body of the message
            body = p['body'].split(' ')
        
            # if command is list
            if body[0].lower() == 'list':
                
                # get all items
                cur.execute('select * from PantryItems')
                rows = cur.fetchall()
                
                
                msg = ''
                
                for r in rows:
                    msg = msg + r[1] + ' ' + str(r[2]) + '\n'

                
                # send back to sender
                if 'source_device_iden' in p:
                    iden = p['source_device_iden']
                else:
                    iden = ''
                    

                # note, title, msg, device
                data = json.dumps({'type':'note'
                                   , 'title':'Pantry'
                                   , 'body': msg
                                   , 'device_iden': iden})
                # send push back
                r = requests.post(url
                                  , data
                                  , auth=(apiKey,'')
                                  , headers = {'content-type': 'application/json'})
                
                
            elif body[0].lower() == 'add':
                item = ' '.join(body[1:len(body)-1]).lower()
                cur.execute('select * from PantryItems where ItemName = \'' + item + '\'')
                result = cur.fetchall()


                if result:
                    num = result[0][2] + Decimal(body[-1])
                    
                    with con:
                        cur.execute('update PantryItems set Quantity = ' 
                                    + str(num)
                                    + ' where ItemName = \'' 
                                    + item + '\'')
                    
                else:
                    with con:
                        cur.execute('insert into PantryItems(ItemName, Quantity) values (\'' 
                                    + item 
                                    + '\', ' 
                                    + str(body[-1]) + ')')

                cur.execute('select * from PantryItems where ItemName = \'' + item + '\'')
                result = cur.fetchall()
                
                
                msg = result[0][1] + ' ' + str(result[0][2])
                

                # send back to sender
                if 'source_device_iden' in p:
                    iden = p['source_device_iden']
                else:
                    iden = ''
                    

                # note, title, msg, device
                data = json.dumps({'type':'note'
                                   , 'title':'Pantry'
                                   , 'body': msg
                                   , 'device_iden': iden})
                # send push back
                r = requests.post(url
                                  , data
                                  , auth=(apiKey,'')
                                  , headers = {'content-type': 'application/json'})

            
            
            
            
            
            
                    
                    
