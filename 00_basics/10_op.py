from numpy import random
import numpy

nd = random.rand(1000)
# print(numpy.min(nd))
# print(numpy.var(nd))
# iqr = numpy.percentile(nd, 75) - numpy.percentile(nd, 25)
# print("IQR: ",iqr)

# Given a matrix, find row-wise sum and column-wise sum.

print("Given a matrix, find row-wise sum and column-wise sum.")

arr = random.randint(1,20,(3,4))
row_sum = numpy.sum(arr, axis=1)
col_sum = numpy.sum(arr, axis=0)
print("Original: ")
print(arr)
print("row sum: ", row_sum)
print("Col Sum: ", col_sum)