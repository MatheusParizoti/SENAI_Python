# 31-Crie um programa que leia o arquivo texto.txt e exiba o conteúdo na tela.

with open("texto.txt","r") as arquivo:
    print(arquivo.read())