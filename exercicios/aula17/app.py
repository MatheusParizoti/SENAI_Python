num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))
impares=[]
if num1 < num2:
  print("Numero um é menor")
  intervalo = range(num1, num2 +1)
  for i in list(intervalo):
     if (i%2) == 1:
       impares.append(i)
  print(impares)