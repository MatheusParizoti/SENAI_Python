import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_total_privado', removendo caracteres de moeda e espaços
df['PEPR_total_privado'] = df['PEPR_total_privado'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_total_privado' para numérico, forçando erros para NaN
df['PEPR_total_privado'] = pd.to_numeric(df['PEPR_total_privado'], errors='coerce')

# Filtrar os dados pelas siglas de interesse
siglas_interesse = ['SP', 'RJ', 'MG', 'ES']
df_filtrado = df[df['Sigla_UF'].isin(siglas_interesse)]

# Contar os valores não nulos
num_nao_nulos = df_filtrado['PEPR_total_privado'].notna().sum()

# Filtrar para mostrar apenas valores maiores que zero
df_maiores_que_zero = df_filtrado[df_filtrado['PEPR_total_privado'] > 0]

# Contar os valores positivos por sigla
contagem_positivos_por_sigla = df_maiores_que_zero.groupby('Sigla_UF').size()

# Exibir os resultados
print("")
print(f"Numeros de Danos: {num_nao_nulos}")
print(f"Danos acima de 0: {len(df_maiores_que_zero)}")

print("\nContagem de valores positivos para cada sigla:")
# Imprimir sigla e quantidade de valores positivos
for sigla, quantidade in contagem_positivos_por_sigla.items():
    print(f"Sigla {sigla}: {quantidade}")
