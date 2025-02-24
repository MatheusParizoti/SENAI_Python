otimo = []
bom = []
regular = []
media = 0
total_respostas = 0 

for _ in range(15):
    idade = int(input("Digite sua Idade: "))
    print("De a sua Opinião:")
    print("Digite 3 - Ótimo")
    print("Digite 2 - Bom")
    print("Digite 1 - Regular")
    opiniao = int(input("Qual a sua opinião sobre o cinema: "))
    print("")

    if opiniao not in [1, 2, 3]:
        print("Por favor escolha apenas entre 3 / 2 / 1")
    else:
        total_respostas += 1

    if opiniao == 3:
        otimo.append(idade)

    elif opiniao == 2:
        bom.append(opiniao)

    elif opiniao == 1:
        regular.append(opiniao)

soma = sum(otimo)
media =  soma / len(otimo) if len(otimo) > 0 else 0
qp = len(regular)
bomP = (len(bom) / total_respostas) * 100 if total_respostas > 0 else 0
print(f"A media da Idade das pessoas que escolheram Ótimo é: {media}" )
print("")
print(f"A quantidade de pessoas que escolheu Regular foi: {qp}")
print("")
print(f"A porcentagem de passoas que escolheram o Bom é: {bomP}")
