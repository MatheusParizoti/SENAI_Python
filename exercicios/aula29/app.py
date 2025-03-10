quantidade = int(input("Digite a quantidade de Comodos da sua casa: "))
areaCasa = []
geral = []
soma = 0

for i  in range(quantidade):
    info = []
    nome = str(input("Digite o nome do comodo: "))
    info.append(nome)
    largura = int(input("Digite a largura: "))
    info.append(largura)
    comprimento = int(input("Digite a comprimento: "))
    info.append(comprimento)
    geral.append(info)

    area = largura * comprimento
    areaCasa.append(area)

    soma += area

print("")
print(f"Informações dos comodos: {geral}")
print(f"Area dos comodos: {areaCasa}")
print(f"Area da Casa é : {soma} metros quadrados")
