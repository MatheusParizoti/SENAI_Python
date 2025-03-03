import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
try:
    df = pd.read_excel("df_reduzido.xlsx")
    print(df.head())  # Para imprimir as primeiras linhas do DataFrame
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Dicionário de mapeamento dos estados para suas regiões
regioes = {
    'Sudeste': ['ES', 'MG', 'RJ', 'SP']
}

# Criar uma coluna 'Região' no DataFrame com base no mapeamento de regiões
def obter_regiao(uf):
    for regiao, ufs in regioes.items():
        if uf in ufs:
            return regiao
    return 'Desconhecida'

df['Região'] = df['Sigla_UF'].apply(obter_regiao)

# Garantir que os valores de "PEPR_Indústria (R$)" sejam numéricos
df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# Preencher NaN com zero (caso haja valores ausentes)
df['PEPR_Indústria (R$)'].fillna(0, inplace=True)

# Converter a coluna 'Data_Evento' para datetime
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# Extrair o ano da data
df['Ano'] = df['Data_Evento'].dt.year

# Filtrar dados para a Região Sudeste
df_sudeste = df[df['Região'] == 'Sudeste']

# Filtrar os dados para os anos entre 2000 e 2023
df_sudeste_ano_range = df_sudeste[(df_sudeste['Ano'] >= 2000) & (df_sudeste['Ano'] <= 2023)]

# Agrupar por estado (UF), ano e contar o número de desastres
# Usaremos a coluna "grupo_de_desastre" para contar os desastres
desastres_estado_ano = df_sudeste_ano_range.groupby(['Sigla_UF', 'Ano']).size().reset_index(name='Numero_de_Desastres')

# Agrupar por estado (UF) e somar o número de desastres para cada ano
desastres_estado_ano_total = desastres_estado_ano.groupby('Sigla_UF')['Numero_de_Desastres'].sum()

# Ordenar os estados da Região Sudeste do maior para o menor número de desastres
desastres_estado_ano_ordenado = desastres_estado_ano_total.sort_values(ascending=False)

# Selecionar os 3 maiores estados (UFs) em termos de número de desastres
top_3_ufs = desastres_estado_ano_ordenado.head(3).index

# Criar os gráficos de linha para cada um dos 3 maiores estados
plt.figure(figsize=(15, 10))

for i, uf in enumerate(top_3_ufs, 1):
    # Filtrar os dados para o estado (UF) atual dentro do intervalo de anos
    df_uf = desastres_estado_ano[desastres_estado_ano['Sigla_UF'] == uf]
    
    # Agrupar os dados por ano e somar os números de desastres
    desastres_ano_uf = df_uf.groupby('Ano')['Numero_de_Desastres'].sum()
    
    # Criar o gráfico de linha para o estado (UF) atual
    plt.subplot(3, 1, i)
    sns.lineplot(x=desastres_ano_uf.index, y=desastres_ano_uf.values, marker='o')
    
    # Personalizar o gráfico
    plt.title(f'Número de Desastres em {uf} por Ano (2000-2023)', fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Número de Desastres', fontsize=12)
    plt.grid(True)

    # Exibir os valores de desastres ao lado de cada ponto no gráfico
    for year, value in zip(desastres_ano_uf.index, desastres_ano_uf.values):
        plt.text(year, value, f'{value}', fontsize=9, ha='left', va='bottom')

# Ajustar o layout para que os gráficos não se sobreponham
plt.tight_layout()

# Exibir os gráficos
plt.show()


# import pandas as pd
# import plotly.express as px

# # Carregar os dados
# try:
#     df = pd.read_excel("df_reduzido.xlsx")
#     print(df.head())  # Para imprimir as primeiras linhas do DataFrame
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# # Dicionário de mapeamento dos estados para suas regiões
# regioes = {
#     'Sudeste': ['ES', 'MG', 'RJ', 'SP']
# }

# # Criar uma coluna 'Região' no DataFrame com base no mapeamento de regiões
# def obter_regiao(uf):
#     for regiao, ufs in regioes.items():
#         if uf in ufs:
#             return regiao
#     return 'Desconhecida'

# df['Região'] = df['Sigla_UF'].apply(obter_regiao)

# # Garantir que os valores de "PEPR_Indústria (R$)" sejam numéricos
# df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# # Preencher NaN com zero (caso haja valores ausentes)
# df['PEPR_Indústria (R$)'].fillna(0, inplace=True)

# # Converter a coluna 'Data_Evento' para datetime
# df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# # Extrair o ano da data
# df['Ano'] = df['Data_Evento'].dt.year

# # Filtrar dados para a Região Sudeste
# df_sudeste = df[df['Região'] == 'Sudeste']

# # Filtrar os dados para os anos entre 2000 e 2023
# df_sudeste_ano_range = df_sudeste[(df_sudeste['Ano'] >= 2000) & (df_sudeste['Ano'] <= 2023)]

# # Agrupar por estado (UF), ano e contar o número de desastres
# desastres_estado_ano = df_sudeste_ano_range.groupby(['Sigla_UF', 'Ano']).size().reset_index(name='Numero_de_Desastres')

# # Agrupar por estado (UF) e somar o número de desastres para cada ano
# desastres_estado_ano_total = desastres_estado_ano.groupby('Sigla_UF')['Numero_de_Desastres'].sum()

# # Ordenar os estados da Região Sudeste do maior para o menor número de desastres
# desastres_estado_ano_ordenado = desastres_estado_ano_total.sort_values(ascending=False)

# # Selecionar os 3 maiores estados (UFs) em termos de número de desastres
# top_3_ufs = desastres_estado_ano_ordenado.head(3).index

# # Preparar os dados para plotagem
# # Criar o gráfico de linha para cada estado, mostrando o valor de dano à indústria
# fig = px.line(desastres_estado_ano, x='Ano', y='Numero_de_Desastres', color='Sigla_UF',
#               title='Número de Desastres por Estado e Ano (2000-2023)',
#               labels={'Numero_de_Desastres': 'Número de Desastres', 'Ano': 'Ano'},
#               markers=True)

# # Mostrar os danos à indústria como texto ao passar o mouse
# fig.update_traces(
#     hovertemplate='<b>Estado:</b> %{text}<br>' +
#                   '<b>Ano:</b> %{x}<br>' +
#                   '<b>Desastres:</b> %{y}<br>' +
#                   '<b>Danos à Indústria (R$):</b> %{customdata[0]}',
#     customdata=df_sudeste_ano_range[['Sigla_UF', 'PEPR_Indústria (R$)']].values
# )

# # Exibir o gráfico interativo
# fig.show()
