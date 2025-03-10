n1 = int(input("Digite um numero 1: "))
n2 = int(input("Digite um numero 2: "))

if n1 > 30000:
    print("Tente novamente, não aceitamos numeros acima de 30.000")
elif n2 > 30000:
    print("Tente novamente, não aceitamos numeros acima de 30.000")

soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
multiplicacao = n1 * n2

print(f"A soma de {n1} + {n2} é: {soma}")
print(f"A subtração de {n1} - {n2} é: {subtracao}")
print(f"A divisão de {n1} / {n2} é: {divisao}")
print(f"A multiplicação de {n1} * {n2} é: {multiplicacao}")