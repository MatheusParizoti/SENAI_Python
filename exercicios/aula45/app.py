from datetime import datetime as dt
from num2words import num2words

def data_por_extenso(data):
    try:
        # Corrige o formato da data para garantir que o mês e o dia tenham dois dígitos
        data = '/'.join([parte.zfill(2) for parte in data.split('/')])

        meses = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        
        # Converte a string da data para um objeto datetime
        converter = dt.strptime(data, "%d/%m/%Y")
        
        # Transformando o dia e o ano para palavras
        dia = num2words(converter.day, lang='pt_BR')  # Dia por extenso
        mes = meses[converter.month - 1].capitalize()  # Mes por extenso
        ano = num2words(converter.year, lang='pt_BR')  # Ano por extenso
        
        return f"A data é: {dia} de {mes} de {ano}"
    
    except ValueError:
        # Se a data for inválida, retornar None
        return None

n1 = input("Digite a data no formato DD/MM/AAAA: ")

resultado = data_por_extenso(n1)

if resultado:
    print(f"A data por extenso é: {resultado}")
else:
    print("Data inválida! Por favor, insira uma data no formato correto.")
