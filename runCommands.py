import json
import sys
import MySQLdb as mdb

# open file based on argument
f = open(sys.argv[1])
# load as JSON
newPushes = json.load(f)

if 'pushes' in newPushes:

    # open file to write commands to ##### XXXXXXXX
    g = open('cmds', 'w')
    h = open('push', 'w')

    # read in new pushes
    # for each command do stuff
    for p in newPushes['pushes']:
        if 'title' in p 
        and 'body' in p 
        and 'target_device_iden' in p 
        and p['target_device_iden'] == 'ujA68FT1A28sjAyPxI9Aei':
            g.write(str(p['title']) + str(p['body'])) ##########XXXXXXXXXXXXXX
            

            # one type of command
            if p['title'] == 'Pantry':

                con = mdb.connect('localhost', 'PBuser', open('mysqlpasswd').readline()[:-1],'PushBullet')
                cur = con.cursor()

                if p['body'].split(' ')[0].lower() == 'list':
                    cur.execcute('select * from PantryItems')
                    data = cur.fetchall()
                    for d in data:
                        h.write(d[1] + ' ' + d[2] + '\n')
                # elif insert
                # elif update
                # elif delete
                            
                    
                
                    
            
            
    # look for first push with created date
    for p in newPushes['pushes']:
        if 'created' in p:
            open('latestPush', 'w').write(str(p['created']))
            break
            
