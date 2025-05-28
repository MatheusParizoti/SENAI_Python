# 6.Classe Produto
# Crie uma classe com nome, preço e quantidade_estoque. Adicione métodos para vender, repor e aplicar desconto.

class Produto():
    def __init__(self,nome,preco,quantidade_estoque=5):

        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
    
    def vender(self, dinheiro):
        print(f"O valor do {self.nome} é R${self.preco}")
        if dinheiro >= self.preco:
            if self.quantidade_estoque > 0:
                self.quantidade_estoque -= 1
                return "Compra feita"
            else:
                return "Produto fora de estoque"
        else:
            return "Falta de dinheiro"
    
    def verificar_estoque(self):
        return f"O numero de {self.nome} dentro do nosso estoque é {self.quantidade_estoque}"
    
    def repor(self):
        if self.quantidade_estoque < 5:
            r = 5 - self.quantidade_estoque
            return f"O numero de {self.nome} que faltam no estoque é {r}"
        else:
            return "O estoque está cheio"
        
    def desconto(self):
        desconto = self.preco / 10
        if self.quantidade_estoque < 3:
            self.preco -= desconto
            return f"Agora o preço dos {self.nome} está 10% mais barato: {self.preco}"
    
# Criando um produto
lapis = Produto("Lápis", 12)

# 1. Verificando estoque inicial
print(lapis.verificar_estoque())

# 2. Tentando comprar 1 lápis com dinheiro suficiente
print(lapis.vender(14))
print(lapis.verificar_estoque())

# 3. Comprando até o estoque ficar abaixo de 3
print(lapis.vender(14))
print(lapis.vender(14))  # estoque agora será 2
print(lapis.verificar_estoque())

# 4. Aplicando desconto (estoque < 3)
print(lapis.desconto())

# 5. Tentando comprar com valor exato do novo preço com desconto
print(lapis.vender(lapis.preco))
print(lapis.verificar_estoque())

# 6. Comprando até zerar o estoque
print(lapis.vender(15))
print(lapis.vender(15))  # agora fora de estoque
print(lapis.verificar_estoque())

# 7. Tentando aplicar desconto com estoque 0
print(lapis.desconto())

# 8. Repondo o estoque até o máximo (5)
print(lapis.repor())
print(lapis.verificar_estoque())


        

    

    # 

        