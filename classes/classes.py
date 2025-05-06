lista = []

# Para crir uma classe utiliza-se o nickname class
# Classe é um gabarito para criat um objeto
class MinhaClasse:
    valor = 10
    pass # Função que não executa nada 

objeto = MinhaClasse() # Criação de um objeto, instanciar uma classe
objeto_dois = MinhaClasse()

print(type(objeto))
objeto.valor = 15
print(objeto.valor)
print(objeto_dois.valor)
print(MinhaClasse.valor)



