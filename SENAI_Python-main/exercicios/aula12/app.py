n1 = input("Digite a sua massa corporal(kg): ")
n2 = input("Digite a sua altura: ")

altura = float(n2) ** 2
calculo = int(n1) / altura

print("Dados informados:")
print(f"Massa corporal: {n1} kg")
print(f"Altura: {n2} m")
print("Com base nos Calculos da IMC: ")

if(calculo < 18):
    print("Classificação: Magreza")
elif(calculo >= 18 and calculo <= 24.9):
    print("Classificação: Saudável")
elif(calculo >= 25 and calculo <= 29.9):
    print("Classificação: Sobrepeso")
elif(calculo >= 30):
    print("Classificação: Obesidade")
