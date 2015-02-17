from PushBullet import *
from MysqlCursor import *


class Pantry:
    def __init__(self, pb, sql):
        self.pb = pb
        self.sql = sql


    def list(self):
        # get all items
        rows = sql.ssf('PantryItems')
        
        # put in message form
        msg = ''
        for r in rows:
            msg = msg + r[1] + ' ' + str(r[2]) + '\n'

        return msg



    def add(self, body):
        # the middle items of the command
        item = ' '.join(body[1:len(body)-1]).lower()
        
        where = {}
        where['ItemName'] = "'" + item + "'"

        result = self.sql.ssfw('PantryItems', where)
        
        
        if result:
            num = result[0][2] + Decimal(body[-1])
            
            self.sql.execute('update PantryItems set Quantity = ' 
                             + str(num)
                             + ' where ItemName = \'' 
                             + item + '\'')
                
        else:
            self.sql.execute('insert into PantryItems(ItemName, Quantity) values (\'' 
                             + item 
                             + '\', ' 
                             + str(body[-1]) + ')')

        result = self.sql.ssfw('PantryItems', where)
                
        return result[0][1] + ' ' + str(result[0][2])
        
            

    def cmd(self, body):
        # if command is list
        if body[0].lower() == 'list':
            msg = self.list()
                
        elif body[0].lower() == 'add':
            msg = self.add(body)
            
        self.pb.pushNote('Pantry', msg)
            
            
