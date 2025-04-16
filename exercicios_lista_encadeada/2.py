## 


def adicionar(atual,valor):
    
    while atual:
        if atual["próximo"]==None:

            no ={"valor":valor, "próximo":None}

            atual["próximo"]= no
            return True
        atual=atual["próximo"]
    return False

lista = {
    "valor":10,
    "próximo":{
        
        "valor":20,
        "próximo":{
            
            "valor":30,
            "próximo":None
        }
    }
}
print(lista)
adicionar(lista,40)
print(lista)