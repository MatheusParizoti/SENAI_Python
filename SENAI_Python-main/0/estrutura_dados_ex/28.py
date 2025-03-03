# 28-Use o módulo random para gerar uma lista com 5 números aleatórios entre 1 e
# 100 e exibi-los.

import random

aleatorios = []
n1 = int(input("Digite um numero: "))
for _ in range(5):
    num = random.randint(1, n1)
    aleatorios.append(num)

print(f"Numero aleatorio é: {aleatorios}")