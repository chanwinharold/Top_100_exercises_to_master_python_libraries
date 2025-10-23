import numpy as np

rand_arr = np.random.rand(1000)
norm_arr = np.random.randn(1000)

sigma_1 = rand_arr.std()
x_bar_1 = rand_arr.mean()

sigma_2 = norm_arr.std()
x_bar_2 = norm_arr.mean()

print(f"Array 1 -> Moyenne : {x_bar_1.round()} \t Écart-type : {sigma_1.round()} \n"
      f"Array 2 -> Moyenne : {x_bar_2.round()} \t Écart-type : {sigma_2.round()} \n")

