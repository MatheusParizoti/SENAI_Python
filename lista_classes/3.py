# 3.Classe Carro
# Crie uma classe com atributos marca, modelo, ano. Adicione um método descricao().

class Carro():
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"A marca: {self.marca}, O modelo: {self.modelo}, O ano: {self.ano}"
    

car = Carro("Fiat","Mobi",2016)
mostrar = car.descricao()
print(mostrar)
        