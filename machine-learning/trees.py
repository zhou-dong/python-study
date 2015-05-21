'''
decision tree

1. find the most efficient category to sepeare the data
    - infromation theory
    - greedy algorithm

2. repeat the first step(recursive), until all the end

not finish yet...

'''

import numpy as np

def createDataSet():
    data_set = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return np.matrix(data_set), labels

# use greedy algorithm
def findSeperateCategory(matrix):
    result = 0
    count = 1000
    matrix_col = matrix.shape[1]
    for x in range(matrix_col - 1):
        col_x = matrix[:,x].astype(int)
        count_min = np.count_nonzero(col_x)
        if count_min < count:
            count = count_min
            result = x
        return result

data_set, lables = createDataSet()
print findSeperateCategory(data_set)
print data_set.shape
print data_set[:,0]
print data_set
