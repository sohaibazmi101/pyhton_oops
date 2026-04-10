import numpy as np

arr = np.array([1,2,3,4,5])
for x in arr:
    print(x)

a = np.array([[1,2,3,4],
              [5,6,7,8]])
for x in a:
    print(x)
for x in a:
    for y in x:
        print(y)