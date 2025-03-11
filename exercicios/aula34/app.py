import numpy as np

matriz_5x5 = np.reshape(np.arange(1, 26), (5, 5))

# Exibindo a matriz
print("Matriz 5x5:")
print(matriz_5x5)

n1 = int(input("Digite um numero dentro da matriz: "))

if n1 in matriz_5x5:
    print(f"O valor {n1} está dentra da matriz")
else:
        print(f"O valor {n1} não está dentra da matriz")
