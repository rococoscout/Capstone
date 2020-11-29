import flask
from flask_cors import CORS, cross_origin
import pymysql.cursors
from flask import request, jsonify
from dbconn import connection

app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True





@app.route('/api/entries/rules', methods=['GET'])
@cross_origin()
def api_rules():   
    rules = getRulesDict()
    # return json array of answers
    return jsonify(all_rules)





# need to look into python path folder. 
import sys
sys.path.insert(1, '../Python')
# import regex functions 
#from regex import readRules, getResponse
from regex import Regex

@app.route('/api/input', methods=['POST'])
@cross_origin()
def api_input():
    inp = request.form.get("input")
    
    if not inp:
        return "error: no input arg given"
    
    merged_dict = getMergeDict()

    if not (rules or responses):
        print("ERROR: db connection")
        return "UNSUCCESSFUL"

    # Create Regex object with rules given 
    re = Regex(merged_dict)
    return re.getResponses(inp)



    
@app.route('/api/entries/addRule', methods=['POST'])
@cross_origin()
def api_addRule():
    rule = request.form.get('rule')

    if not rule:
        print ("Error: not all args given")
        return "no arg"
    
    # connect to the database
    try:
        cursor, db = connection()
        #SQL command
        insertSQL = "INSERT INTO Rules (rule) VALUES (%s)"
        val = (rule)
        # Execute the SQL command
        cursor.execute(insertSQL, val)
        db.commit()
    except:
        print("Error: unable to fetch data")
        return "INSERT UNSUCCESSFUL"

    # disconnect from server
    db.close()
    return "INSERT SUCCESSFUL"

#app.run("0.0.0.0", "5000")

#--------------------HELPER----------------------------------
def getRulesDict():
    # connect to the database
    cursor, db = connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # prepare SQL query to select entries from db 
    sql = "SELECT idRules, rule FROM Rules"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetach all the rows in a list of lists
        all_rules = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
        return False

    db.close()
    return all_rules
    
def getResponsesDict():
    # connect to the database
    cursor, db = connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # prepare SQL query to select entries from db 
    sql = "SELECT idResponses, idRules, responses FROM Responses"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetach all the rows in a list of lists
        all_responses = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
        return False

    db.close()
    return all_responses

def getMergeDict():
    # connect to the database
    cursor, db = connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # prepare SQL query to select entries from db 
    sql = "SELECT * FROM Merged"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetach all the rows in a list of lists
        all_merged = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
        return False

    db.close()
    return all_merged
