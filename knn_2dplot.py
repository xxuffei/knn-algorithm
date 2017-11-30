from sklearn.datasets import load_iris
from numpy import *
iris=load_iris()
data=iris.data
target=iris.target
dataset=array(data)
labels=array(target)
newInput=array([4.5,3.2,3.5,0.8])

import matplotlib.pyplot as plt
fig=plt.figure(1,figsize=(13,13))
ax1=fig.add_subplot(321,xlabel='sepal length (cm)',ylabel='sepal width (cm)');
ax2=fig.add_subplot(322,xlabel='sepal length (cm)',ylabel='petal length (cm)');
ax3=fig.add_subplot(323,xlabel='sepal length (cm)',ylabel='petal width (cm)');
ax4=fig.add_subplot(324,xlabel='sepal width (cm)',ylabel='sepal width (cm)');
ax5=fig.add_subplot(325,xlabel='sepal width (cm)',ylabel='petal length (cm)');
ax6=fig.add_subplot(326);plt.xlabel('sepal width (cm)');plt.ylabel('petal width (cm)');

ax1.scatter(dataset[labels==0,0],dataset[labels==0,1],15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax1.scatter(dataset[labels==1,0],dataset[labels==1,1],15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax1.scatter(dataset[labels==2,0],dataset[labels==2,1],15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax1.legend(loc='upper right')
ax2.scatter(dataset[labels==0,0],dataset[labels==0,2],15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax2.scatter(dataset[labels==1,0],dataset[labels==1,2],15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax2.scatter(dataset[labels==2,0],dataset[labels==2,2],15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax2.legend(loc='upper left')
ax3.scatter(dataset[labels==0,0],dataset[labels==0,3],15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax3.scatter(dataset[labels==1,0],dataset[labels==1,3],15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax3.scatter(dataset[labels==2,0],dataset[labels==2,3],15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax3.legend(loc='upper left')
ax4.scatter(dataset[labels==0,1],dataset[labels==0,2],15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax4.scatter(dataset[labels==1,1],dataset[labels==1,2],15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax4.scatter(dataset[labels==2,1],dataset[labels==2,2],15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax4.legend(loc='upper right')
ax5.scatter(dataset[labels==0,1],dataset[labels==0,3],15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax5.scatter(dataset[labels==1,1],dataset[labels==1,3],15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax5.scatter(dataset[labels==2,1],dataset[labels==2,3],15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax5.legend(loc='upper left')
ax6.scatter(dataset[:,2],dataset[:,3],15.0*array(labels+1),15.0*array(labels+1))
plt.show()