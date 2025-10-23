import numpy as np

np.random.seed(123)
n = np.random.randint(0, 20, 20)

# 4 élèves × 5 matières
grades = n.reshape((4, 5))
print(grades)

for row in grades:
    mask = row >= 10
    print(f"{len(row[mask]) * 100 / row.shape[0]}%")
