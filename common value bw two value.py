import numpy as np
arr1=np.array([0,10,20,40,60])
print("array 1 :",arr1)
arr2=[10,30,40]
print("array 2 :",arr2)
print("the common values between two array :")
print(np.intersect1d(arr1,arr2))