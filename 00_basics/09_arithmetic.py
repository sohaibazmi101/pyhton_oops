from numpy import random
import numpy as np

arr1 = random.randint(1,20,(3,4))
arr2 = random.randint(1,20,(3,4))
print("Arr1: ")
print(arr1)
print("Arr2")
print(arr2)

sum_arr = arr1 + arr2
sub_arr = arr1 - arr2
mult_arr = arr1 * arr2
mult2_arr = arr1@arr2.T

print("SUM:")
print(sum_arr)
print("SUB:")
print(sub_arr)
print("MULT:")
print(mult_arr)
print("Matrix Mult:")
print(mult2_arr)
c = np.matmul(arr1,arr2.T)
print(c)