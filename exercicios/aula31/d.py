import numpy as np

matriz_5x5 = np.reshape(np.arange(1, 26), (5, 5))

soma_diagonal_secundaria = np.sum(np.fliplr(matriz_5x5).diagonal())
print("Soma da diagonal principal:", soma_diagonal_secundaria)