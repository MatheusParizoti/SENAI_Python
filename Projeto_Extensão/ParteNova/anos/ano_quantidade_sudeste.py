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

# Criar coluna 'Região'
def obter_regiao(uf):
    for regiao, ufs in regioes.items():
        if uf in ufs:
            return regiao
    return 'Desconhecida'

df['Região'] = df['Sigla_UF'].apply(obter_regiao)

# Garantir que os valores de "PEPR_Indústria (R$)" sejam numéricos
df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# Preencher NaN com zero
df['PEPR_Indústria (R$)'].fillna(0, inplace=True)

# Converter a coluna 'Data_Evento' para datetime
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# Extrair o ano
df['Ano'] = df['Data_Evento'].dt.year

# Filtrar para Sudeste e anos entre 2000 e 2023
df_sudeste = df[df['Região'] == 'Sudeste']
df_sudeste_ano_range = df_sudeste[(df_sudeste['Ano'] >= 2000) & (df_sudeste['Ano'] <= 2023)]

# === GRÁFICO DOS 3 ESTADOS COM MAIS DESASTRES ===
desastres_estado_ano = df_sudeste_ano_range.groupby(['Sigla_UF', 'Ano']).size().reset_index(name='Numero_de_Desastres')
desastres_estado_ano_total = desastres_estado_ano.groupby('Sigla_UF')['Numero_de_Desastres'].sum()
desastres_estado_ano_ordenado = desastres_estado_ano_total.sort_values(ascending=False)
top_3_ufs = desastres_estado_ano_ordenado.head(3).index

plt.figure(figsize=(15, 10))
for i, uf in enumerate(top_3_ufs, 1):
    df_uf = desastres_estado_ano[desastres_estado_ano['Sigla_UF'] == uf]
    desastres_ano_uf = df_uf.groupby('Ano')['Numero_de_Desastres'].sum()
    plt.subplot(3, 1, i)
    sns.lineplot(x=desastres_ano_uf.index, y=desastres_ano_uf.values, marker='o')
    plt.title(f'Número de Desastres em {uf} por Ano (2000-2023)', fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Número de Desastres', fontsize=12)
    plt.grid(True)
    for year, value in zip(desastres_ano_uf.index, desastres_ano_uf.values):
        plt.text(year, value, f'{value}', fontsize=9, ha='left', va='bottom')

plt.tight_layout()
plt.show()

# === TIPOLOGIA MAIS FREQUENTE POR ANO ===
# Garantir que a coluna seja texto
df_sudeste_ano_range['descricao_tipologia'] = df_sudeste_ano_range['descricao_tipologia'].astype(str)

# Obter a tipologia mais frequente por ano + contagem
tipologia_contagem = (
    df_sudeste_ano_range
    .groupby(['Ano', 'descricao_tipologia'])
    .size()
    .reset_index(name='Contagem')
    .sort_values(['Ano', 'Contagem'], ascending=[True, False])
    .drop_duplicates(subset='Ano')
)

# Mostrar os resultados
print("\nTipologia mais frequente por ano:")
print(tipologia_contagem)

# === GRÁFICO COM TIPOLOGIA DOMINANTE POR ANO ===
plt.figure(figsize=(15, 6))
sns.barplot(data=tipologia_contagem, x='Ano', y='Contagem', hue='descricao_tipologia', dodge=False)
plt.title('Tipologia Mais Frequente por Ano na Região Sudeste (2000-2023)')
plt.xlabel('Ano')
plt.ylabel('Número de Ocorrências')
plt.legend(title='Tipologia', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# === FILTRAR DESASTRES RELACIONADOS A "CHUVAS INTENSAS" NOS ANOS DE 2020-2023 ===
# Filtrar os dados para os anos de 2021 a 2023 e para 'chuvas intensas'
df_2021_2023 = df_sudeste_ano_range[(df_sudeste_ano_range['Ano'] >= 2020) & (df_sudeste_ano_range['Ano'] <= 2023)]

# Filtrar os desastres de 'chuvas intensas' (ajustar conforme o nome exato na sua base)
df_chuvas_intensas = df_2021_2023[df_2021_2023['descricao_tipologia'].str.contains('chuvas intensas', case=False, na=False)]

# Agrupar por estado (UF) e contar o número de desastres por estado
desastres_chuvas_intensas_estado = df_chuvas_intensas.groupby('Sigla_UF').size().reset_index(name='Numero_de_Chuvas_Intensas')

# Ordenar os estados pela quantidade de desastres
desastres_chuvas_intensas_estado_ordenado = desastres_chuvas_intensas_estado.sort_values(by='Numero_de_Chuvas_Intensas', ascending=False)

# Criar gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(data=desastres_chuvas_intensas_estado_ordenado, x='Sigla_UF', y='Numero_de_Chuvas_Intensas', palette='Blues_d')

# Adicionar título e rótulos
plt.title('Distribuição de Desastres Relacionados a Chuvas Intensas (2020-2023)', fontsize=16)
plt.xlabel('Estado (UF)', fontsize=12)
plt.ylabel('Número de Desastres de Chuvas Intensas', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
