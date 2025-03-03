# 29-Simule o lançamento de um dado (números de 1 a 6) e exiba o resultado após
# uma pausa de 2 segundos.

import random
import time

num = random.randint(1, 6)
print("Jogando o Dado")
time.sleep(2)

print(f"O resultado do Dado é: {num}")