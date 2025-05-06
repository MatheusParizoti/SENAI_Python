## 3.Classe Carro
## Crie uma classe com atributos marca, modelo, ano. 
# Adicione um método descricao().

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
            
    def descricao(self):
        
        print(f'a marca do carro é: {self.marca}   o modelo do carro é: {self.modelo}  o ano do carro é {self.ano}')
        
teste = Carro("armagedor","maverick",2002)
teste.descricao()
        

        