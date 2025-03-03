# Lista Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados".

lista = []
soma = 0

for i in range(5):
    lista.append(int(input("Digite um número: ")))
    soma += lista[i]


print(lista, soma)