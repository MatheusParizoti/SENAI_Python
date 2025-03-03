import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame
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

# Verificar se a coluna 'Regiao' foi criada corretamente
if df['Regiao'].isnull().any():
    print("Atenção! Existem valores nulos na coluna 'Regiao'.")
    print(df[df['Regiao'].isnull()])  # Exibir linhas com valores nulos

# Filtrar apenas as regiões Nordeste e Sudeste
df_filtered = df[df['Regiao'].isin(['Nordeste', 'Sudeste'])]

# Verificar se há dados na filtragem
print(f"Quantidade de dados após filtrar as regiões Nordeste e Sudeste: {df_filtered.shape[0]}")

# Contagem de desastres por Estado
desastres_estado = df_filtered.groupby('Sigla_UF').size().reset_index(name='Num_Desastres')

# Identificar o grupo de desastre mais frequente por Estado
grupo_frequente_estado = df_filtered.groupby('Sigla_UF')['grupo_de_desastre'].agg(lambda x: x.mode()[0]).reset_index()

# Identificar a descrição da tipologia mais frequente por Estado
tipologia_frequente_estado = df_filtered.groupby('Sigla_UF')['descricao_tipologia'].agg(lambda x: x.mode()[0]).reset_index(name='Tipologia_Mais_Frequente')

# Juntar as informações (número de desastres, grupo de desastre mais frequente e tipologia mais frequente)
resultado_estado = pd.merge(desastres_estado, grupo_frequente_estado, on='Sigla_UF')
resultado_estado = pd.merge(resultado_estado, tipologia_frequente_estado, on='Sigla_UF')

# Agora, incluir a coluna 'Regiao' do DataFrame original
resultado_estado = pd.merge(resultado_estado, df[['Sigla_UF', 'Regiao']].drop_duplicates(), on='Sigla_UF', how='left')

# Para cada região, obter os 5 estados com mais desastres (permitindo repetições de estados)
top_5_estados = resultado_estado.sort_values(by='Num_Desastres', ascending=False).groupby('Regiao').head(5).reset_index(drop=True)

# Exibir a tabela com os resultados
print(top_5_estados)

# Gráficos de barras por região
regioes = top_5_estados['Regiao'].unique()

# Definir o tamanho do gráfico
plt.figure(figsize=(12, 8))

for regiao in regioes:
    # Filtrando os dados para a região
    region_data = top_5_estados[top_5_estados['Regiao'] == regiao]

    # Plotando os gráficos
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Num_Desastres', y='Sigla_UF', data=region_data, hue='grupo_de_desastre', palette='Set2')

    # Adicionar título com a tipologia mais frequente
    for idx, row in region_data.iterrows():
        plt.text(row['Num_Desastres'] + 2, idx, f"{row['Tipologia_Mais_Frequente']}", va='center', ha='left', fontsize=9, color='black')

    # Adicionar título e labels
    plt.title(f'Top 5 Estados com Mais Desastres - Região {regiao}')
    plt.xlabel('Número de Desastres')
    plt.ylabel('Estado')
    plt.legend(title='Grupo de Desastre')

    # Exibir o gráfico
    plt.show()

    # Exibir tabela com os valores para cada estado
    print(f"Tabela de Estados - Região {regiao}")
    print(region_data[['Sigla_UF', 'Num_Desastres', 'grupo_de_desastre', 'Tipologia_Mais_Frequente','Sigla_UF']])
    print("\n" + "="*50 + "\n")
