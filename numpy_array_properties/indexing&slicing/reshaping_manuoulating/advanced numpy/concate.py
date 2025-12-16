""""
np.concatenate((array1,array2),axis = 0)
axis = 0 >vertical stacking
axis = 1 > horinzontal stacking
"""
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([10,20,30])
new_arr = np.concatenate((arr1,arr2))
print(new_arr)