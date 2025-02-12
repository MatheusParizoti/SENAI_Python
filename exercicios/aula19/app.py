media = []
alunos = []

# Variáveis para contagem de situações
aprovados = 0
exame = 0
reprovados = 0

for i in range(6):
    aluno = input("Coloque o nome: ")
    alunos.append(aluno)
    n1 = int(input("Coloque a nota: "))
    n2 = int(input("Coloque a nota: "))
    print("")
    
    media_calculada = (n1 + n2) / 2
    media.append(media_calculada)  
    
for i in range(6):
    aluno = alunos[i]
    media_calculada = media[i]
    
    if media_calculada < 3:
        print(f"{aluno}: Reprovado")
        reprovados += 1
    elif 3 <= media_calculada <= 7:
        print(f"{aluno}: Exame")
        exame += 1
    elif media_calculada > 7:
        print(f"{aluno}: Aprovado")
        aprovados += 1

# Contagem dos aprovados, exames e reprovados
print(f"Numero de aprovados: {aprovados}")
print(f"Numero de exames: {exame}")
print(f"Numero de reprovados: {reprovados}")

# Calculando a média da sala
media_sala = sum(media) / len(media)
print(f"Média da sala: {media_sala:.2f}")