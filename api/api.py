import flask
from flask_cors import CORS, cross_origin
from flask import request, jsonify
import sys
sys.path.insert(1, '../Python') # see Python folder
from DBController import DBController as ctlr # Database controller

# establish flask
app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

# --------------------- Methods Begin ------------------------------------

@app.route('/api/entries/rules', methods=['GET'])
@cross_origin()
def api_rules():
    db = ctlr()
    rules = db.getRulesDict()
    db.closeDB()
    # return json array of answers
    return jsonify(rules)

# -----------------------------------------------------------------------

# import regex functions 
#from regex import readRules, getResponse
from regex import Regex

@app.route('/api/input', methods=['POST'])
@cross_origin()
def api_input():
    inp = request.form.get("input")
    
    if not inp:
        return "error: no input arg given"

    db = ctlr()
    merged_dict = db.getMergeDict()
    db.closeDB()

    if not (rules or responses):
        print("ERROR: db connection")
        return "UNSUCCESSFUL"

    # Create Regex object with rules given 
    re = Regex(merged_dict)
    return re.getResponses(inp)


# ----------------------------------------------------------------------
    
@app.route('/api/entries/addRule', methods=['POST'])
@cross_origin()
def api_addRule():
    rule = request.form.get('rule')

    if not rule:
        print ("Error: not all args given")
        return "no arg"

    db = ctlr()
    if not db.addRule(rule):
        print("ERROR: insert")
        return "ERROR: INSERT UNSUCCESSFUL"

    return "INSERT SUCCESSFUL"


#####################################################################
   
if __name__ == "__main__":
    app.run()

    



