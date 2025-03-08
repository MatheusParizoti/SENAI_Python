import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_total_privado', removendo caracteres de moeda e espaços
df['PEPR_total_privado'] = df['PEPR_total_privado'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_total_privado' para numérico, forçando erros para NaN
df['PEPR_total_privado'] = pd.to_numeric(df['PEPR_total_privado'], errors='coerce')

# Certificar-se de que a coluna 'Data_Evento' é do tipo datetime
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# Extrair o ano da coluna 'Data_Evento'
df['Ano'] = df['Data_Evento'].dt.year

# Filtrar os dados pelas siglas de interesse
siglas_interesse = ['SP', 'RJ', 'MG', 'ES']
df_filtrado = df[df['Sigla_UF'].isin(siglas_interesse)]

# Filtrar para mostrar apenas valores maiores que zero
df_maiores_que_zero = df_filtrado[df_filtrado['PEPR_total_privado'] > 0]

# Agrupar os dados por sigla, valor, nome do município e ano, contando quantas vezes cada valor aparece
resultados = df_maiores_que_zero.groupby(['Sigla_UF', 'PEPR_total_privado', 'Nome_Municipio', 'Ano']).size().reset_index(name='Contagem')

# Ordenar os resultados por sigla e valor em ordem decrescente
resultados_sorted = resultados.sort_values(by=['Sigla_UF', 'PEPR_total_privado'], ascending=[True, False])

# Para cada sigla, pegar os 10 maiores valores
top_10_por_sigla = resultados_sorted.groupby('Sigla_UF').head(10)

# Exibir os resultados com linha em branco antes e depois de cada sigla
last_sigla = None

# Adicionar uma linha em branco antes de cada sigla
for index, row in top_10_por_sigla.iterrows():
    sigla = row['Sigla_UF']
    
    # Adicionar linha em branco antes da sigla se a sigla for diferente da última
    if sigla != last_sigla:
        if last_sigla is not None:
            print()  # Linha em branco após a última sigla
        print()  # Linha em branco antes da nova sigla
        print(f"Sigla: {sigla}")
        last_sigla = sigla
    
    # Imprimir os dados da linha
    print(f"  Valor: {row['PEPR_total_privado']} - Município: {row['Nome_Municipio']} - Ano: {row['Ano']} - Contagem: {row['Contagem']}")