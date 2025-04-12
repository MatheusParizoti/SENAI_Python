import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# -----------------------------
# Tratamento dos dados
# -----------------------------
df['grupo_de_desastre'] = df['grupo_de_desastre'].replace({'R\$': '', ',': '', '  +': ' '}, regex=True)
df['grupo_de_desastre'] = df['grupo_de_desastre'].str.strip()

# -----------------------------
# Frequência geral dos grupos
# -----------------------------
grupo_valores = df['grupo_de_desastre'].dropna()
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
df_validos = df.dropna(subset=['grupo_de_desastre'])
df_sudeste = df_validos[df_validos['Sigla_UF'].isin(siglas_sudeste)]

# Contagem por grupo no Sudeste
frequencia_sudeste = df_sudeste['grupo_de_desastre'].value_counts()
df_grupos['Quantidade_Sudeste'] = df_grupos['Grupo'].map(frequencia_sudeste).fillna(0).astype(int)
df_grupos['Porcentagem_Sudeste_no_Grupo'] = (df_grupos['Quantidade_Sudeste'] / df_grupos['Quantidade_Total']) * 100

# -----------------------------
# Porcentagem de cada estado do Sudeste por grupo
# -----------------------------
# Criar DataFrame pivot com contagem por estado e grupo
df_estados_sudeste = df_sudeste.groupby(['grupo_de_desastre', 'Sigla_UF']).size().unstack(fill_value=0)

# Calcular a porcentagem de cada estado em relação ao total da região Sudeste no grupo
df_estados_pct = df_estados_sudeste.div(df_estados_sudeste.sum(axis=1), axis=0) * 100
df_estados_pct = df_estados_pct[['SP', 'RJ', 'MG', 'ES']]  # Garantir ordem

# Juntar com o DataFrame principal
df_final = df_grupos.merge(df_estados_pct, left_on='Grupo', right_index=True, how='left')

# Exibir resultado final
print("\nParticipação do Sudeste e de cada estado dentro de cada grupo de desastre:")
print(df_final[['Grupo', 'Quantidade_Total', 'Quantidade_Sudeste', 'Porcentagem_Sudeste_no_Grupo', 'SP', 'RJ', 'MG', 'ES']].to_string(
    index=False, formatters={
        'Porcentagem_Sudeste_no_Grupo': '{:.2f}%'.format,
        'SP': '{:.2f}%'.format,
        'RJ': '{:.2f}%'.format,
        'MG': '{:.2f}%'.format,
        'ES': '{:.2f}%'.format
    }))
