from numpy import random
import numpy as np

a = random.randint(1,10,(3,4))
print("Original: ")
print(a)
print("Transpose")
print(a.transpose())
print("Using T: ")
print(a.T)
b = random.randint(1,10,6)
print(b)
print(np.flip(b))