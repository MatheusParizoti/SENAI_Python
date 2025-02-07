n1 = input("Digite a idade do seu filho(a): ")

if(int(n1) <= 12):
    print("A categoria do seu filho(a) é: Criança")
elif(int(n1) >= 13 and int(n1) <= 17):
    print("A categoria do seu filho(a) é: Adolescente")
elif(int(n1) >= 18 and int(n1) <= 59):
    print("A categoria do seu filho(a) é: Adulto")
elif(int(n1) >= 60):
    print("A categoria do seu filho(a) é: Idoso")   

