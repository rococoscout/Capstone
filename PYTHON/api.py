# Python Flask program that provides the chatbot website with functional backend
# for database connection and function calling.  
#
# MIDN 1/C Polmatier 

# flask files 
from flask import Flask, request, jsonify
import json
from flask_cors import CORS, cross_origin # handle Cross Origin Resource Sharing (CORS) [for AJAX]
# Project files 
from dbhelper import DBHelper # Database controller
from rule import Rule   # Handle rule format in db 
from regex import Regex # Regex functions

# establish flask
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

# establish database
db = DBHelper()

# --------------------- Methods Begin ------------------------------------

# return rules
@app.route('/api/entries/rules', methods=['GET'])
@cross_origin()
def api_rules():
    # return json array of answers
    return jsonify(Rule.getRulesDict())

# -----------------------------------------------------------------------

# return chatbot answer 
@app.route('/api/input', methods=['POST'])
@cross_origin()
def api_input():
    inp = request.form.get("input")
    
    if not inp:
        return "error: no input arg given"

    

# ----------------------------------------------------------------------

# insert rule into database
@app.route('/api/entries/addRule', methods=['POST'])
@cross_origin()
def api_addRule():
    regexes = json.loads(request.form.get('regexes'))
    title = request.form.get('title')
    description = request.form.get('description')
    answers = json.loads(request.form.get('answers'))
    questions = json.loads(request.form.get('questions'))

    # if not rule:
    #     print ("Error: not all args given")
    #     return "no arg"
    r = Rule(regexes, answers, questions, title, description)
    return r.addRule()

# -----------------------------------------------------------------------

# delete rules
@app.route('/api/entries/rules/delete', methods=['POST'])
@cross_origin()
def api_delete():
    ruleID = request.form.get('id')
    
    sql = f"DELETE FROM Rules WHERE IdRules = {int(ruleID)};"
    return db.execute(sql)

# -----------------------------------------------------------------------

# update
@app.route('/api/entries/rules/update', methods=['POST'])
@cross_origin()
def api_update():
    #figure out how to get everything but just get what I wanted
    regexes = json.loads(request.form.get('regexes'))
    title = request.form.get('title')
    description = request.form.get('description')
    answers = json.loads(request.form.get('answers'))
    questions = json.loads(request.form.get('questions'))
    ruleID = request.form.get('id')

    # delete the old rule
    sql = f"DELETE FROM Rules WHERE IdRules = {int(ruleID)};"
    db.execute(sql)
    
    # add the new one. 
    r = Rule(regexes, answers, questions, title, description)
    return r.addRule()

    
#####################################################################
   
if __name__ == "__main__":
    app.run()

    



