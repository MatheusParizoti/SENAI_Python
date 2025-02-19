# Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz,
#     matriz = np.array([[3, 4, 1],
#                     [3, 1, 5]])"

import numpy as np

matriz = np.array([[3, 4, 1],
                    [3, 1, 5]])

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
        soma += matriz[i][j]

print("")
print(f"A soma de todos os elementos da matriz é: {soma}")