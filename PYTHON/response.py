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
        Rule.addUnmatchedQuestion(input)

    return answer

if __name__ == '__main__':
    print(getAnswer("Hi"))
    print(getAnswer("What is Computer Science?"))
    print(getAnswer("Tell me what computer science is about"))
    print(getAnswer("computer science is what?"))
    print(getAnswer("who made you?"))
    print(getAnswer("How are babies made?"))
    print(getAnswer("Are you able to double major?"))
    print(getAnswer("Where to go for classes in computer science?"))