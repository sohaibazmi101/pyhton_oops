import numpy as np
from numpy import random as rn

# data = np.loadtxt("data.csv", delimiter=",", skiprows=1, usecols=(1,3))
data = np.genfromtxt("data.csv", delimiter=",", skip_header=1, usecols=(0,1,2,3), filling_values=np.nan)
# print(data)
# np.savetxt("array.csv", data, delimiter=",", fmt='%f')

arr = rn.rand(5)

print("Default: ")
print(arr)
np.set_printoptions(precision=2, suppress=True)
arr2 = np.array([1.0000238348394834,0.00002374834782378237823])
print("set_printoptions: ", arr)
print("With suppress on: ", arr2)