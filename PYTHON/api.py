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
    idname = 'Id' + str(table)
    print(field, idname)

    sql = f"INSERT INTO {table} (IdRules, {field}) VALUES ({int(ID)}, '{newitem}');"
    print(sql)
    return db.execute(sql)

# add rules
@app.route('/api/entries/rules/edit/rule', methods=['POST'])
@cross_origin()
def api_edit_add():
    ID = request.form.get('id') # rule id
    title = request.form.get('title')
    description = request.form.get('description')


    sql = f"UPDATE Rules SET title='{title}', description='{description}' WHERE IdRules={int(ID)};"
    print(sql)
    return db.execute(sql)

# update
# @app.route('/api/entries/rules/update', methods=['POST'])
# @cross_origin()
# def api_update():
#     #figure out how to get everything but just get what I wanted
#     regexes = json.loads(request.form.get('regexes'))
#     title = request.form.get('title')
#     description = request.form.get('description')
#     answers = json.loads(request.form.get('answers'))
#     # might just have jess send me a tuple of questions like i send him
#     questions = json.loads(request.form.get('questions'))
#     ruleID = request.form.get('id')

#     # UPDATE title and description
#     sql = f"UPDATE Rules SET title='{title}', Description='{description}' WHERE IdRules = {int(ruleID)};"
#     db.execute(sql)

#     # for each question that matches ruleID update
#     # NOT DONE - waiting to see what Jess will send me
#     # also this will get broken up into different api functions
#     for q in questions:
#         sql = f"UPDATE Questions SET question='{q}' WHERE IdRules = {int(ruleID)};"

#     # for each regex that matches ruleID update
#     for r in regexes:
#         sql = f"UPDATE Regexes SET regex='{r}' WHERE IdRules = {int(ruleID)};"

#     # for each answer that matches ruleID update
#     for a in answers:
#         sql = f"UPDATE Answers SET answer='{a}' WHERE IdRules = {int(ruleID)};"



#     # add the new one. 
#     r = Rule(regexes, answers, questions, title, description)
#     return r.addRule()

# update
@app.route('/api/entries/rules/update', methods=['POST'])
@cross_origin()
def api_update():
#####################################################################
   
if __name__ == "__main__":
    app.run()

    



