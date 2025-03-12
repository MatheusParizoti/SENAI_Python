def horario():
    hora = int(input("Que horas são? "))
    minuto = int(input("Qual são os minutos? "))

    if hora < 0 or hora >= 25:
        print("Hora inválida! Digite uma hora entre 0 e 23.")

    if hora == 0:
        hora_12h = 12
        periodo = "AM"
    elif hora == 12:
        hora_12h = 12
        periodo = "PM"
    elif hora > 12:
        hora_12h = hora - 12
        periodo = "PM"
    else:
        hora_12h = hora
        periodo = "AM"
    
    print(f"{hora_12h}:{minuto:02d} {periodo}") 

def main():
    while True:
        horario()       

        resposta = input("Deseja calcular novamente? (s/n): ").strip().lower()

        if resposta != 's':
            print("Obrigado por usar o programa!")
            break 
        
main()
