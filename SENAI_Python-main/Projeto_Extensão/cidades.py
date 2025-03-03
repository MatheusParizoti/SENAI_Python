import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


try:
    df = pd.read_excel("df_reduzido.xlsx")
    print(df.head())  # Para imprimir as primeiras linhas do DataFrame
except Exception as e:
    print(f"Ocorreu um erro: {e}")
# Mapeamento de estados para regiões do Brasil
regiao_uf = {
    'AC': 'Norte', 'AL': 'Nordeste', 'AP': 'Norte', 'AM': 'Norte', 'BA': 'Nordeste', 'CE': 'Nordeste', 
    'DF': 'Centro-Oeste', 'ES': 'Sudeste', 'GO': 'Centro-Oeste', 'MA': 'Nordeste', 'MT': 'Centro-Oeste', 
    'MS': 'Centro-Oeste', 'MG': 'Sudeste', 'PA': 'Norte', 'PB': 'Nordeste', 'PR': 'Sul', 'PE': 'Nordeste', 
    'PI': 'Nordeste', 'RJ': 'Sudeste', 'RN': 'Nordeste', 'RS': 'Sul', 'RO': 'Norte', 'RR': 'Norte', 
    'SC': 'Sul', 'SP': 'Sudeste', 'SE': 'Nordeste', 'TO': 'Norte'
}

# Adicionar coluna 'Regiao' com base na Sigla_UF
df['Regiao'] = df['Sigla_UF'].map(regiao_uf)

# Contagem de desastres por Município e Região
desastres_municipio_regiao = df.groupby(['Nome_Municipio', 'Regiao']).size().reset_index(name='Num_Desastres')

# Identificar o grupo de desastre mais frequente por município
grupo_frequente = df.groupby(['Nome_Municipio', 'Regiao'])['grupo_de_desastre'].agg(lambda x: x.mode()[0]).reset_index()

# Juntar as duas informações (número de desastres e grupo de desastre mais frequente)
resultado = pd.merge(desastres_municipio_regiao, grupo_frequente, on=['Nome_Municipio', 'Regiao'])

# Para cada região, obter as 5 cidades com mais desastres
top_5_cidades = resultado.groupby('Regiao').apply(lambda x: x.nlargest(5, 'Num_Desastres')).reset_index(drop=True)

# Gráficos de barras por região
regioes = top_5_cidades['Regiao'].unique()

# Definir o tamanho do gráfico
plt.figure(figsize=(12, 8))

for regiao in regioes:
    # Filtrando os dados para a região
    region_data = top_5_cidades[top_5_cidades['Regiao'] == regiao]

    # Plotando os gráficos
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Num_Desastres', y='Nome_Municipio', data=region_data, hue='grupo_de_desastre', palette='Set2')

    # Adicionar título e labels
    plt.title(f'Top 5 Cidades com Mais Desastres - Região {regiao}')
    plt.xlabel('Número de Desastres')
    plt.ylabel('Município')
    plt.legend(title='Grupo de Desastre')

    # Exibir o gráfico
    plt.show()
