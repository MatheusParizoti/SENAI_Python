## 2.Classe Círculo
## Crie uma classe Circulo com atributo raio. 
# Implemente métodos para calcular área e circunferência.

class Circulo:
    def __init__(self,raio):
        self.pi = 3.14
        self.raio = raio
    
    def calcular_area_circulo(self):
        
        quadrado = self.raio * 2
        area = self.pi * quadrado
        print(f" a area do circulo {area}")
        

teste = Circulo(12)
teste.calcular_area_circulo()