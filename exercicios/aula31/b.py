import numpy as np

matriz_5x5 = np.reshape(np.arange(1, 26), (5, 5))
print(matriz_5x5)

soma_coluna_3 = np.sum(matriz_5x5[:, 1])
print(soma_coluna_3)