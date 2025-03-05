import pandas as pd


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

# Agrupar por Estado dentro da Região Sudeste
industria_estado_sudeste = df_sudeste.groupby('Sigla_UF')['PEPR_Indústria (R$)'].sum()

# Ordenar os estados da Região Sudeste do maior para o menor
industria_estado_sudeste_ordenado = industria_estado_sudeste.sort_values(ascending=False)

print("\nDanos à Indústria por Estado na Região Sudeste (ordem do maior para o menor):")
print(industria_estado_sudeste_ordenado)

# Agrupar os dados por 'Nome_Municipio' dentro da Região Sudeste
industria_municipio_sudeste = df_sudeste.groupby('Nome_Municipio')['PEPR_Indústria (R$)'].sum()

# Ordenar os municípios da Região Sudeste do maior para o menor
industria_municipio_sudeste_ordenado = industria_municipio_sudeste.sort_values(ascending=False)

print("\nDanos à Indústria por Município na Região Sudeste (ordem do maior para o menor):")
print(industria_municipio_sudeste_ordenado)

