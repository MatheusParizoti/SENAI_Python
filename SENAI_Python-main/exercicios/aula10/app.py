n1 = input("Digite o numero que seu veiculo estava passando pela avenida(km/h): ")


print("Motivo da Multa: Velocidade acima do permitido")
print("Velocidade do veiculo: ", n1 + " km/h")

if(int(n1) <= 10):
    print("O valor da multa é de 50,00")
elif(int(n1) >= 11 and int(n1) <= 30):
     print("O valor da multa é de 100,00")
elif(int(n1) >= 31):
     print("O valor da multa é de 200,00")



