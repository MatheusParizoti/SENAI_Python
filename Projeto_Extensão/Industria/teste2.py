import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_Indústria (R$)', removendo caracteres de moeda e espaços
df['PEPR_Indústria (R$)'] = df['PEPR_Indústria (R$)'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_Indústria (R$)' para numérico, forçando erros para NaN
df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# Filtrar os dados pelas siglas de interesse
siglas_interesse = ['SP', 'RJ', 'MG', 'ES']
df_filtrado = df[df['Sigla_UF'].isin(siglas_interesse)]

# Contar os valores não nulos
num_nao_nulos = df_filtrado['PEPR_Indústria (R$)'].notna().sum()

# Filtrar para mostrar apenas valores maiores que zero
df_maiores_que_zero = df_filtrado[df_filtrado['PEPR_Indústria (R$)'] > 0]

# Contar os valores positivos por sigla
contagem_positivos_por_sigla = df_maiores_que_zero.groupby('Sigla_UF').size()

# Exibir os resultados
print("")
print(f"Valores não nulos: {num_nao_nulos}")
print(f"Valores positivos: {len(df_maiores_que_zero)}")

print("\nContagem de valores positivos para cada sigla:")
# Imprimir sigla e quantidade de valores positivos
for sigla, quantidade in contagem_positivos_por_sigla.items():
    print(f"Sigla {sigla}: {quantidade}")



# # Calcular o menor e o maior valor positivo por sigla, e contar quantas vezes esses valores aparecem
# resultados = []

# for sigla in siglas_interesse:
#     # Filtrar os valores para cada sigla
#     df_sigla = df_maiores_que_zero[df_maiores_que_zero['Sigla_UF'] == sigla]
    
#     if not df_sigla.empty:
#         # Obter o menor e maior valor
#         menor_valor = df_sigla['PEPR_Indústria (R$)'].min()
#         maior_valor = df_sigla['PEPR_Indústria (R$)'].max()
        
#         # Contar quantas vezes o menor e maior valor aparecem
#         count_menor = df_sigla[df_sigla['PEPR_Indústria (R$)'] == menor_valor].shape[0]
#         count_maior = df_sigla[df_sigla['PEPR_Indústria (R$)'] == maior_valor].shape[0]
        
#         # Adicionar o resultado para essa sigla
#         resultados.append({
#             'Sigla': sigla,
#             'Menor Valor': menor_valor,
#             'Contagem Menor': count_menor,
#             'Maior Valor': maior_valor,
#             'Contagem Maior': count_maior
#         })

# # Criar um DataFrame com os resultados
# df_resultados = pd.DataFrame(resultados)

# # Ordenar os resultados pela sigla em ordem crescente
# df_resultados = df_resultados.sort_values(by='Sigla')

# # Exibir os resultados
# print(df_resultados)