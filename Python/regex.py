
import re
import sys
from response import Response

Dict = dict() #Dictionary of responses
unknownQuestions=dict() #Dictionary of unanswered questions

#Reads the rules from the given file.
#Rules in the file should be in this format:
#Rule1;Rule2;RuleETC:Answer
def readRules(filename):
    fo = open(filename, 'r')

    rules = list()
    lines = fo.readlines()

    for line in lines:
        values = line.split(":")
        rules = values[0].split(";")

        #Creates a response class for each response.
        response= Response(values[1])
        response.setMoreRules(rules)
        Dict[response]=0

    fo.close()


def getResponse(sentence):
    flag = True
    answer = "I'm not too sure"
    #Iterates through the responses
    for ans in Dict.keys():
        #Iterates through the rules in the responses
        for rule in ans.getRules():
            #Checks if the sentence matches the rule
            x=re.search(rule, sentence)
            if x:
                answer = ans.getAns()
                #Adds the question to collection of questions with that rule
                ans.addQuestion(sentence)
                flag = False
                break
    if flag:
        unknownQuestions[sentence]=1
        answer= "I'm not too sure, I will find out about: "+sentence
    return answer

if __name__ == '__main__':
    readRules('rule.txt')
    q= input("what do you want to know?")
    while q != "quit":
        ans=getResponse(q)
        print(ans)
        q= input("what else?")
    print("Goodbye!")
