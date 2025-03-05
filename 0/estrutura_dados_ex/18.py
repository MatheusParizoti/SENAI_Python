# 18-Crie um dicionário que armazene os nomes e idades de três pessoas e permita
# que o usuário consulte a idade de uma pessoa informando seu nome

idades = {"Matheus":18, "Guilherme":7, "Priscila":43 }

pergunta = str(input("Digite o nome de uma pessoa :"))

if pergunta == "Matheus":
    print(f"A idade de Matheus é {idades["Matheus"]}")
elif pergunta == "Guilherme":
    print(f"A idade de Guilherme é {idades["Guilherme"]}")
elif pergunta == "Priscila":
    print(f"A idade de Priscila é {idades["Priscila"]}")
else:
    print("Esse nome não esta na lista")