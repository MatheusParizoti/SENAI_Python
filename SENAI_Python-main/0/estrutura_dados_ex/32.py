# 32-Peça ao usuário para inserir um nome e um telefone e armazene-os em um
# arquivo chamado contatos.txt.

info = str(input("Coloque seu nome: "))
info2 = str(input("Coloque seu telefone: "))

with open("contatos.txt","w") as arquivo:
    arquivo.write(info)
    arquivo.write(info2)