import numpy
import nltk
import math
from nltk.corpus import stopwords

keywords = []
trainData = []
trainLabel = []

index = 0 

def loadData(fileName):
    with open(fileName, "r") as text_file:
        data = text_file.read()
    return data.splitlines()

keywords = loadData("vocabulary.txt")
trainData = loadData("train.data.txt")
trainLabel = loadData("train.label.txt")

# findStopWord:
def getStopwords():
    result = {}
    for x in range(0, len(keywords)):
        if keywords[x] in stopwords.words('english'):
            result[x] = keywords[x]
    return result

stopWords = getStopwords()

# new list without stopwords
def cleanKeywords():
    result = []
    for word in keywords:
        if word in stopwords.words('english'):
            continue
        result.append(word)
    return result

# cleanedWords = cleanKeywords()

# new training data without stopwords
def cleanTraingData():
    result = []
    for data in trainData:
        wordIndex = data.split()[1]
        if wordIndex is None:
            continue
        if stopWords.get(int(wordIndex)) is not None:
            continue
        result.append(data)
    return result

cleanedTrainData = cleanTraingData()

# remove rare and common words
def removeRareCommonWords():
    return [data for data in cleanedTrainData if isNotLimit(int(data.split()[2]), 2, 20)]

def isNotLimit(num, rareLimit, commonLimit):
    return num > rareLimit and num < commonLimit

finalTrainingData = removeRareCommonWords()

# calculate tf and idf

documentDict = {}
wordIndexDict = {}

def addWeight():
    for data in finalTrainingData:
        datas = data.split()
        documentId = datas[0]
        wordIndex = datas[1]
        count = datas[2]
        if documentId not in documentDict.keys():
            documentDict[documentId] = {wordIndex, count}
        else:
            documentDict[documentId].add({wordIndex, count})
       # print datas

def calculateWeight(tf, idf):
    return tf * idf

def calculateIdf(containsCount, totalCount):
    return  math.log10(totalCount / containsCount)

def calculateTf(appearCount, totalAppear):
    return appearCount / totalAppear

addWeight()

print documentDict

print len(cleanedTrainData)
print len(finalTrainingData)

