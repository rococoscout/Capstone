from rule import Rule
import numpy
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

embeds = api.load("glove-wiki-gigaword-50")

#rules = getRules()

def getVecAnswer(rules, question):

    uservec = embeds[question]

    allscores = list()
    for rule in rules:
        score = cosine(uservec, rules.vector)
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

def make_total_vector(rule):
    if rule.vector is None:
        rule.vector = numpy.zeros(50)
        for question in rule.questions:
            vec = embeds[question]
            rule.vector = rule.vector + vec
        rule.updateVector()
    return


def cosine(vA, vB):
    return numpy.dot(vA,vB) / (numpy.sqrt(numpy.dot(vA,vA)) * numpy.sqrt(numpy.dot(vB,vB)))

if __name__ == "__main__":

    testrule = Rule(1,None,["a"],["where is Hopper Hall"],None)

    print(testrule.vector)
