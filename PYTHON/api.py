# Python Flask program that provides the chatbot website with functional backend
# for database connection and function calling.  
#
# MIDN 1/C Polmatier 

# flask files 
from flask import Flask, request, jsonify
import json
import datetime
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

    ans = getAnswer(inp)

    sql = f'SELECT idRules, answer FROM Answers WHERE answer="{ans}";'
    response = db.fetch(sql)

    return jsonify(response)


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

    sql = f'UPDATE {table} SET {field}="{update}" WHERE {idname} = {int(ID)};'
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

    sql = f'INSERT INTO {table} (IdRules, {field}) VALUES ({int(ID)}, "{newitem}");'
    print(sql)
    db.execute(sql)

    sql = f'SELECT {idname} FROM {table} WHERE {field}="{newitem}";'
    return jsonify(db.fetch(sql))

# add rules
@app.route('/api/entries/rules/edit/rule', methods=['POST'])
@cross_origin()
def api_edit_rule():
    ID = request.form.get('id') # rule id
    title = request.form.get('title')
    description = request.form.get('description')

    sql = f'UPDATE Rules SET title="{title}", description="{description}" WHERE IdRules={int(ID)};'
    print(sql)
    return db.execute(sql)

# returns questions and date created 
@app.route('/api/entries/rules/graph', methods=['POST'])
@cross_origin()
def api_get_graph():
    ID = request.form.get('id') # rule id

    sql = 'SELECT title, count(*) AS Count, Date_FORMAT(dateCreated, "%Y-%m-%d") AS Date '\
            'FROM Questions INNER JOIN Rules ON Questions.idRules = Rules.idRules '\
            f'WHERE Questions.idRules = {ID} '\
            'GROUP BY Date_FORMAT(dateCreated, "%Y-%m-%d"), title;'
    
    l = db.fetch(sql)

    title = l[0]["title"]

    reformat = ()
    extract =['Date', 'Count']
    data = []
    for item in l:
        data.append({key: item[key] for key in extract})
    reformat = (title, data)

    return jsonify(reformat)


# returns questions and date created 
@app.route('/api/entries/rules/top3', methods=['POST'])
@cross_origin()
def api_top3():
    sql = "SELECT idRules "\
                "FROM Questions " \
                "GROUP BY idRules " \
                "ORDER BY COUNT(idRules) DESC " \
                "LIMIT 3;"
    print(sql)

    top3 = Rule.db.fetchNoDict(sql)

    sql = "SELECT title, count(*) AS Count, Date_FORMAT(dateCreated, '%Y-%m-%d') AS Date "\
            "FROM Questions INNER JOIN Rules ON Questions.idRules = Rules.idRules "\
            f"WHERE Questions.idRules IN {tuple(top3)} "\
            "GROUP BY Date_FORMAT(dateCreated, '%Y-%m-%d'), title;"
    
    l = db.fetch(sql)

    top3  = []
    for item in l:
        if item['title'] not in top3:
            top3.append(item['title'])

    newl = {}
    for title in top3:
        newl[title] = []

    extract =['Date', 'Count']
    for item in l:
        newl[item['title']].append({key: item[key] for key in extract})

    return jsonify(newl)




def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

#####################################################################
   
if __name__ == "__main__":
    app.run()

    



