## Conceito: Se for o primeiro valor, atualizamos o início. Se for no meio ou fim, fazemos
## o nó anterior apontar para o próximo.
## Enunciado: Remova o valor 20 da lista 10 → 20 → 30.

def deletar(inicio, valor):
    atual=inicio
    anterior = None
    
    while atual: 
        if atual["valor"] == valor:  

            if anterior == None:  
                return atual["próximo"] 
            else:
                anterior["próximo"] = atual["próximo"]  
            return inicio  
        
        anterior = atual  
        atual = atual["próximo"] 
    
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

deletar(lista,20)
print(lista)
