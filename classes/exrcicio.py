class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nota = []
        
    def adicionar_nota(self, nota):
        self.nota.append(nota)
        
    def media(self):
        m = sum(self.nota) / len(self.nota)
        
        print(f"A média é {m}")
        print(f"{self.nome} está Aprovado")


matheus = Aluno('Matheus', 18)

matheus.adicionar_nota(2)
matheus.adicionar_nota(4)
matheus.adicionar_nota(6)
matheus.adicionar_nota(8)

matheus.media()

