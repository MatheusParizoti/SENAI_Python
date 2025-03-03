while True:
    base = int(input("Coloque a base: "))
    altura = int(input("Coloque a altura: "))
    formula = (base * altura) / 2
    print(formula)
    p = input("deseja continuar ?: S ou N ")
    p = p.upper()
    if(p == "S"):
        print("eba")
        
    elif p == "N":
        print("fim da aplicação")
        break