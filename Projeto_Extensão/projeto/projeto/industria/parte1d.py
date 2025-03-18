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

# Filtrar os dados especificamente para o Espírito Santo (ES) e ano de 2020
df_es_2020 = df_filtrado[(df_filtrado['Sigla_UF'] == 'ES') & (df_filtrado['Data_Evento'].dt.year == 2021)]

# Filtrar os dados para mostrar apenas valores maiores que zero na coluna 'PEPR_Indústria (R$)'
df_maiores_que_zero_es_2020 = df_es_2020[df_es_2020['PEPR_Indústria (R$)'] > 0]

# Selecionar as colunas de interesse: Município, PEPR_Indústria (R$), Data_Evento e descricao_tipologia
df_resultado = df_maiores_que_zero_es_2020[['Nome_Municipio', 'PEPR_Indústria (R$)', 'Data_Evento', 'descricao_tipologia']]

# Exibir os resultados
print(df_resultado)
