from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np

clf = svm.SVC()

f = open ('../datas.txt' , 'r')
temp = [ map(float,line.split(' ')) for line in f ]

m = np.matrix(temp)

a,b = m.shape

y = m[:,6]
X =  m[:, 0:2]

clf.fit(X, y) 

h = .2
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.5)

# Plot also the training points

plt.scatter(X[:, 0].tolist(), X[:, 1].tolist(), c=y.tolist(), cmap=plt.cm.Paired)

c1 = plt.scatter([1.0,2,3], [3,2,1], c='r', s=50,marker='+')

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.title("SVM Classify")

plt.show()

