# 4.Classe Livro
# Crie uma classe com título, autor, ano. Adicione um método que imprima os dados formatados.

class Livro():
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def imprimir_dados(self):
        for chave, valor in self.__dict__.items():
            print(f"{chave.capitalize()}: {valor}")


# Criando um livro
meu_livro = Livro("1984", "George Orwell", 1949)

# Imprimindo com for
meu_livro.imprimir_dados()