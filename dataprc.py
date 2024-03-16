from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')

x,y=make_blobs(n_samples=100, centers=3, cluster_std=1, n_features=2)

plt.scatter(x[:,0],x[:,1], s=40,color='g')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
plt.clf()
