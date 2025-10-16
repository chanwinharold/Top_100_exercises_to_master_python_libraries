import numpy as np

angles = np.array([0, 30, 45, 60, 90, 180])

rad_conv = np.deg2rad(angles)
print("Conversion en Radians : ", rad_conv)
print()
print("Cosinus : ", np.cos(rad_conv))
print()

valeurs = np.array([1, -4, 9, -16])
# la racine carrée des valeurs absolues de cet array
print(np.sqrt( np.abs(valeurs) ))