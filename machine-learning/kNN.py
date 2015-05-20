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

def calculateDistance(vector, matrix):
    matrix_size = matrix.shape[0]
    new_matrix = tile(vector, (matrix_size,1))
    different_matrix = new_matrix - matrix
    square_matrix = different_matrix ** 2
    square_distances = square_matrix.sum(axis=1)
    return square_distances ** 0.5

def classify(vector, dataset, labels, k):
    distances = calculateDistance(vector, dataset)
    print distances

group, labels = createDataset()
print calculateDistance([0,1], group)


classify([0,1], group, labels, 2)
