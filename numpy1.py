import numpy as np

a = np.array([(1, 2, 3, 4),(3, 5, 7, 8),(5, 7, 7, 9)])


b = np.array([(1, 3), (4,4)])
c = np.array([(7, 4), (7,9)])
print(b+c)
b = b.reshape(1, 4)
print(b)
print(b.max())
print(b.min())
print(b.sum())
print(a.sum(axis=0))



