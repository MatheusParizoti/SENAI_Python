# 33-Solicite ao usuário um número e tente dividir 100 por ele, tratando o erro caso
# seja digitado zero.

n1 = int(input("Digite um numero: "))

if n1 == 0:
    print("Não pode ser divido por 0 Nessa atividade")
else:
    dividir = n1 / 100
    print(dividir)