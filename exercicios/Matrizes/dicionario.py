#  Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média.

sala = {}
soma = 0
media = 0

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    sala[nome] = nota
    soma += sala[nome]

for _ in sala:
    media = soma / len(sala)

print(f"A sala de aula é: {sala}")
print(f"A meida das notas é: {media}")