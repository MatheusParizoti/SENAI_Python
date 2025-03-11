import numpy as np

matriz_aposta = np.random.randint(0, 2, size=(13, 3))


print("Matriz Aposta: ")
print(matriz_aposta)

soma = 0
print("")
print("Numero de Pontos: ")
for i in range(13):
    for j in range(3):
        if matriz_aposta[i, j] == 1:  # Verifica se o elemento é 1
            soma += 1

print(soma)

simples = 0
duplas = 0
triplas = 0

for i in range(13):
    # : significa todos os elementos da linha
    num_1s = np.sum(matriz_aposta[i, :] == 1)  # Conta os 1's na linha i
    if num_1s == 1:
        simples += 1
    elif num_1s == 2:
        duplas += 1
    elif num_1s == 3:
        triplas += 1

print("")
print(f"Numero de apostas simples: {simples}")
print(f"Numero de apostas duplas: {duplas}")
print(f"Numero de apostas triplas: {triplas}")
