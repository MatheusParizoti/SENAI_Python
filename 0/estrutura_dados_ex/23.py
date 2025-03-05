# 23-Crie uma função que receba um número e informe se ele é par ou ímpar.


def num(n1 = int(input("Digite um numero: "))):
    if n1 % 2 == 0:
        print("Numero Par")
    else:
        print("Numero Impar")
num()