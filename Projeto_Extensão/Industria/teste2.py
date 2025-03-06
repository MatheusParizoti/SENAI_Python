import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_Indústria (R$)', removendo caracteres de moeda e espaços
df['PEPR_Indústria (R$)'] = df['PEPR_Indústria (R$)'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_Indústria (R$)' para numérico, forçando erros para NaN
df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# Filtrar os dados pelas siglas de interesse
siglas_interesse = ['SP', 'RJ', 'MG', 'ES']
df_filtrado = df[df['Sigla_UF'].isin(siglas_interesse)]

# Contar os valores não nulos
num_nao_nulos = df_filtrado['PEPR_Indústria (R$)'].notna().sum()

# Filtrar para mostrar apenas valores maiores que zero
df_maiores_que_zero = df_filtrado[df_filtrado['PEPR_Indústria (R$)'] > 0]

# Contar os valores positivos por sigla
contagem_positivos_por_sigla = df_maiores_que_zero.groupby('Sigla_UF').size()

# Exibir os resultados
print("")
print(f"Valores não nulos: {num_nao_nulos}")
print(f"Valores positivos: {len(df_maiores_que_zero)}")

print("\nContagem de valores positivos para cada sigla:")
# Imprimir sigla e quantidade de valores positivos
for sigla, quantidade in contagem_positivos_por_sigla.items():
    print(f"Sigla {sigla}: {quantidade}")


# Filtrar os dados para considerar apenas valores positivos de 'PEPR_Indústria (R$)'
df_positivos = df_filtrado[df_filtrado['PEPR_Indústria (R$)'] > 0]

# Agrupar por 'Sigla_UF' e 'descricao_tipologia' e contar as ocorrências, mas apenas para os valores positivos
contagem_tipologia_por_estado = df_positivos.groupby(['Sigla_UF', 'descricao_tipologia']).size().reset_index(name='Quantidade')

# Exibir os resultados
print("\nContagem de Tipologias Positivas por Estado:")
for sigla, grupo in contagem_tipologia_por_estado.groupby('Sigla_UF'):
    print(f"\nSigla {sigla}:")
    for _, row in grupo.iterrows():
        print(f"  Tipologia: {row['descricao_tipologia']} - Quantidade: {row['Quantidade']}")

# Filtrar os dados para considerar apenas valores positivos de 'PEPR_Indústria (R$)'
df_positivos = df_filtrado[df_filtrado['PEPR_Indústria (R$)'] > 0]

# Agrupar por 'Sigla_UF' e 'descricao_tipologia' e contar as ocorrências, mas apenas para os valores positivos
contagem_tipologia_por_estado = df_positivos.groupby(['Sigla_UF', 'descricao_tipologia']).size().reset_index(name='Quantidade')

# Calcular o total de valores positivos por estado
total_por_estado = df_positivos.groupby('Sigla_UF').size()

# Calcular a porcentagem de cada tipologia dentro do estado
contagem_tipologia_por_estado['Porcentagem'] = contagem_tipologia_por_estado.apply(
    lambda row: (row['Quantidade'] / total_por_estado[row['Sigla_UF']]) * 100, axis=1)

# Exibir os resultados
print("\nContagem de Tipologias Positivas por Estado (em porcentagem):")
for sigla, grupo in contagem_tipologia_por_estado.groupby('Sigla_UF'):
    print(f"\nSigla {sigla}:")
    for _, row in grupo.iterrows():
        print(f"  Tipologia: {row['descricao_tipologia']} - Porcentagem: {row['Porcentagem']:.2f}%")
