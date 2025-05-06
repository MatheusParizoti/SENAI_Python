## 4.Classe Livro
## Crie uma classe com título, autor, ano. 
# Adicione um método que imprima os dados formatados.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
            
    def descricao(self):
        
        print(f'a titulo do titulo é: {self.titulo}   o autor do carro é: {self.autor}  o ano do carro é {self.ano}')
        
teste = Livro("Nunes e Amigos","matheus",2002)
teste.descricao()