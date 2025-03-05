# 34-Peça ao usuário para inserir um número e trate possíveis erros de entrada
# (como digitar uma letra no lugar do número).

while True:
    try:
        n1 = int(input("Digite um número: "))
        break  
    except ValueError:
        print("Isso não é um número válido. Tente novamente.")

print(f"Você digitou o número: {n1}")
