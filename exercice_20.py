import numpy as np

mat = np.arange(12).reshape(3,4)
print(mat)

offset = np.arange(1, 5)
print(offset.shape)

mat = mat + offset
print(mat)