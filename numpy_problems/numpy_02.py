import numpy as np
arr = np.array([1,2,3,4])
print(arr[3])


arr = np.array([1,2,3,4])
print(arr[0])

arr1 = np.array(42) # 0D array
arr2 = np.array([42]) # 1D array

print(arr1.ndim)
print(arr2.ndim)