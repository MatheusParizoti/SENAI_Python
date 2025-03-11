def rotina():
    print("Olá Bem-vindo(a) a Calculadora")
    print("Esses são os metodos Matematicos: ")
    print("*")
    pergunta = str(input("Qual metodo matematico voce deseja usar? "))
    
    if pergunta not in ["*"]:
        print("Por favor digite apenas os numeros matematicos")
    
    def multi():
        n1 = float(input("Ótimo, agora digite o primeiro número da multiplicação: "))
        n2 = int(input("Agora digite o segundo número que vai determinar quantas vezes o primeiro número será somado: "))
        
        multiplicacao = 0
        for _ in range(n2):  
            multiplicacao += n1
        
        print("")
        print("Aqui está o resultado:")
        print(multiplicacao)

    if pergunta == "*":
        multi()


rotina()