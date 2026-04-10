import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr[0,4])
print(arr[0:4,1])
print(arr[0:1,1:5])

# This is an example of window slice

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

print("2D-Array: \n", a[:,1:3])
print("Another: ", a[1:3,3:-1])