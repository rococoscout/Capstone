from rule import Rule
import re
import json
import genericResponse as gen
import regexResponse as reg
import vecResponse as vec

from polyglot.detect import Detector
from polyglot.detect.base import logger
#from profanity_check import predict, predict_prob
#from profanityfilter import ProfanityFilter


logger.disabled = True

#Function that ensures user input is in English
#Takes in a string of user input and uses Polyglot library to check its language of origin
#If input is English, it returns true, allowing the getAnswer() function to follow through with its job
#If the input is not in English, it returns False
#A false return prompts the getAnswer() function to return a response asking the user to enter their question in English

def checkLanguage(input):
    detector = Detector(input)
    if detector.language.code == 'en':
        return True
    else:
        return False



#Function that gives the answer to the input Question
#Takes a string input and returns the string answer
#Gets rules from rule.py and calls functions from other ~Response.py's
def getAnswer(input):
    # pf = ProfanityFilter()

    #if(predict([input]) == 0):
#    if(pf.is_clean(input)):
    for i in range(1,5):
        allRules = Rule.getRules(priority=i)
        matched=False

        matchedRules = reg.getRegexAnswer(allRules, input)
        if(matchedRules == None):
            if checkLanguage(input):
                answer = vec.getVecAnswer(allRules, input)
            else:
                answer = "It seems that you have entered input that is not in English. \n Unfortunately I only speak English! \n Please translate your question so I can properly assist you!"
        else:
            answer = vec.getVecAnswer(matchedRules, input)
        if(answer != None):
            break
            
    if(answer == None):
        answer= gen.getGenericAnswer(input)
        Rule.addUnmatchedQuestion(input)
    return answer
"""
    else:
        answer = "[EXPLICIT LANGUAGE DETECTED]"
        return answer
"""

if __name__ == '__main__':
    print(getAnswer("Hi"))
    print(getAnswer("What is Computer Science?"))
    print(getAnswer("Tell me what computer science is about"))
    print(getAnswer("computer science is what?"))
    print(getAnswer("who made you?"))
    print(getAnswer("Are you able to double major?"))
    print(getAnswer("Where to go for classes in computer science?"))
