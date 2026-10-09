#slicing operations 1D
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5]) # index 1 to 4
print(arr[:5]) # index 0 to 4
print(arr[:]) # index first to last (0 to 7)
print(arr[4:]) # index  4 to end (4 to 7)
print(arr[:4]) # index start to 4 (0 to 3)

# negative slicing 
print(arr[-3:-1]) # from back last 2nd to last last 3rd (-1 not included)

# step 
print(arr[1:5:2]) # step =  2 prints numbers at a step of 2
print(arr[::2]) # step = 2 prints numbers from start to end with a step 2


#2D slicing
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1, 1:4]) # prints 1st row and column 1 to 3
print(arr[0:2, 2]) # prints column 2 and row 0

# row slicing

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
element = arr2[1,2] # selects the element at row 1, column 2
print(element) # prints 6
row_slice = arr2[0:2, :] # selects rows 0 and 1, all columns
print(row_slice) # prints [[1 2 3] [4 5 6]]

# column slicing

arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
column_slice = arr3[:, 1:3] # selects all rows, columns 1 and 2
print(column_slice) # prints [[2 3] [5 6]]