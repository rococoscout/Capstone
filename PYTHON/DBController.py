# Controller class to connect to the MySQL database
#
# MIDN 1/C Polmatier

import pymysql #facilitate connection to MySql

class DBController:
    def __init__(self):
        self.cursor, self.db = self.connection()
        # dictionary cursor
        self.dict_cursor = self.db.cursor(pymysql.cursors.DictCursor)

    # Open database connection and return cursor and connection object
    def connection(self):
        db = pymysql.connect(host="midn.cs.usna.edu",
                             user = "m215394",
                             passwd = "greg1018",
                             db = "capstone_chatbot")
        cursor = db.cursor()
        return cursor, db

    # Return a merged dictionary between the Rules and Responses MySQL tables
    def getMergeDict(self):
        # prepare SQL query to select entries from db 
        sql = "SELECT * FROM Merged"
        try:
            # Execute the SQL command
            self.dict_cursor.execute(sql)
            # Fetach all the rows in a list of lists
            all_merged = self.dict_cursor.fetchall()
        except:
            print("Error: unable to fetch data")
            return False
        
        return all_merged

    # Return a dictionary representing the Responses MySQL table
    def getResponsesDict(self):
        # prepare SQL query to select entries from db 
        sql = "SELECT idResponses, idRules, responses FROM Responses"
        try:
            # Execute the SQL command
            self.dict_cursor.execute(sql)
            # Fetach all the rows in a list of lists
            all_responses = self.dict_cursor.fetchall()
        except:
            print("Error: unable to fetch data")
            return False

        return all_responses

    # Return dictionary representation of the Rules MySQL table
    def getRulesDict(self):
        # prepare SQL query to select entries from db 
        sql = "SELECT idRules, rule FROM Rules"
        try:
            # Execute the SQL command
            self.dict_cursor.execute(sql)
            # Fetach all the rows in a list of lists
            all_rules = self.dict_cursor.fetchall()
        except:
            print("Error: unable to fetch data")
            return False

        return all_rules

    # Update Rules MySQL table with new entry 
    def addRule(self,rule):
        try:
            #SQL command
            insertSQL = "INSERT INTO Rules (rule) VALUES (%s)"
            val = (rule)
            # Execute the SQL command
            self.cursor.execute(insertSQL, val)
            self.db.commit()
        except:
            return False

        return True

    def closeDB(self):
        self.db.close()
