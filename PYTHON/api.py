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
#from rule import Rule   # Handle rule format in db 
from response import Rule, getAnswer
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

    return getAnswer(inp)


# return chat bot answer 
@app.route('/api/rules/search', methods=['POST'])
@cross_origin()
def api_search():
    search = request.form.get("search")
    
    if not search:
        return "error: no search arg given"

    
    return jsonify(Rule.getRulesDict(search))
    

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

# delete rules
@app.route('/api/entries/rules/edit/delete', methods=['POST'])
@cross_origin()
def api_edit_delete():
    ID = request.form.get('id') # answer, question, regex id
    table = request.form.get('table')

    idname = 'Id' + str(table)

    sql = f"DELETE FROM {table} WHERE {idname} = {int(ID)};"
    print(sql)
    return db.execute(sql)

# update rules
@app.route('/api/entries/rules/edit/update', methods=['POST'])
@cross_origin()
def api_edit_update():
    ID = request.form.get('id') # answer, question, regex id
    table = request.form.get('table')
    update = request.form.get('update')

    field = table.lower()[:-1]
    if (field == 'regexe'):
        field = field[:-1]

    idname = 'Id' + str(table)
    print(field, idname)

    sql = f"UPDATE {table} SET {field}='{update}' WHERE {idname} = {int(ID)};"
    print(sql)
    return db.execute(sql)

# add rules
@app.route('/api/entries/rules/edit/add', methods=['POST'])
@cross_origin()
def api_edit_add():
    ID = request.form.get('id') # rule id
    table = request.form.get('table')
    newitem = request.form.get('newitem')

    field = table.lower()[:-1]
    if (field == 'regexe'):
        field = field[:-1]

    idname = 'Id' + str(table)
    print(field, idname)

    sql = f"INSERT INTO {table} (IdRules, {field}) VALUES ({int(ID)}, '{newitem}');"
    print(sql)
    db.execute(sql)

    sql = f"SELECT {idname} FROM {table} WHERE {field}='{newitem}';"
    return db.fetch(sql)

# add rules
@app.route('/api/entries/rules/edit/rule', methods=['POST'])
@cross_origin()
def api_edit_rule():
    ID = request.form.get('id') # rule id
    title = request.form.get('title')
    description = request.form.get('description')

    sql = f"UPDATE Rules SET title='{title}', description='{description}' WHERE IdRules={int(ID)};"
    print(sql)
    return db.execute(sql)

# returns questions and date created 
@app.route('/api/entries/rules/graph', methods=['POST'])
@cross_origin()
def api_get_graph():
    ID = request.form.get('id') # rule id

    sql = f"SELECT (question, dateCreated) FROM Questions WHERE IdRules={int(ID)};"
    print(sql)
    return db.fetch(sql)




#####################################################################
   
if __name__ == "__main__":
    app.run()

    



