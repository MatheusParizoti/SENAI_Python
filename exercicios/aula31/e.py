import numpy as np

matriz_5x5 = np.reshape(np.arange(1, 26), (5, 5))

soma_todos_elementos = np.sum(matriz_5x5)
print("Soma de todos os elementos da matriz:", soma_todos_elementos)