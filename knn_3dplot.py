from mpl_toolkits.mplot3d import Axes3D 
fig2=plt.figure(2,figsize=(13,13))
ax1=fig2.add_subplot(221,projection='3d',xlabel='sepal length (cm)',ylabel='sepal width (cm)',zlabel='petal length (cm)')
ax1.scatter(dataset[labels==0,0],dataset[labels==0,1],dataset[labels==0,2],s=15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax1.scatter(dataset[labels==1,0],dataset[labels==1,1],dataset[labels==1,2],s=15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax1.scatter(dataset[labels==2,0],dataset[labels==2,1],dataset[labels==2,2],s=15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax1.legend(loc='upper right')

ax1=fig2.add_subplot(222,projection='3d',xlabel='sepal length (cm)',ylabel='sepal width (cm)',zlabel='petal width (cm)')
ax1.scatter(dataset[labels==0,0],dataset[labels==0,1],dataset[labels==0,3],s=15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax1.scatter(dataset[labels==1,0],dataset[labels==1,1],dataset[labels==1,3],s=15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax1.scatter(dataset[labels==2,0],dataset[labels==2,1],dataset[labels==2,3],s=15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax1.legend(loc='upper right')

ax1=fig2.add_subplot(223,projection='3d',xlabel='sepal length (cm)',ylabel='petal length (cm)',zlabel='petal width (cm)')
ax1.scatter(dataset[labels==0,0],dataset[labels==0,2],dataset[labels==0,3],s=15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax1.scatter(dataset[labels==1,0],dataset[labels==1,2],dataset[labels==1,3],s=15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax1.scatter(dataset[labels==2,0],dataset[labels==2,2],dataset[labels==2,3],s=15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax1.legend(loc='upper right')

ax1=fig2.add_subplot(224,projection='3d',xlabel='sepal width (cm)',ylabel='petal length (cm)',zlabel='petal width (cm)')
ax1.scatter(dataset[labels==0,1],dataset[labels==0,2],dataset[labels==0,3],s=15.0*array(labels[labels==0]+1),c='r',label='setosa')
ax1.scatter(dataset[labels==1,1],dataset[labels==1,2],dataset[labels==1,3],s=15.0*array(labels[labels==1]+1),c='g',label='versicolor')
ax1.scatter(dataset[labels==2,1],dataset[labels==2,2],dataset[labels==2,3],s=15.0*array(labels[labels==2]+1),c='b',label='virginica')
ax1.legend(loc='upper right')
plt.show()                                                           
                                                              