import MySQLdb as mdb



class Mysqlcursor:
    def __init__(self):
        mysqlpasswd = open('mysqlpasswd').readline().strip()
        self.con = mdb.connect('localhost', 'PBuser', mysqlpasswd,'PushBullet')
        self.cur = con.cursor()

    def ssf(self, table):
        return self.execute('select * from ' + table)

    def ssfw(self, table, where):
        # beginning
        cmd = 'select * from ' + table + ' where '
        # list of wheres
        w = []
        # for each where command format
        for key in where:
            w.append(str(key) + ' = ' + str(a[key]))
        # join and add to beginning
        cmd = cmd + ', '.join(w)
        return self.execute(cmd)

    def execute(self, cmd):
        with con:
            self.cur.execute(cmd)
        return cur.fetchall()
