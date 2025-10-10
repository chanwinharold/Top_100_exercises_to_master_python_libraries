import numpy as np

np.random.seed(345)
a = np.random.randint(1, 10, 9)
b = np.random.randint(1, 10, 9)

a = a.reshape((3, 3))
b = b.reshape((3, 3))

print(a, '\n\n', b)

# Somme
print(f"\nSomme -> \n{a + b} \n")

# Différence
print(f"\nDifférence -> \n{a - b}\n")

# Produit
print(f"\nProduit -> \n{a * b}\n")

# Quotient
print(f"\nQuotient -> \n{a / b}\n")