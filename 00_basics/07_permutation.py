from numpy import random
import numpy as np

arr = np.array([11,22,33,44,55])

b = arr.copy()

random.shuffle(arr)
print("Using Shuffle: ",arr)

k = random.permutation(arr)
print("Using Permutation(k): ", k)
print("Original: ", b)

# • Generate a 3×4 matrix of random integers between 1 and 100.

print("• Generate a 3×4 matrix of random integers between 1 and 100.")

x = np.array([1,2,3,4,5,6])
y = random.permutation(x)
print("Original: ", x)
print("Shuffled: ", y)