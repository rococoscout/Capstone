import numpy
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

embeds = api.load("glove-wiki-gigaword-50")

def make_vector(question):
    cleanedQ = clean(question)
    vec = numpy.zeros(50)
    for word in cleanedQ:
        if word not in embeds:
            continue
        vec = embeds[word] + vec
    return vec

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

    mainInput= input("Main input: ")
    tempInput= input("Test input: ")

    testvm = numpy.zeros(50)
    testvm = make_vector(mainInput)
    testvt = numpy.zeros(50)
    while(tempInput != "q"):
        testvt = make_vector(tempInput)
        print(cosine(testvm,testvt))
        t2=input("New Main? [leave empty to keep]: ")
        if(t2 != ""):
            testvm = make_vector(t2)
        tempInput= input("Test input: ")
