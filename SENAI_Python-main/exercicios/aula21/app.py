soma = 0
q = []
media = 0
mediap = 0
somap = 0
ma = 0
me = float("inf")

for i in range(10):
    ns = int(input("coloque os numeros: "))

    q.append(i)
    soma += ns
   
    
    if ns > ma:
        ma = ns

    if ns < me:
        me = ns

   
        
media = soma / ns

    

print(soma, len(q), media, ma, me)



    

