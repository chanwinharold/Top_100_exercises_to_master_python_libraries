import numpy as np

np.random.seed(321)
arr = np.random.randint(10, 35, 30)
print("Températures : \n", arr)

mask = arr > 25
temps_chaud = arr[mask]
print("Temps chauds : \n", temps_chaud)

# proportion de températures au-dessus de 25°C
print(f"Proportion de températures au-dessus de 25°C : {round(sum(mask) * 100 / mask.shape[0], 2)}%")