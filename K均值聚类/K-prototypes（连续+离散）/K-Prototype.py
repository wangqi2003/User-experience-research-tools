#python
#测试成功

import numpy as np
from kmodes.kprototypes import KPrototypes

# stocks with their market caps, sectors and countries
syms = np.genfromtxt('D:\GitHub\Practices-code\html\K-prototypes\stocks.csv', dtype=str, delimiter=',')[:, 0]
X = np.genfromtxt('D:\GitHub\Practices-code\html\K-prototypes\stocks.csv', dtype=object, delimiter=',')[:, 1:]
X[:, 0] = X[:, 0].astype(float)

kproto = KPrototypes(n_clusters=4, init='Huang', verbose=2, gamma=0)#init="Huang""Cao"表示不同的距离计算方法
                                                                    #gamma=0.8代表分类变量的权重
clusters = kproto.fit_predict(X, categorical=[1,2,3])#categorical类别变量的索引

# Print cluster centroids of the trained model.
print(kproto.cluster_centroids_)
# Print training statistics
print(kproto.cost_)
print(kproto.n_iter_)

for s, c in zip(syms, clusters):
    print("Symbol: {}, cluster:{}".format(s, c))