import rule
import re
import json
import genericResponse
import regexResponse
import vecResponse



def getAnswer(input):
    allRules = Rules.getRules()
    matched=False

    matchedRules = getRegexAnswer(allRules, input)
    if(matchedRules == None):
        answer = getVecAnswer(allRules, input)
    else
        answer = getVecAnswer(matchedRules, input)
    if(answer == None):
        answer= getGenericAnswer(input)
        Rules.addUnmatchedQuestion(input)

    return answer
