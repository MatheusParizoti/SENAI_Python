## Classe Retângulo
## 1.Crie uma classe que represente um retângulo com 
# largura e altura. Adicione métodos para calcular a área e o perímetro.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        area = self.largura * self.altura
        
        print(f'area do retangulo é {area}')
        

teste = Retangulo(10,9)
teste.calcular_area()


        