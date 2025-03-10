# Função para gerar os primeiros 'n' números de Fibonacci
def fibonacci(n):
    sequencia = [1, 1]  # Começamos com os dois primeiros números: 1 e 1
    
    # Geramos a sequência até atingir o número n
    while len(sequencia) < n:
        next_fib = sequencia[-1] + sequencia[-2]
        sequencia.append(next_fib)
    
    return sequencia

n1 = fibonacci(30)

print(n1)
