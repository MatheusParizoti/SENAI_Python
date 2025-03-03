par = []
impar = []

for i in range(10):
    n1 = int(input("Ecolha um numero: "))

    if  n1 % 2 == 0:
        par.append(n1)
    else:
        impar.append(n1)

print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")

soma_p = sum(par)
soma_i = sum(impar)

print(f"Soma dos numeros pares: {soma_p}")
print(f"Soma dos numeros impares: {soma_i}")