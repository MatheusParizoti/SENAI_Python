n1 = int(input("Digite o ano em que voce entrou para a empresa: "))
atual = 2025
si = 1000
percentual_aumento = 0.015
# faça um for em que o conte do n1 até o ano atual
# e imprima o ano e o tempo que a pessoa está na empresa
total = atual - n1

for i in range(n1, atual):
    if i == n1: 
        aumento = si * percentual_aumento
        si += aumento
    else:  
        percentual_aumento *= 2 
        aumento = si * percentual_aumento
        si += aumento

print(f"Voce está na empresa a {total} anos")
print(f'salario: {si:.2f}')



    

