# Classe Retângulo
# 1.Crie uma classe que represente um retângulo com largura e altura. Adicione métodos para calcular a área e o perímetro.

class Retangulo():
    def __init__(self, largura, altura, medidas,lados=4):

        self.larura = largura
        self.altura = altura
        self.medidas = medidas
        self.lados = lados
    
    def calcular(self):
        x = self.larura * self.altura
        p = self.medidas * self.lados
        
        return f"A área do retângulo é {x}\nO perímetro do retângulo é {p}"



        
        
r1 = Retangulo(10,5,4)
contas = r1.calcular()
print(contas)