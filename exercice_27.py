import numpy as np

arr = np.arange(1, 26).reshape((5, 5))
print(arr)

arr_1 = arr[0, 0]
arr_2 = arr[1, 2]
arr_3 = arr[3, 4]
arr_4 = arr[4, 1]

arr_0 = np.array([arr_1, arr_2, arr_3, arr_4])
print(arr_0)