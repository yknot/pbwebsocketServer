from PushBullet import *
#from MySQLCursor import *
import csv


class Pantry:
    def __init__(self, pb):
        self.pb = pb
        reader = csv.reader(open('Pantry.csv'))

        self.pantry = {}
        for row in reader:
            key = row[0]
            self.pantry[key] = float(row[1])



    def list(self):
        # get all items
        
        
        # put in message form
        msg = ''
        for key, value in self.pantry.items():
            msg = msg + key + '\t' + str(value) + '\n'

        return msg



    def add(self, body):
        # the middle items of the command
        item = ' '.join(body[1:len(body)-1]).lower()
        
        if item in self.pantry:
            self.pantry[item] += float(body[-1])
        else:
            self.pantry[item] = float(body[-1])
                
        return  item + '\t' + str(self.pantry[item])
        
            

    def cmd(self, body):
        # if command is list
        if body[0].lower() == 'list':
            msg = self.list()
                
        elif body[0].lower() == 'add':
            msg = self.add(body)
            
        self.pb.pushNote('Pantry', msg)


    def save(self):
        with open('dict.csv', 'wb') as f:
            writer = csv.writer(f)
            for key, value in self.pantry.items():
                writer.writerow([key, value])
