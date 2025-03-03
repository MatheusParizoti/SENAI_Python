# import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt

# # Carregar o shapefile dos estados brasileiros
# gdf = gpd.read_file("BR_UF_2023.shp")

# # Carregar os dados da sua planilha
# df = pd.read_excel("df_reduzido.xlsx")

# # Criar a coluna de regiões no seu DataFrame
# def definir_regiao(sigla):
#     if sigla in ['SP', 'RJ', 'MG', 'ES']:
#         return 'Sudeste'
#     elif sigla in ['PR', 'SC', 'RS']:
#         return 'Sul'
#     elif sigla in ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'MA']:
#         return 'Norte'
#     elif sigla in ['BA', 'CE', 'SE', 'AL', 'PE', 'PB', 'RN', 'PI', 'MA', 'GO']:
#         return 'Nordeste'
#     elif sigla in ['MT', 'MS', 'DF']:
#         return 'Centro-Oeste'

# df['Regiao'] = df['Sigla_UF'].apply(definir_regiao)

# # Filtrar os dados da região Sudeste
# df_sudeste = df[df['Regiao'] == 'Sudeste']

# # Contando as ocorrências de cada 'descricao_tipologia' na Sudeste
# tipologia_por_desastre_sudeste = df_sudeste.groupby('Sigla_UF').size().reset_index(name='contagem')

# # Integrar as contagens de tipologia no DataFrame 'df'
# df_sudeste = df_sudeste.merge(tipologia_por_desastre_sudeste[['Sigla_UF', 'contagem']], on='Sigla_UF', how='left')

# # Filtrar apenas os estados da região Sudeste no GeoDataFrame
# gdf_sudeste = gdf[gdf['SIGLA_UF'].isin(['SP', 'RJ', 'MG', 'ES'])]

# # Integrar as contagens de desastre com o GeoDataFrame dos estados da Sudeste
# gdf_sudeste = gdf_sudeste.merge(df_sudeste[['Sigla_UF', 'contagem']], left_on='SIGLA_UF', right_on='Sigla_UF', how='left')

# # Plotando o mapa com os estados da região Sudeste e as contagens de desastre
# fig, ax = plt.subplots(figsize=(10, 8))

# # O mapa será colorido de acordo com a quantidade de desastres, usando a coluna 'contagem'
# gdf_sudeste.plot(column='contagem', ax=ax, legend=True,
#                 legend_kwds={'label': "Número de Ocorrências de Desastres",
#                              'orientation': "horizontal"},
#                 cmap='OrRd', edgecolor='black')

# # Título do mapa
# plt.title('Número de Ocorrências de Desastres na Região Sudeste do Brasil', fontsize=16)

# # Exibindo o mapa
# plt.show()


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o shapefile dos estados brasileiros
gdf = gpd.read_file("BR_UF_2023.shp")

# Carregar os dados da sua planilha
df = pd.read_excel("df_reduzido.xlsx")

# Criar a coluna de regiões no seu DataFrame
def definir_regiao(sigla):
    if sigla in ['SP', 'RJ', 'MG', 'ES']:
        return 'Sudeste'
    elif sigla in ['PR', 'SC', 'RS']:
        return 'Sul'
    elif sigla in ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'MA']:
        return 'Norte'
    elif sigla in ['BA', 'CE', 'SE', 'AL', 'PE', 'PB', 'RN', 'PI', 'MA', 'GO']:
        return 'Nordeste'
    elif sigla in ['MT', 'MS', 'DF']:
        return 'Centro-Oeste'

df['Regiao'] = df['Sigla_UF'].apply(definir_regiao)

# Contando as ocorrências de cada 'descricao_tipologia' e criando a coluna 'contagem'
tipologia_por_desastre = df.groupby('descricao_tipologia').size().reset_index(name='contagem')

# Integrando a coluna 'contagem' ao DataFrame 'df'
df = df.merge(tipologia_por_desastre[['descricao_tipologia', 'contagem']], on='descricao_tipologia', how='left')

# Filtrar apenas os estados da região Sudeste (SP, RJ, MG, ES)
gdf_sudeste = gdf[gdf['SIGLA_UF'].isin(['SP', 'RJ', 'MG', 'ES'])]

# Plotando o mapa com os estados da região Sudeste
gdf_sudeste.plot(figsize=(8, 5), color='lightblue', edgecolor='black')
plt.title('Estados da Região Sudeste do Brasil')
plt.show()