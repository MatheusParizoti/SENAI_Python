# 30-Crie um programa que crie e escreva a frase "Python é incrível!" em um arquivo
# chamado texto.txt.

with open("texto.txt","w") as arquivo:
    arquivo.write("Python é incrível")