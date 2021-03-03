# Code to handle finding and returning viable rules based on their regex
# MIDN 1/C Signorelli
import re
import rule

# class myRule:
#     def __init__(self, regex, answer):
#         self.regex = regex
#         self.answer = answer


#Takes a list of Rules and input question
#Returns a list of Rules if there were matches
#Returns None if there were no matches
def getRegexAnswer(allRules, input):
    matchedRules = []
    for rule in allRules:
        for regex in rule.regexes:
            check = re.search(regex, input)
            if check:
                #print('Rule match: ',rule.regex)
                matchedRules.append(rule)

    if not matchedRules:
        return None
    else:
        return matchedRules

if __name__ == '__main__':
    test1 = myRule("[wW]here.*[fF]ood", "testing 1 2 3")
    test2 = myRule("[wW]here.*midshipmen.*[eE]at", "hungry test")
    test3 = myRule("[wW]here", "Your question had the word 'where' in it")
    #test1 = rule(1, "[wW]here.*[fF]ood", "testing 1 2 3", "Where is the food?", None)
    #test2 = rule(2, "[wW]here.*midshipmen.*[eE]at", "hungry test", "Where do midshipmen eat?", None)
    testList = [test1, test2, test3]

    input = input('Ask something: ')

    check = getRegexAnswer(testList, input)
    if check:
        for response in check:
            print('Answer: ', response.answer)
    else:
        print('nothing matched!')
