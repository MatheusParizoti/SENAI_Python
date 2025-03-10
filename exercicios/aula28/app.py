base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
resultado = 0
for i in range(expoente):
    resultado = resultado + base

print(f'a exponenciação com soma é: {resultado}')