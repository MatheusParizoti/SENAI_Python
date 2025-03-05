import pandas as pd
import matplotlib.pyplot as plt

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

# Filtrar dados para a Região Sudeste
df_sudeste = df[df['Região'] == 'Sudeste']

# 1. Total de danos à indústria por ano
df_sudeste['Ano'] = pd.to_datetime(df_sudeste['Data_Evento']).dt.year
danos_por_ano = df_sudeste.groupby('Ano')['PEPR_Indústria (R$)'].sum()
print("\nDanos à Indústria por Ano na Região Sudeste:")
print(danos_por_ano)

# 2. Estatísticas de danos à indústria por estado
estatisticas_estado = df_sudeste.groupby('Sigla_UF')['PEPR_Indústria (R$)'].agg(['sum', 'mean', 'std', 'max'])
print("\nEstatísticas de Danos à Indústria por Estado na Região Sudeste:")
print(estatisticas_estado)

# 3. Estatísticas de danos à indústria por município
estatisticas_municipio = df_sudeste.groupby('Nome_Municipio')['PEPR_Indústria (R$)'].agg(['sum', 'mean', 'max'])
print("\nEstatísticas de Danos à Indústria por Município na Região Sudeste:")
print(estatisticas_municipio)

# 4. Tendência de danos à indústria ao longo do tempo
danos_por_ano.plot(kind='line')
plt.title('Tendência de Danos à Indústria por Ano na Região Sudeste')
plt.xlabel('Ano')
plt.ylabel('Danos à Indústria (R$)')
plt.show()

# 5. Relação entre número de mortos e danos à indústria
df_sudeste['DH_MORTOS'] = pd.to_numeric(df_sudeste['DH_MORTOS'], errors='coerce')
correlacao_mortos_danos = df_sudeste[['DH_MORTOS', 'PEPR_Indústria (R$)']].corr()
print("\nCorrelação entre Número de Mortos e Danos à Indústria na Região Sudeste:")
print(correlacao_mortos_danos)

# 6. Análise de danos à indústria por tipo de desastre
danos_por_tipo_desastre = df_sudeste.groupby('grupo_de_desastre')['PEPR_Indústria (R$)'].sum()
print("\nDanos à Indústria por Tipo de Desastre na Região Sudeste:")
print(danos_por_tipo_desastre)

# 7. Relação entre número de desabrigados e danos à indústria
df_sudeste['DH_DESABRIGADOS'] = pd.to_numeric(df_sudeste['DH_DESABRIGADOS'], errors='coerce')
correlacao_desabrigados_danos = df_sudeste[['DH_DESABRIGADOS', 'PEPR_Indústria (R$)']].corr()
print("\nCorrelação entre Número de Desabrigados e Danos à Indústria na Região Sudeste:")
print(correlacao_desabrigados_danos)

# 8. Danos à indústria por município ao longo dos anos
danos_por_municipio_ano = df_sudeste.groupby(['Nome_Municipio', 'Ano'])['PEPR_Indústria (R$)'].sum().unstack()
print("\nDanos à Indústria por Município ao Longo dos Anos:")
print(danos_por_municipio_ano)

# 9. Análise de outliers nos danos à indústria
q1 = df_sudeste['PEPR_Indústria (R$)'].quantile(0.25)
q3 = df_sudeste['PEPR_Indústria (R$)'].quantile(0.75)
iqr = q3 - q1
outliers = df_sudeste[(df_sudeste['PEPR_Indústria (R$)'] < (q1 - 1.5 * iqr)) | (df_sudeste['PEPR_Indústria (R$)'] > (q3 + 1.5 * iqr))]
print("\nOutliers de Danos à Indústria na Região Sudeste:")
print(outliers)

# 10. Comparação entre danos à indústria e outros setores
df_sudeste['PEPR_total_privado'] = pd.to_numeric(df_sudeste['PEPR_total_privado'], errors='coerce')
df_sudeste['PEPL_total_publico'] = pd.to_numeric(df_sudeste['PEPL_total_publico'], errors='coerce')

comparacao_setores = df_sudeste[['PEPR_Indústria (R$)', 'PEPR_total_privado', 'PEPL_total_publico']].sum()
print("\nComparação de Danos por Setor na Região Sudeste:")
print(comparacao_setores)