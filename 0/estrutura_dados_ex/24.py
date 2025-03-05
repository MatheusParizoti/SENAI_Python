# 24-Crie uma função que receba uma lista de números e retorne a soma de todos
# os números ímpares da lista

def num(n1 = int(input("Quantos numeros voce vai querer usar? : "))):
    impares = []
    for _ in range(n1):
        numeros = int(input("Coloque os numeros: "))
        if numeros % 2 == 1:
            impares.append(numeros)
    
    soma = sum(impares)
    print(impares)
    print(f"A soma dos numeros impares é: {soma}")

num()