# Controller class to connect to the MySQL database
#
# MIDN 1/C Polmatier

import pymysql #facilitate connection to MySql

class DBHelper:
    def __init__(self):
        self.host = "midn.cs.usna.edu"
        self.user = "m215394"
        self.password = "greg1018"
        self.db = "capstone_chatbot"

    # Open database connection and return cursor and connection object
    def __connect__(self):
        self.con = pymysql.connect(host=self.host,
                             user = self.user,
                             passwd = self.password,
                             db = self.db,
                             cursorclass=pymysql.cursors.DictCursor)
        
        self.cursor = self.con.cursor()

    def noDictConnect(self):
        self.con = pymysql.connect(host=self.host,
                             user = self.user,
                             passwd = self.password,
                             db = self.db,
                             cursorclass=pymysql.cursors.Cursor)
        
        self.cursor = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.__disconnect__()
        return result

    def fetchNoDict(self, sql):
        self.noDictConnect()
        self.cursor.execute(sql)
        result = [x[0] for x in self.cursor.fetchall()]
        self.__disconnect__()
        return result


    def execute(self, sql):
        self.__connect__()
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except MySQLError as e:
            return f"Error: {e}"
        self.__disconnect__()
        return "SUCCESS"
