#Class for the responses to questions
class Response:
    def __init__(self, answer):
        self.ans=answer #Main answer
        self.Rules=dict() #Collection of rules associated with this answer
        self.Questions=dict() #Collection of questions that matched

    #Returns the Answer
    def getAns(self):
        return self.ans

    #Adds a rule to the collection. Rule is regex as a string
    def setRule(self, rule):
        if rule in self.Rules.keys():
            return
        self.Rules[rule]=0

    #Adds multiple rules. Just to make life easier when adding Rules
    #rules is a list of regex strings
    def setMoreRules(self, rules):
        for rule in rules:
            self.setRule(rule)

    #Adds a quesion that matched to this response
    def addQuestion(self, question):
        if question in self.Questions.keys():
            self.Questions[question] += 1
        self.Questions[question]=0

    #Returns the rules with this Response
    def getRules(self):
        return self.Rules.keys()
