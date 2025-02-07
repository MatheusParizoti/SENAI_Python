("Lados de um Triângulo")
n1 = input("Primeiro Lado: ")
n2 = input("Segundo Lado: ")
n3 = input("Terceiro Lado: ")


if(int(n1) == 0 or int(n2) == 0 or int(n3) == 0):
    print("Não é um triângulo")
elif(int(n1) == int(n2) and int(n2) == int(n3)):
    print("Triângulo Equilátero")
elif(int(n1) == int(n2) or int(n2) == int(n3) or int(n1) == int(n3)):
    print("Triângulo Isósceles")
elif(int(n1) != int(n2) and int(n2) != int(n3) and int(n1) != int(n3)):
    print("Triângulo Escaleno")
elif(int(n1) + int(n2) > int(n3) or int(n2) + int(n3) > int(n1) or int(n1) + int(n3) > int(n2)):
    print("Não é um triângulo")



