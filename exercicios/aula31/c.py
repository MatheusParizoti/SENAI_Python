import numpy as np

matriz_5x5 = np.reshape(np.arange(1, 26), (5, 5))

soma_diagonal_principal = np.sum(np.diagonal(matriz_5x5))
print("Soma da diagonal principal:", soma_diagonal_principal)
