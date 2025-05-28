# 2.Classe Círculo
# Crie uma classe Circulo com atributo raio. Implemente métodos para calcular área e circunferência.

class Circulo():
    def __init__(self,raio,pi=3.14):
        self.raio = raio
        self.pi = pi

    def area(self):
        quadrado = self.raio ** 2
        area = self.pi * quadrado
        return f"Area do circulo é {area}"
    
raio = Circulo(4) 
contas = raio.area()
print(contas)
