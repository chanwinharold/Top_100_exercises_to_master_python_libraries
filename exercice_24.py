import numpy as np

arr = np.random.randint(1, 51, (4,5))

sum_row = arr.sum(axis=1)
sum_col = arr.sum(axis=0)

max_row = arr.max(axis=1)
max_col = arr.max(axis=0)

min_row = arr.min(axis=1)
min_col = arr.min(axis=0)


print(arr, end="\n\n")
print(
    sum_row,
    sum_col,
    max_row,
    max_col,
    min_row,
    min_col)


