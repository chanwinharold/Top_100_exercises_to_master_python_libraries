import numpy as np

n = np.random.randint(1, 100, 100)
n_sorted = np.sort(n)
print(n_sorted)

index_sorted = np.argsort(n)
print(n[index_sorted])

