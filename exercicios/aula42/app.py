def velocidade_media():
    distancia = float(input("Distancia percorrida(Metros): "))
    tempo = float(input("Tempo percorrido(segundos): "))
    # hora = 60
    # converter = tempo * hora
    formula = distancia / tempo
    print(f"A velocidade media é: {formula}")


    print("")
    print("Descobrindo a velocidade")
    print("")
    

    def divisao():
        p1 = float(input("Parametro 1: "))
        p2 = float(input("Parametro 2: "))
        div = p1 / p2
        print(f"A velocidade dos parametros é: {div}")

    divisao()

velocidade_media()