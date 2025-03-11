import numpy as np

matriz_4x6A = np.reshape(np.arange(1, 25), (4, 6))
print("")
print("Matriz A")
print(matriz_4x6A)



matriz_4x6B = np.reshape(np.arange(1, 25), (4, 6))
print("")
print("Matriz B")
print(matriz_4x6B)

matrizD = matriz_4x6B - matriz_4x6A
print("")
print("A soma das Matriz")
print(matrizD)