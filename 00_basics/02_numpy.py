import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)

arr.shape = (3,2)
print(arr)

a = np.arange(24)
print(a)
print("NDIM: ", a.ndim)
a.shape = (4,2,3)
print("NDIM: ", a.ndim)
print(a)

b = np.array([1,2,3,4], dtype=int)
print("Item Size: ",b.itemsize, b.dtype)

print("____________Complex___________")

c = np.array([1,2,3,4,5,6], dtype=complex)
print(c)