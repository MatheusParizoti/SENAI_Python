def rotina():
    print("Olá Bem-vindo(a) a Calculadora")
    print("Esses são os metodos Matematicos: ")
    print(" +  -  /  *")
    pergunta = str(input("Qual metodo matematico voce deseja usar? "))
    
    if pergunta not in ["+", "-", "/", "*"]:
        print("Por favor digite apenas os numeros matematicos")

    # variaveis
    um = pergunta == "+"
    dois = pergunta == "-"
    tres = pergunta == "/"
    quatro = pergunta == "*"

    def soma():
        n1 = float(input("Otimo, agora digite o um da soma: "))
        n2 = float(input("Agora digite o segundo valor que será somado: "))
        soma = n1 + n2
        print("")
        print("Aqui está o resultado")
        print(soma)

    def subi():
        n1 = float(input("Otimo, agora digite o um da subtracao: "))
        n2 = float(input("Agora digite o segundo valor que será subtraido: "))
        subtracao = n1 - n2
        print("")
        print("Aqui está o resultado")
        print(subtracao)
    
    def divi():
        n1 = float(input("Otimo, agora digite o um da divisao: "))
        n2 = float(input("Agora digite o segundo valor que será dividido: "))
        divisao = n1 / n2
        if n2 == 0:  
            print("Não é possível dividir por zero.")
            return
        print("")
        print("Aqui está o resultado")
        print(divisao)
    
    def multi():
        n1 = float(input("Otimo, agora digite o um da multiplicacao: "))
        n2 = float(input("Agora digite o segundo valor que será multiplicado: "))
        multiplicacao = n1 * n2
        print("")
        print("Aqui está o resultado")
        print(multiplicacao)

    if pergunta == "+":
        soma()
    elif pergunta == "-":
        subi()
    elif pergunta == "/":
        divi()
    elif pergunta == "*":
        multi()


rotina()