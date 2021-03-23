# A class to store a Rule, based on the capstone Schema
# MIDN 1/C Polmatier
from dbhelper import DBHelper
import json
import numpy as np

class Rule:
    db = DBHelper()
    def __init__(self, regexes, answers, questions, title, description, ID = None, vector = np.zeros(50)):
        self.id = ID                # rule ID
        self.regexes = regexes      # List of Regular Expression
        self.answers = answers      # List of answers based on the Rule
        self.questions = questions  # List of questions that have been asked that asssociate with the rule
        self.vector = vector        # The total vector representation of the list of Questions
        self.title = title
        self.description = description


    '''
    update total vector of this Rule in the database
    '''
    def updateVector(self):
        json_v = json.dumps(self.vector.tolist())
        sql = f'UPDATE Rules SET totalVector="{json_v}" WHERE idRules={self.id};'
        return Rule.db.execute(sql)


    '''
    Updates regex and total vector into the database schema
    
    def updateRule(self):
        json_v = json.dumps(self.vector.tolist())
        sql = f"UPDATE Rules SET regex='{self.regex}' totalVector='{json_v}' WHERE idRules={self.id};"
        return None
    '''

    def addQuestion(self, q):
        sql = f'INSERT INTO Questions (question, idRules) VALUES ("{q}", {self.id});'
        print(sql)
        return Rule.db.execute(sql)

    def addAnswer(self, a):
        sql = f'INSERT INTO Answers (answer, idRules) VALUES ("{a}", {self.id});'
        return Rule.db.execute(sql)

    def addRegex(self, r):
        sql = f'INSERT INTO Regexes (regex, idRules) VALUES ("{r}", {self.id});'
        return Rule.db.execute(sql)

    def addRule(self):
        # add to rule table
        json_vec = []
        if self.vector is not None:
            json_vec = json.dumps(self.vector.tolist())
        sql = f'INSERT INTO Rules (title, description, totalVector) VALUES ("{self.title}", "{self.description}", "{json_vec}");'

        print(sql)
        print(Rule.db.execute(sql))

        # get ID
        sql = f'SELECT idRules FROM Rules WHERE title="{self.title}";'
        print(sql)
        print(Rule.db.fetchNoDict(sql))
        self.id = Rule.db.fetchNoDict(sql)[0]

        # add to questions table
        [self.addQuestion(q) for q in self.questions]
        # add to answers table
        [self.addAnswer(a) for a in self.answers]
        # add to regexes table
        [self.addRegex(r) for r in self.regexes]

        return "SUCCESS"

    '''
    Function returns all the rules in the database including regex(if exists),
    list of answers, list of questions, and the total vector

    Returns a list of class Rules
    '''
    @staticmethod
    def getRules(isNumpy=True, s=None):
        rules = []

        # get rules from sql
        if s is None:
            sql = "SELECT idRules, totalVector, title, description FROM Rules;"
        else:
            sql = f'SELECT idRules, totalVector, title, description FROM Rules WHERE title LIKE "%{s}%";'
        print(sql)
        ruleEntries = Rule.db.fetch(sql)

        # for all rules
        for r in ruleEntries:
            # get id, totalVector, and regex
            ID = r['idRules']
            vec = r['totalVector']
            if vec is not None:
                if isNumpy:
                    vec = np.asarray(json.loads(r['totalVector']))
                else:
                    vec = json.loads(r['totalVector'])
            title = r['title']
            des   = r['description']

            # based off id get list of regexes
            sql = f"SELECT regex FROM Regexes WHERE Regexes.idRules = {ID};"
            rs = Rule.db.fetchNoDict(sql)

            # based off id get list of questions
            sql = f"SELECT DISTINCT question FROM Questions WHERE idRules = {ID} AND isExample = TRUE;"
            qs = Rule.db.fetchNoDict(sql)

            # based off id get list of answers
            sql = f"SELECT answer FROM Answers WHERE Answers.idRules = {ID};"
            ans = Rule.db.fetchNoDict(sql)

            # create Rule object and append
            rules.append(Rule(rs, ans, qs, title, des, ID, vec))

        # return list
        return rules

    @staticmethod
    def getRulesDict(search=None):
        rs = Rule.getRules(isNumpy=False, s=search)
        x=True
        for r in rs:
            ID = r.id

            r.vector = [] 

            # based off id get list of regexes
            sql = f"SELECT regex, idRegexes FROM Regexes WHERE Regexes.idRules = {ID};"
            r.regexes = Rule.db.fetch(sql)

            # based off id get list of questions
            sql = f"SELECT DISTINCT question, idQuestions FROM Questions WHERE Questions.idRules = {ID} and isExample = TRUE GROUP BY question;"
            if x:
                print(sql)
                x = False

            r.questions = Rule.db.fetch(sql)

            # based off id get list of answers
            sql = f"SELECT answer, idAnswers, flagCount FROM Answers WHERE Answers.idRules = {ID};"
            r.answers = Rule.db.fetch(sql)

        return [vars(r) for r in rs]

    

    @staticmethod
    def addUnmatchedQuestion(q):
        sql = f'INSERT INTO Questions (question) VALUES ("{q}");'
        return Rule.db.execute(sql)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
 



if __name__ == "__main__":
    
    sql = "SELECT title, count(*) AS Count, Date_FORMAT(dateCreated, '%Y-%m-%d') AS Date "\
            "FROM Questions INNER JOIN Rules ON Questions.idRules = Rules.idRules "\
            f"WHERE Questions.idRules = 104 "\
            "GROUP BY Date_FORMAT(dateCreated, '%Y-%m-%d'), title;"

    l = Rule.db.fetch(sql)

    title = l[0]["title"]

    reformat = ()
    extract =['Date', 'Count']
    data = []
    for item in l:
        data.append({key: item[key] for key in extract})
    reformat = (title, data)

    print(json.dumps(reformat))