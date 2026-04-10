import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

arr[0] = 42

print(arr)
print("Copy: ",x)
print("View: ",y)

print("Arr base: ",arr.base)
print("x base: ", x.base)
print("y base: ", y.base)