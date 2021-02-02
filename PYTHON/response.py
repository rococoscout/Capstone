from rule import Rule
import re
import json
import genericResponse as gen
import regexResponse as reg
import vecResponse as vec


#Function that gives the answer to the input Question
#Takes a string input and returns the string answer
#Gets rules from rule.py and calls functions from other ~Response.py's
def getAnswer(input):
    allRules = Rule.getRules()
    matched=False

    matchedRules = reg.getRegexAnswer(allRules, input)
    if(matchedRules == None):
        answer = vec.getVecAnswer(allRules, input)
    else:
        answer = vec.getVecAnswer(matchedRules, input)
    if(answer == None):
        answer= gen.getGenericAnswer(input)
        Rules.addUnmatchedQuestion(input)

    return answer

if __name__ == '__main__':
    print(getAnswer("Hi"))
