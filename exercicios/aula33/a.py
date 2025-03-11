import numpy as np

# Criando a matriz 4x4
matriz_4x4 = np.reshape(np.arange(1, 17), (4, 4))

# Exibindo a matriz
print("Matriz 4x4:")
print(matriz_4x4)

parte1 = matriz_4x4[:2, :2] 
parte2 = matriz_4x4[:2, 2:]  
parte3 = matriz_4x4[2:, :2]  
parte4 = matriz_4x4[2:, 2:]  

print(parte1)
print("Soma da Parte 1:", np.sum(parte1))

print(parte2)
print("Soma da Parte 2:", np.sum(parte2))

print(parte3)
print("Soma da Parte 3:", np.sum(parte3))

print(parte4)
print("Soma da Parte 4:", np.sum(parte4))

# Parte da Diagonal Pricipal

# Inicializando as somas
soma_diagonal_e_abaixo = 0
soma_acima_diagonal = 0

# Iterando sobre os índices para separar a soma das partes
for i in range(4):
    for j in range(4):
        if i >= j:  # Diagonal e abaixo
            soma_diagonal_e_abaixo += matriz_4x4[i, j]
        else:  # Acima da diagonal
            soma_acima_diagonal += matriz_4x4[i, j]

# Exibindo os resultados
print(f"Matriz 4x4:\n{matriz_4x4}")
print(f"Soma da diagonal principal e posições abaixo dela: {soma_diagonal_e_abaixo}")
print(f"Soma das posições acima da diagonal: {soma_acima_diagonal}")