import numpy as np

matriz_random = np.random.randint(1, 101, size=(12, 13))

print("Matriz com valores aleatórios:")
print(matriz_random)

maior_valor_por_linha = np.max(matriz_random, axis=1).reshape(-1, 1)

print("")
print("Maior Valor de Cada Linha")
print(maior_valor_por_linha)

matriz_dividida = matriz_random / maior_valor_por_linha

matriz_modificada = np.round(matriz_dividida, 2)

print("")
print("Matriz Modificada")
print(matriz_modificada)