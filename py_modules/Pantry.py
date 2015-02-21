from PushBullet import *
#from MySQLCursor import *
import csv
import os.path


class Pantry:
    def __init__(self, pb):
        self.pb = pb
        if os.path.isfile('Pantry.csv'):
            reader = csv.reader(open('Pantry.csv'))

            self.pantry = {}
            for row in reader:
                key = row[0]
                self.pantry[key] = float(row[1])
        else:
            self.pantry = {}



    def list(self):
        # get all items
        
        
        # put in message form
        msg = ''
        for key, value in self.pantry.items():
            msg = msg + key + '\t' + str(value) + '\n'

        return msg



    def add(self, line):
        # the middle items of the command
        item = ' '.join(line[1:len(line)-1]).lower()
        
        if item in self.pantry:
            self.pantry[item] += float(line[-1])
        else:
            self.pantry[item] = float(line[-1])
                
        return 'new value: ' + item + '\t' + str(self.pantry[item])
        

    def remove(self, line):
        # the middle items of the command
        item = ' '.join(line[1:len(line)-1]).lower()
        
        if item in self.pantry:
            if pantry[item] - float(line[-1]) < 0:
                del pantry[item]
                return 'deleted: ' + item
            else:
                self.pantry[item] -= float(line[-1])
            
                
        return 'new value: ' + item + '\t' + str(self.pantry[items])
            

    def cmd(self, body):
        # for each command 
        msg = ''
        for line in body:
            part = line.split()
            # if command is list
            if part[0].lower() == 'list':
                # quit only returning list
                self.pb.PushNote('Pantry', self.list())
                
            elif part[0].lower() == 'add':
                msg += self.add(part)
                
            elif part[0].lower() == 'remove':
                msg += self.remove(part)
            
        self.pb.pushNote('Pantry', msg)


    def save(self):
        with open('dict.csv', 'wb') as f:
            writer = csv.writer(f)
            for key, value in self.pantry.items():
                writer.writerow([key, value])
