import numpy as np

serie = np.array([2, 4, 6, 8, 10])

sum_cum = np.cumsum(serie)
diff_ = np.diff(serie)

print(sum_cum, "\n", diff_)