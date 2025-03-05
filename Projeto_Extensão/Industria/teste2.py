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
