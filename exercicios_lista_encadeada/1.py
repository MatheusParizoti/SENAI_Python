## Conceito: Percorremos a lista do início até o fim comparando com o valor procurado.
## Enunciado: Faça um teste buscando os valores 20 e 50.

def buscar(inicio, valor):
    atual=inicio
    while atual:
        if atual["valor"]==valor:
            return True
        atual=atual["próximo"]
    return False

lista = {
    "valor":20,
    "próximo":{
        
        "valor":30,
        "próximo":{
            
            "valor":50,
            "próximo":None
        }
    }
}

print(buscar(lista,50))

no ={"valor":8, "proximo":None}
no1={"valor": 5, "próximo":no}

print(no1)
print()
print(lista)