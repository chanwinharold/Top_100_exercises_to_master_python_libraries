import numpy as np

x = np.linspace(-2, 2, 5)
y = np.linspace(-3, 3, 7)

X, Y = np.meshgrid(x, y)

Z = X**2 - Y**2

print(Z.shape)
print(Z[0, 0])
print(Z[-1, -1])
print(Z)
