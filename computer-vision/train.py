from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np

clf = svm.SVC()

f = open ('datas.txt' , 'r')
temp = [ map(float,line.split(' ')) for line in f ]

m = np.matrix(temp)

a,b = m.shape

y = m[:,6]
X =  m[:, 0:6]

z = m [a-1, 0:6]

clf.fit(X, y) 

print clf.predict(z)

plt.show()
