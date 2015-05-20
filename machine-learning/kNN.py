'''
KNN: k nearest neighbour
    It is a supervised learning method
Step:
    1. calculate distance with all the data
    2. find the k nearest data
    3. from the shortest distance find the result
advantage:
    simple
week:
    1. must calculte all the distance of the data
    2. only can categorize, can not predict percent
'''

from numpy import *
import operator

def createDataset():
    group = array([[1.0, 1.1],[1.0, 1.0],[0, 0],[0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

group, labels = createDataset()

print group

print labels
