def rotina():

    n1 = str(input("Digite um numero: "))
    
    crescente = ''.join(sorted(n1))
    
    decrescente = ''.join(sorted(n1, reverse=True))
    
    reverso = n1[:-1]
    
    print("")
    print(f"Crescente: {crescente}")
    print(f"Decrescente: {decrescente}")
    print(f"Reverso: {reverso}")

    # Explicação:
    # .join() vai juntar o str novamente
    # sorted() vai ordenar ordem crescente
    # reverse=True) vai ordenar decrescente
    # [:-1] os : esta selecionando tudo que tem dentro da minha variavel
    #          -1 vai reverter a ordem

rotina()
