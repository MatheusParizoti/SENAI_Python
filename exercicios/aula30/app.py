
montanha = 2500  
passo = 0.47  
escorregamento = 0.47  
passos_10 = (passo * 10) - escorregamento 

distancia_percorrida = 0
passos_totais = 0

while distancia_percorrida < montanha:
   
    distancia_percorrida += passos_10
    passos_totais += 10  
    
    if distancia_percorrida > montanha:
        excesso = distancia_percorrida - montanha
        passos_finais = excesso / passo
        passos_totais -= 10 - passos_finais
        break

print(f'O alpinista deu um total de {int(passos_totais)} passos.')
