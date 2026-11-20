# Exercise 5: Reshaping and Broadcasting
# 1. Reshape a 1D array of size 12 into a 3x4 matrix.
# 2. Create a column vector with values [1, 2, 3] and add it to every row of the matrix using broadcasting.
import numpy as np

#Create 1D array of size 12
arr = np.arange(12)
print(arr)

#Reshape a 1D array of size 12 into a 3x4 matrix
arr = np.arange(12).reshape(3,4)
print(arr)

#Create a column vector with values [1, 2, 3]
colvec = np.array([[1], [2], [3]])
print(colvec)

#Add it to every row of the matrix 
result = arr + colvec
print(result)