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

def classify(distances, labels, k):
    sort_index = distances.argsort()
    class_count = {}
    for x in range(k):
        index = sort_index[x]
        label = labels[index]
        class_count[label] = class_count.get(label,0) + 1
    sorted_class_count =sorted(class_count.iteritems(), 
            key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]

def execute(vector, dataset, labels, k):
    distances = calculateDistance(vector, dataset)
    print classify(distances, labels, k)

group, labels = createDataset()
execute([1,1], group, labels, 3)
