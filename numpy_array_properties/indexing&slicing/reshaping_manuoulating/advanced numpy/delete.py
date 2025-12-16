""""
np.dlete(array,index,axis = none)
"""
import numpy as np
arr = np.array([100,200,300,400,500])
print(arr)
new_arr = np.delete(arr,2,axis = 0)
print(new_arr)