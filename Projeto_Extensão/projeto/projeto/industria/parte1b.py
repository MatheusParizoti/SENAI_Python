import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_Indústria (R$)', removendo caracteres de moeda e espaços
df['PEPR_Indústria (R$)'] = df['PEPR_Indústria (R$)'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_Indústria (R$)' para numérico, forçando erros para NaN
df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# Certificar-se de que a coluna 'Data_Evento' é do tipo datetime
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# Extrair o ano da coluna 'Data_Evento'
df['Ano'] = df['Data_Evento'].dt.year

# Filtrar os dados apenas para a sigla 'ES'
df_filtrado_ES = df[df['Sigla_UF'] == 'ES']

# Filtrar para mostrar apenas valores maiores que zero
df_maiores_que_zero_ES = df_filtrado_ES[df_filtrado_ES['PEPR_Indústria (R$)'] > 0]

# Agrupar os dados por sigla, valor, nome do município e ano, contando quantas vezes cada valor aparece
resultados_ES = df_maiores_que_zero_ES.groupby(['Sigla_UF', 'PEPR_Indústria (R$)', 'Nome_Municipio', 'Ano']).size().reset_index(name='Contagem')

# Ordenar os resultados por valor em ordem decrescente
resultados_sorted_ES = resultados_ES.sort_values(by=['PEPR_Indústria (R$)'], ascending=False)

# Para pegar os 10 maiores valores para 'ES'
top_10_ES = resultados_sorted_ES.head(10)

# Agora, adicionar a coluna 'descricao_tipologia' ao 'top_10_ES'
# Certifique-se de que a coluna 'descricao_tipologia' existe no DataFrame original
df['descricao_tipologia'] = df['descricao_tipologia']  # Apenas como exemplo; altere conforme necessário

# Adicionar a 'descricao_tipologia' ao 'top_10_ES' com base na correspondência das colunas
top_10_ES = top_10_ES.merge(df[['Sigla_UF', 'Nome_Municipio', 'PEPR_Indústria (R$)', 'Ano', 'descricao_tipologia']], 
                             on=['Sigla_UF', 'Nome_Municipio', 'PEPR_Indústria (R$)', 'Ano'], 
                             how='left')

# Exibir os resultados do Top 10 com a descrição da tipologia para 'ES'
print("\nTop 10 maiores danos para a sigla 'ES' com descrição da tipologia:")
for index, row in top_10_ES.iterrows():
    print(f"  Valor: {row['PEPR_Indústria (R$)']} - {row['Nome_Municipio']} - Ano: {row['Ano']} - Tipologia: {row['descricao_tipologia']}")

# Agora, calcular a descrição da tipologia mais frequente por ano para 'ES'
tipologia_mais_frequente_por_ano_ES = df_maiores_que_zero_ES.groupby(['Ano', 'descricao_tipologia']).size().reset_index(name='Contagem')

# Encontrar a tipologia mais frequente para cada ano
tipologia_mais_frequente_por_ano_ES = tipologia_mais_frequente_por_ano_ES.loc[tipologia_mais_frequente_por_ano_ES.groupby('Ano')['Contagem'].idxmax()]

# Exibir as tipologias mais frequentes por ano para 'ES'
print("\nTipologia mais frequente por ano para 'ES':")
print(tipologia_mais_frequente_por_ano_ES[['Ano', 'descricao_tipologia', 'Contagem']])
