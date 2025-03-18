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

# Filtrar para mostrar apenas valores maiores que zero
df_maiores_que_zero = df_filtrado[df_filtrado['PEPR_total_privado'] > 0]

# Adicionar a coluna 'Ano_Evento' extraindo o ano da coluna 'Data_Evento'
df_maiores_que_zero['Ano_Evento'] = pd.to_datetime(df_maiores_que_zero['Data_Evento'], errors='coerce').dt.year

# Contar os valores positivos por ano e sigla
contagem_positivos_por_ano_sigla = df_maiores_que_zero.groupby(['Ano_Evento', 'Sigla_UF']).size().unstack(fill_value=0)

# Exibir os resultados
print("\nContagem de valores positivos por ano e sigla:")
print(contagem_positivos_por_ano_sigla)