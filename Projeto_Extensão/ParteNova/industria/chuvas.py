import pandas as pd

# Carregar os dados
try:
    df = pd.read_excel("df_reduzido.xlsx")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Limpar os valores da coluna 'PEPR_Indústria (R$)', removendo caracteres de moeda e espaços
df['PEPR_Indústria (R$)'] = df['PEPR_Indústria (R$)'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_Indústria (R$)' para tipo numérico
df['PEPR_Indústria (R$)'] = pd.to_numeric(df['PEPR_Indústria (R$)'], errors='coerce')

# Garantir que a coluna 'Data_Evento' está no formato de data
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# Filtrar as linhas que contêm 'Chuvas Intensas' na coluna 'descricao_tipologia'
chuvas_intensas = df[df['descricao_tipologia'].str.contains('Chuvas Intensas', case=False, na=False)]

# Filtrar os casos onde 'PEPR_Indústria (R$)' > 0
chuvas_intensas_com_valor = chuvas_intensas[chuvas_intensas['PEPR_Indústria (R$)'] > 0]

# Filtrar as linhas para os anos de 2020 a 2023
chuvas_intensas_com_valor_anos = chuvas_intensas_com_valor[
    chuvas_intensas_com_valor['Data_Evento'].dt.year.between(2020, 2023)
]

# Filtrar os casos para os estados SP, RJ, MG, ES
estados_filtro = ['SP', 'RJ', 'MG', 'ES']
chuvas_intensas_estado = chuvas_intensas_com_valor_anos[chuvas_intensas_com_valor_anos['Sigla_UF'].isin(estados_filtro)]

# Contar a quantidade de casos por estado
quantidade_casos_por_estado = chuvas_intensas_estado.groupby('Sigla_UF').size()

# Exibir os resultados
print("Quantidade de casos de 'Chuvas Intensas' com 'PEPR_Indústria (R$)' > 0 entre 2020 e 2023 nos estados SP, RJ, MG, ES:")
print(quantidade_casos_por_estado)
