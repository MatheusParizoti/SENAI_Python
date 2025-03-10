def fibonacci_n(n):
    # Casos base para n = 0 ou n = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    # Iniciar os dois primeiros números da sequência
    a, b = 1, 1
    
    # Calcular o valor na n-ésima posição
    for i in range(2, n + 1):
        a, b = b, a + b  # Atualiza os valores de a e b
    
    return b

# Solicitar ao usuário a posição desejada
n = int(input("Digite a posição n da sequência: "))

# Imprimir o valor na posição n da sequência
print(f"O valor {n} da sequência é: {fibonacci_n(n)}")
