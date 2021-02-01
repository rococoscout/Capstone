# A class to store a Rule, based on the capstone Schema 
# MIDN 1/C Polmatier
from dbhelper import DBHelper
import json

class Rule:
    db = DBHelper()
    def __init__(self, ID, regexes, answers, questions, vector, title, description):
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
        json_v = json.dumps(self.vector)
        print(json_v)
        sql = f"UPDATE Rules SET totalVector='{json_v}' WHERE idRules={self.id};"
        return Rule.db.execute(sql)


    '''
    Updates regex and total vector into the database schema 
    '''
    def updateRule(self):
        json_v = json.dumps(self.vector)
        sql = f"UPDATE Rules SET regex='{self.regex}' totalVector='{json_v}' WHERE idRules={self.id};"
        return Rule.db.execute(sql)
        return None

    def addQuestion(self, q):
        sql = f"INSERT INTO Questions (question, idRules) VALUES ('{q}', {self.id});"
        return Rule.db.execute(sql)


    '''
    Function returns all the rules in the database including regex(if exists), 
    list of answers, list of questions, and the total vector

    Returns a list of class Rules
    '''
    @staticmethod
    def getRules():
        rules = []

        # get rules from sql
        sql = "SELECT idRules, totalVector, title, description FROM Rules;"
        ruleEntries = Rule.db.fetch(sql)

        #print(ruleEntries)
        # for all rules
        for r in ruleEntries:
            # get id, totalVector, and regex 
            ID = r['idRules']
            vec = json.loads(r['totalVector'])
            title = r['title']
            des   = r['description']

            # based off id get list of questions
            sql = f"SELECT regex FROM Regexes WHERE Regexes.idRules = {ID};"
            rs = Rule.db.fetchNoDict(sql)

            # based off id get list of questions
            sql = f"SELECT question FROM Questions WHERE Questions.idRules = {ID};"
            qs = Rule.db.fetchNoDict(sql)

            # based off id get list of answers
            sql = f"SELECT answer FROM Answers WHERE Answers.idRules = {ID};"
            ans = Rule.db.fetchNoDict(sql)

            # create Rule object and append
            rules.append(Rule(ID, rs, ans, qs, vec, title, des))
        
        # return list
        return rules

    @staticmethod
    def addUnmatchedQuestion(q):
        sql = f"INSERT INTO Questions (question) VALUES ('{q}');"
        return Rule.db.execute(sql)

    @staticmethod
    def getRulesDict():
        rs = Rule.getRules()
        return [vars(r) for r in rs]

if __name__ == "__main__":
    print(Rule.getRulesDict())