liste = list(range(1, 6))
print(liste, type(liste))

import numpy as np

arr = np.array(liste)
print(arr, type(arr))

print(arr.shape, arr.dtype)

arr = arr.reshape((arr.shape[0], 1))
print(arr, arr.shape)