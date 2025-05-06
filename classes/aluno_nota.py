## 5.Classe Aluno com Notas
## Crie uma classe com nome e lista de notas. 
# Implemente métodos para adicionar notas, calcular média e verificar aprovação.

class AlunoNotas:
    def __init__(self, nome):
        self.nome = nome
        self.nota = []
        
    def adicionar_nota(self, nota):
        self.nota.append(nota)
        
    def lista_notas(self):
        m = sum(self.nota) / len(self.nota)
        
        print(f"A média é {m}")
        if m >= 5:
            print(f" {self.nome} está Aprovado")
        else:
            return print(f"o aluno {self.nome} está reprovado")
        
matheus = AlunoNotas("Matheus")

matheus.adicionar_nota(2)
matheus.adicionar_nota(4)
matheus.adicionar_nota(6)
matheus.adicionar_nota(8)

matheus.lista_notas()
        