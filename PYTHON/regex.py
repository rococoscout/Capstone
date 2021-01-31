import re
import sys

class Regex:
    def __init__(self, dictionary):
        self.List = dictionary

def getResponse(sentence):
    flag = True
    answer = "I'm not too sure"
    #Iterates through the responses
    for ent in List:
        x=re.search(ent['rule'], sentence)
        if x:
            answer = ent['response']
            # TODO: add question to db
            flag = False
            break
    if flag:
        unknownQuestions[sentence]=1
        answer= "I'm not too sure, I will find out about: "+sentence
    return answer

    '''
    for ans in self.Dict.keys():
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
'''

if __name__ == '__main__':
    #readRules('rule.txt')
    q= input("what do you want to know?")
    while q != "quit":
        ans=getResponse(q)
        print(ans)
        q= input("what else?")
    print("Goodbye!")
