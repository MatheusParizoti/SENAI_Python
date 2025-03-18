import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_Indústria (R$)', removendo caracteres de moeda e espaços
df['PEPR_Indústria (R$)'] = df['PEPR_Indústria (R$)'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_Indústria (R$)' para numérico, forçando erros para NaN
df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# Garantir que 'Data_Evento' seja do tipo datetime
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# Filtrar os dados pelas siglas de interesse
siglas_interesse = ['SP', 'RJ', 'MG', 'ES']
df_filtrado = df[df['Sigla_UF'].isin(siglas_interesse)]

# Filtrar os dados para considerar apenas valores positivos de 'PEPR_Indústria (R$)'
df_positivos = df_filtrado[df_filtrado['PEPR_Indústria (R$)'] > 0]

# Extrair o ano da coluna 'Data_Evento'
df_positivos['Ano'] = df_positivos['Data_Evento'].dt.year

# Agrupar por 'Sigla_UF', 'descricao_tipologia', e 'Ano' e contar as ocorrências
contagem_tipologia_por_ano_estado = df_positivos.groupby(['Sigla_UF', 'descricao_tipologia', 'Ano']).size().reset_index(name='Quantidade')

# Calcular o total de ocorrências por ano e sigla
total_por_ano_estado = contagem_tipologia_por_ano_estado.groupby(['Sigla_UF', 'Ano'])['Quantidade'].transform('sum')

# Calcular a porcentagem de cada tipologia dentro de cada ano e sigla
contagem_tipologia_por_ano_estado['Porcentagem'] = (contagem_tipologia_por_ano_estado['Quantidade'] / total_por_ano_estado) * 100

# Exibir os resultados
print("\nContagem de Tipologias por Ano e Estado (em porcentagem):")
for sigla, grupo_sigla in contagem_tipologia_por_ano_estado.groupby('Sigla_UF'):
    print(f"\nSigla {sigla}:")
    for ano, grupo_ano in grupo_sigla.groupby('Ano'):
        print(f"  Ano {ano}:")
        for _, row in grupo_ano.iterrows():
            print(f"    Tipologia: {row['descricao_tipologia']} - Quantidade: {row['Quantidade']} - Porcentagem: {row['Porcentagem']:.2f}%")