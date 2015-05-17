from py_modules.PushBullet import *
import csv
import logging
import os.path


class Pantry:
    def __init__(self, pb):
        """Initializes Pantry with pusbullet object to communicate via"""
        # pusbullet object
        self.pb = pb
        # if file exists read in
        if os.path.isfile('Pantry.csv'):

            reader = csv.reader(open('Pantry.csv'))

            self.pantry = {}
            # each row is a set of key and value
            for row in reader:
                key = row[0]
                self.pantry[key] = float(row[1])

        # else create dictionary
        else:
            self.pantry = {}

        logging.basicConfig(filename='pushbullet.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)


    def log(self, cmd):
        """logs the command that was just run"""

        self.logger.info("Command:" + cmd[0])


    def list(self):
        """Gets the pantry list from the csv and turns it into a note format"""

        msg = ''
        for key, value in self.pantry.items():
            msg = msg + key + '\t' + str(value) + '\n'

        return msg


    def add(self, line):
        """Runs add command with line as the command"""
        # the middle parts of the command are the item
        item = ' '.join(line[1:len(line)-1]).lower()

        # if the item exists add to existing
        if item in self.pantry:
            self.pantry[item] += float(line[-1])
        # else create new item
        else:
            self.pantry[item] = float(line[-1])

        # return the new value
        return 'new value: ' + item + '\t' + str(self.pantry[item]) + '\n'


    def remove(self, line):
        """Runs remove command with line as the command"""
        # the middle parts of the command are the item
        item = ' '.join(line[1:len(line)-1]).lower()

        # if the item exists remove from existing
        if item in self.pantry:
            # if removing more than exist delete
            if self.pantry[item] - float(line[-1]) <= 0:
                del self.pantry[item]
                return 'deleted: ' + item + '\n'
            # else remove from existing
            else:
                self.pantry[item] -= float(line[-1])
        # else does not exist
        else:
            return item + ' does not exist'

        # return new value
        return 'new value: ' + item + '\t' + str(self.pantry[item]) + '\n'


    def cmd(self, body):
        """Loops through the commands given in the message body"""
        # for each command
        msg = ''
        for c in body:
            cmd = c.split()
            if cmd[0].lower() == 'list':
                msg += self.list()

            elif cmd[0].lower() == 'add':
                msg += self.add(cmd)

            elif cmd[0].lower() == 'remove':
                msg += self.remove(cmd)
            else:
                msg += 'Command not found\n'

            self.log(cmd)

        # push note back to sender with title and message
        self.pb.pushNote('Pantry', msg)


    def save(self):
        """Save the pantry contents to csv"""
        # save the pantry in csv file
        with open('Pantry.csv', 'wb') as f:
            writer = csv.writer(f)
            for key, value in self.pantry.items():
                writer.writerow([key, value])
