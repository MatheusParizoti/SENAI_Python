def velocidade_media():
    distancia = float(input("Distancia percorrida(Metros): "))
    tempo = float(input("Tempo percorrido(segundos): "))
    # hora = 60
    # converter = tempo * hora
    formula = distancia / tempo
    print(f"A velocidade media é: {formula}")

velocidade_media()