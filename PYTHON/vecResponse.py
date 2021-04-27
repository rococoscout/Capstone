from rule import Rule
import numpy
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

embeds = api.load("glove-wiki-gigaword-50")

#Takes a list of Rules and input question
#Returns a string answer if there were matches
#Returns None if there were no matches
def getVecAnswer(rules, userinput):

    if len(rules) == 0:
        return None

    question=clean(userinput)
    uservec= numpy.zeros(50)
    for word in question:
        if word not in embeds:
            continue
        uservec = embeds[word] + uservec

    errorvec = numpy.zeros(50)
    if uservec.all() == errorvec.all():
        return None

    if len(rules)==1:
        print("lenrules=1")
        rules[0].addQuestion(userinput)
        return rules[0].answers[0]

    allscores = list()
    for rule in rules:
        for q in rule.questions:
            qvec = make_vector(q)
            score = cosine(uservec, qvec)
            if not numpy.isnan(score):
                allscores.append((rule,score)) 
                allscores.sort(reverse=True, key=lambda x:x[1])

    if allscores[0][1] > .95:
        rule = allscores[0][0]
        rule.addQuestion(userinput)
        return rule.answers[0]
    else:
        return None

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

    temp = ""
    mainInput= input("Main input: ")
    tempInput= input("Test input: ")

    testvm = numpy.zeros(50)
    testvm = make_vector(mainInput)
    testvt = numpy.zeros(50)
    while(tempInput != "q"):
        testvt = make_vector(tempInput)
        print(cosine(testvm,testvt))
        tempInput= input("Test input: ")
    
