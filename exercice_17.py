import numpy as np

np.random.seed(123)
arr = np.random.randint(0, 99, 15)
print(arr)

# les 5 premiers éléments
print(
    arr[:5]
)

# les 5 derniers
print(
    arr[-5:]
)

# les éléments d’indice pair (0,2,4,...).
mask = arr % 2 == 0
print(
    arr[mask]
)

# Inverser l’ordre
print(arr[::-1])
