import numpy as np

a = np.arange(24)

print(a[1:5])
print(a[:9])
print(a[-3:-1])

print(a[1:21:4])

b = a[-21:24:2]
print("Original Array: ",a)
print(b)