n1 = input("Digite o seu salario: ")

if (int(n1) < 1000):
    aumento = int(n1) * 0.25 
    valor = int(n1) + aumento

if(int(n1) >= 1000 and int(n1) < 2000):
    aumento = int(n1) * 0.15
    valor = int(n1) + aumento

if(int(n1) >= 2000):
    aumento = int(n1) * 0.10
    valor = int(n1) + aumento


print(f"O valor do seu salário com aumento é: {valor}")