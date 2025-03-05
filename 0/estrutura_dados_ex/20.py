# 20-Solicite ao usuário que insira os elementos de uma matriz 3x3 e exiba a matriz
# formatada.

colunaUm =[]
colunaDois=[]
colunaTres =[]

colunas = [colunaUm, colunaDois, colunaTres]

for perguntas in range(1):
    for coluna1 in range(3):
        coluna1p = str(input("Coloque 3 elementos na coluna 1: "))
        colunaUm.append(coluna1p)

    for coluna2 in range(3):
        coluna2p = str(input("Coloque 3 elementos na coluna 2: "))
        colunaDois.append(coluna2p)

    for coluna3 in range(3):
        coluna3p = str(input("Coloque 3 elementos na coluna 3: "))
        colunaTres.append(coluna3p)

print("")
for linha in colunas:
    print(linha)


# # Inicializando a matriz 3x3 como um array vazio de tipo str
# matriz = np.empty((3, 3), dtype=str)

# # Solicitando ao usuário para inserir os elementos da matriz
# for i in range(3):
#     for j in range(3):
#         matriz[i][j] = input(f"Coloque o elemento na posição ({i}, {j}): ")

# # Exibindo a matriz com índices 0 a 8
# print("\nMatriz formatada:")
# contador = 0
# for i in range(matriz.shape[0]):  # Loop pelas linhas
#     for j in range(matriz.shape[1]):  # Loop pelas colunas
#         print(f"{contador}: {matriz[i][j]}", end="  ")
#         contador += 1
#     print()  # Quebra de linha após cada linha da matriz



