import json
import sys


f = open(sys.argv[1])
newPushes = json.load(f)


g = open('cmds', 'w')


# read in new pushes
# for each command do stuff
for p in newPushes['pushes']:
    if 'title' in p:
        if 'body' in p:
            if 'target_device_iden' in p:
                if p['target_device_iden'] == 'ujA68FT1A28sjAyPxI9Aei':
                    g.write(str(p['title']) + str(p['body']))





if 'created' in newPushes['pushes'][0]:
    open('latestPush', 'w').write(str(newPushes['pushes'][0]['created']))

