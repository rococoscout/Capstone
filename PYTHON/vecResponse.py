import rule
import numpy
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

embeds = api.load("glove-wiki-gigaword-50")
#
# rules = getRules()


#Takes a list of Rules and input question
#Returns a string answer if there were matches
#Returns None if there were no matches
def getVecAnswer(rules, question):
    print(embeds)
    question=clean(question)
    uservec= numpy.zeros(50)
    for word in question:
        uservec = embeds[word] + uservec
    allscores = list()
    for rule in rules:
        make_total_vector(rule)
        score = cosine(uservec, rule.vector)
        if not numpy.isnan(score):
            allscores.append((rule,score))
            allscores.sort(reverse=True, key=lambda x:x[1])

    if allscores[0][1] > .90:
        rule = allscore[0][0]
        rule.vector = rule.vector + uservec
        rule.addQuestion(question)
        rule.updateVector()
        return rule.answers[0]
    else:
        return None


#Takes a Rule and the embed to create a total vector based on the
#rule's list of questions
def make_total_vector(rule):
    rule.vector = numpy.zeros(50)
    for question in rule.questions:
        cleanedQ= clean(question)
        vec= numpy.zeros(50)
        for word in cleanedQ:
            vec = embeds[word] + vec
        rule.vector = rule.vector + vec
    rule.updateVector()
    return

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
