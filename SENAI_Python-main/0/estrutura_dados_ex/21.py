# 21-Peça ao usuário que insira duas matrizes 2x2 e exiba a matriz resultante da
# soma das duas

colunaUm =[]
colunaDois=[]

colunaTres =[]
colunaQuatro =[]

matriz1 = [colunaUm, colunaDois]
matriz2 = [colunaTres, colunaQuatro]

for perguntas in range(1):
    for coluna1 in range(2):
        coluna1p = str(input("Coloque 2 elementos matriz 1 na coluna 1: "))
        colunaUm.append(coluna1p)

    for coluna2 in range(2):
        coluna2p = str(input("Coloque 2 elementos matriz 1 na coluna 2: "))
        colunaDois.append(coluna2p)

    for coluna3 in range(2):
        coluna3p = str(input("Coloque 2 elementos matriz 2 na coluna 1: "))
        colunaTres.append(coluna3p)

    for coluna4 in range(2):
        coluna4p = str(input("Coloque 2 elementos matriz 2 na coluna 2: "))
        colunaQuatro.append(coluna4p)

print("")
for linha in matriz1 + matriz2:
    print(linha)