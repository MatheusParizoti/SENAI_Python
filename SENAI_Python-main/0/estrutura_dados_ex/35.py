# 35-Solicite ao usuário um número inteiro e trate o erro caso ele tente inserir um
# valor não numérico. Se a entrada for válida, exiba o quadrado do número.

while True:
    try:
        n1 = int(input("Digite um número: "))
        break  
    except ValueError:
        print("Isso não é um número válido. Tente novamente.")

area = n1 * n1
print(f"A area do numero que voce digitou: {area}")
