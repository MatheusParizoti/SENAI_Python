# 27-Solicite ao usuário um número e exiba um valor aleatório entre 1 e esse
# número.
import random

n1 = int(input("Digite um numero: "))

num = random.randint(1, n1)

print(f"Numero aleatorio é: {num}")