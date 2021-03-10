from rule import Rule
import numpy
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

embeds = api.load("glove-wiki-gigaword-50")
#
# rules = getRules()


#Takes a list of Rules and input question
#Returns a string answer if there were matches
#Returns None if there were no matches
def getVecAnswer(rules, userinput):
    question=clean(userinput)
    uservec= numpy.zeros(50)
    for word in question:
        if word not in embeds:
            continue
        uservec = embeds[word] + uservec
    if len(rules)==1:
        print("lenrules=1")
        rules[0].vector = rules[0].vector + uservec
        rules[0].addQuestion(userinput)
        rules[0].updateVector()
        return rules[0].answers[0]
    allscores = list()
    for rule in rules:
        make_total_vector(rule)
        #score = cosine(uservec, rule.vector)
        for q in rule.questions:
            qvec = make_vector(q)
            score = cosine(uservec, qvec)
            if not numpy.isnan(score):
                #potentially keep track of q matched
                allscores.append((rule,score)) 
                allscores.sort(reverse=True, key=lambda x:x[1])
    if allscores[0][1] > .95:
        rule = allscores[0][0]
        rule.vector = rule.vector + uservec
        rule.addQuestion(userinput)
        rule.updateVector()
        return rule.answers[0]
    else:
        Rule.addUnmatchedQuestion(userinput)
        return None


#Takes a Rule and the embed to create a total vector based on the
#rule's list of questions
def make_total_vector(rule):
    rule.vector = numpy.zeros(50)
    for question in rule.questions:
        cleanedQ = clean(question)
        vec = numpy.zeros(50)
        for word in cleanedQ:
            if word not in embeds:
                continue
            vec = embeds[word] + vec
        rule.vector = rule.vector + vec
    rule.updateVector()
    return

#Makes a single vector
def make_vector(question):
    cleanedQ = clean(question)
    vec = numpy.zeros(50)
    for word in cleanedQ:
        if word not in embeds:
            continue
        vec = embeds[word] + vec
    return vec

#Cleans the text of punctuaction  and turns it into list of words
def clean(text):
    cleaners= ("?", "!", ".", ",","'",":",";","(",")","~","/",">","<","[","]","#","+","&","*","_","--","-", "$", "\\", "|", "\"", '\'')
    cleantext=text.lower()
    for c in cleaners:
        cleantext=cleantext.replace(c, " ")
    tokens=cleantext.strip().split()
    return tokens

def cosine(vA, vB):
    return numpy.dot(vA,vB) / (numpy.sqrt(numpy.dot(vA,vA)) * numpy.sqrt(numpy.dot(vB,vB)))

if __name__ == "__main__":

    testrule = Rule(1,None,["a"],["where is Hopper Hall"],None)

    print(testrule.vector)
