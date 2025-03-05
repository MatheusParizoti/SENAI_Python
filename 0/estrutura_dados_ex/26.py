# 26-Peça ao usuário para inserir uma data no formato dd/mm/aaaa e exiba o dia da
# semana correspondente.

import calendar as cl

data = input("Coloque o dia em que você quer saber, exemplo (dd/mm/aaaa): ")

dia, mes, ano = map(int, data.split('/'))

numero_dia = cl.weekday(ano, mes, dia)
dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

print("")
print(f"O dia da semana é: {dias_da_semana[numero_dia]}")
