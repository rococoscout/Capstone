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
    # connect to the database
    cursor, db = connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # prepare SQL query to select entries from db 
    sql = "SELECT ruleID, title, rule, description FROM Rules"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetach all the rows in a list of lists
        all_rules = cursor.fetchall()

        # return json array of answers
        return jsonify(all_rules)
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()

# need to look into python path folder. 
import sys
sys.path.insert(1, '../Python')
# import regex functions 
from regex import readRules, getResponse

readRules('rule.txt')

@app.route('/api/input', methods=['POST'])
@cross_origin()
def api_input():
    inp = request.form.get("input")
    
    if not inp:
        return "error: no input arg given"

    return getResponse(inp)
    
    
@app.route('/api/entries/addRule', methods=['POST'])
def api_addRule():
    query_parameters = request.args

    rule = query_parameters.get('rule')
    title = query_parameters.get('title')
    description = query_parameters.get('description')

    if not (rule or title or description):
        print ("Error: not all args given")
        return
    
    # connect to the database
    cursor, db = connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # prepare SQL query to select entries from db 
    sql = "INSERT INTO Rules (title, rule, description) VALUES (%s, %s, %s)"
    try:
        # Execute the SQL command
        cursor.execute(sql, (title,rule,description))
    except:
        print("Error: unable to fetch data")
        return "INSERT UNSUCCESSFUL"

    # disconnect from server
    db.close()
    return "INSERT SUCCESSFUL"

#app.run("0.0.0.0", "5000")