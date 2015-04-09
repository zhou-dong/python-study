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

print "begin to read data"

# keywords = loadData("vocabulary.txt")
trainData = loadData("train.data.txt")
# trainLabel = loadData("train.label.txt")

print "finish read data"

# findStopWord:
def getStopwords():
    result = {}
    for x in range(0, len(keywords)):
        if keywords[x] in stopwords.words('english'):
            result[x] = keywords[x]
    return result

# stopWords = getStopwords()

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

# cleanedTrainData = cleanTraingData()

# remove rare and common words
def removeRareCommonWords():
    return [data for data in cleanedTrainData if isNotLimit(int(data.split()[2]), 2, 20)]

def isNotLimit(num, rareLimit, commonLimit):
    return num > rareLimit and num < commonLimit

#finalTrainingData = removeRareCommonWords()

# calculate tf and idf

documentDict = {}
wordIndexDict = {}

def addWeight():
    countIndex = 0 
    for data in trainData:
        countIndex += 1
        datas = data.split()
        documentId = datas[0]
        wordIndex = datas[1]
        count = datas[2]
        if documentId not in documentDict.keys():
            documentDict[documentId] = 0
        documentDict[documentId] += int(count)
        if wordIndex not in wordIndexDict.keys():
            wordIndexDict[wordIndex] = []
        wordIndexDict[wordIndex].append(documentId)
        if countIndex == 10000:
            break

def calculateWeight(tf, idf):
    return tf * idf

def calculateIdf(containsCount, totalCount):
    return  math.log10(totalCount / containsCount)

def calculateTf(appearCount, totalAppear):
    return appearCount / totalAppear

def calculate():
    countIndex = 0
    for data in trainData:
        datas = data.split()
        documentId = datas[0]
        wordIndex = datas[1]
        count = datas[2]
        documentContain = documentDict.get(documentId) 
        print "tf: ", float(count) / float(documentContain)
        wordIndexAppear = len(set(wordIndexDict[wordIndex]))
        if wordIndexAppear == 0 :
            continue
        print "idf: ", math.log10(len(documentDict) / wordIndexAppear)
        countIndex += 1
        if countIndex == 10000:
            break

addWeight()
calculate()


