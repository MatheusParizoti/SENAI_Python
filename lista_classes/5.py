# 5.Classe Aluno com Notas
# Crie uma classe com nome e lista de notas. Implemente métodos para adicionar notas, calcular média e verificar aprovação.

class Notas():

    def __init__(self,nome):
        self.nome = nome
        
        self.lista_notas = []
    
    def adicionar(self,notas):
        self.notas = notas
        self.lista_notas.append(self.notas)
    
    def mostrar_lista(self):
        return f"Notas de {self.nome}: {self.lista_notas}"

    def media(self):
        m = sum(self.lista_notas)
        final = m / len(self.lista_notas)
        return f"Media do aluno {self.nome} é {final}"
    
    def aprovacao(self):
        media = sum(self.lista_notas) / len(self.lista_notas)

        if media <= 5:
            return f"Aluno {self.nome} está reprovado"
        else:
            return f"Aluno {self.nome} está aprovado"

senai = Notas("Matheus")
senai.adicionar(10)
senai.adicionar(7)
senai.adicionar(9)
senai.adicionar(3)
senai.adicionar(1)
mostrar = senai.mostrar_lista()
media = senai.media()

print(mostrar)
print(media)
print(senai.aprovacao())



        