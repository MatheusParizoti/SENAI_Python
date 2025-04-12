import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# -----------------------------
# Tratamento dos dados
# -----------------------------
df['descricao_tipologia'] = df['descricao_tipologia'].replace({'R\$': '', ',': '', '  +': ' '}, regex=True)
df['descricao_tipologia'] = df['descricao_tipologia'].str.strip()

# -----------------------------
# Frequência geral dos grupos
# -----------------------------
grupo_valores = df['descricao_tipologia'].dropna()
frequencia_absoluta = grupo_valores.value_counts()
frequencia_relativa = (frequencia_absoluta / grupo_valores.shape[0]) * 100

# DataFrame com grupos
df_grupos = pd.DataFrame({
    'Grupo': frequencia_absoluta.index,
    'Quantidade_Total': frequencia_absoluta.values,
    'Porcentagem_Total': frequencia_relativa.values
}).sort_values(by='Quantidade_Total', ascending=False)

print("\nTodos os grupos de desastre com suas quantidades e porcentagens:")
print(df_grupos.to_string(index=False, formatters={'Porcentagem_Total': '{:.2f}%'.format}))

# -----------------------------
# Análise da participação do Sudeste por grupo
# -----------------------------
siglas_sudeste = ['SP', 'RJ', 'MG', 'ES']

# Filtrar válidos
df_validos = df.dropna(subset=['descricao_tipologia'])

# Filtrar apenas os da região Sudeste
df_sudeste = df_validos[df_validos['Sigla_UF'].isin(siglas_sudeste)]

# Contagem por grupo no Sudeste
frequencia_sudeste = df_sudeste['descricao_tipologia'].value_counts()

# Adicionar a contagem do Sudeste ao DataFrame de grupos
df_grupos['Quantidade_Sudeste'] = df_grupos['Grupo'].map(frequencia_sudeste).fillna(0).astype(int)

# Calcular porcentagem da participação do Sudeste em cada grupo
df_grupos['Porcentagem_Sudeste_no_Grupo'] = (df_grupos['Quantidade_Sudeste'] / df_grupos['Quantidade_Total']) * 100

# Mostrar o resultado final
print("\nParticipação da região Sudeste dentro de cada grupo de desastre:")
print(df_grupos[['Grupo', 'Quantidade_Total', 'Quantidade_Sudeste', 'Porcentagem_Sudeste_no_Grupo']].to_string(
    index=False, formatters={'Porcentagem_Sudeste_no_Grupo': '{:.2f}%'.format}))
