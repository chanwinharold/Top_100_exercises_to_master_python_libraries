import numpy as np

volume = np.random.randint(0, 20, (2, 3, 4))
volume_t = np.transpose(volume)

v_sum = np.sum(volume, axis=0)

print("Volume", volume)
print("Volume transposé", volume_t)
print("Somme axe 0", v_sum)
