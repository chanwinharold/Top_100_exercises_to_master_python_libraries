import numpy as np

M = np.array([[1,2,3],[4,5,6]])
N = np.ones((3,2))*2

# produit matriciel M @ N
P = M @ N

# matrice transposée de M
T = M.T

A = np.random.randint(1, 10, 9).reshape((3, 3))
b = np.random.randint(1, 10, 9).reshape((3, 3))

R = np.linalg.solve(A, b)
print(P)
print(T)
print(R)
