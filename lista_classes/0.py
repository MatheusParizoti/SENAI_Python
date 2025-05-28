# 0. Classe Pessoa
# Crie uma classe com os atributos nome e idade. Adicione um método que imprime uma apresentação.

class Pessoa():
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
    
    def visualizar(self):
        return f"Nome: {self.nome} - Idade: {self.idade}"


pessoa = Pessoa("Matheus",18)
ver = pessoa.visualizar()
print(ver)


