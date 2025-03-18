import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Agrupar os dados por sigla, valor, nome do município e ano
resultados = df_maiores_que_zero.groupby(['Sigla_UF', 'PEPR_total_privado', 'Nome_Municipio', 'Ano']).size().reset_index(name='Contagem')

# Ordenar os resultados por sigla e valor em ordem decrescente
resultados_sorted = resultados.sort_values(by=['Sigla_UF', 'PEPR_total_privado'], ascending=[True, False])

# Para cada sigla, pegar os 10 maiores valores
top_10_por_sigla = resultados_sorted.groupby('Sigla_UF').head(10)

# Exibir os gráficos de pizza com base nas siglas
for sigla, grupo_sigla in top_10_por_sigla.groupby('Sigla_UF'):
    # Obter os valores de PEPR_total_privado e os nomes dos municípios
    valores = grupo_sigla['PEPR_total_privado']
    municipios = grupo_sigla['Nome_Municipio']
    
    # Criar o gráfico de pizza
    plt.figure(figsize=(8, 8))  # Ajustar o tamanho da figura
    plt.pie(valores, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(valores)), labels=None)
    
    # Título do gráfico
    plt.title(f"Distribuição de Valores de PEPR_total_privado - Sigla {sigla}")
    plt.axis('equal')  # Garantir que o gráfico de pizza seja circular
    
    # Adicionar a legenda com os nomes dos municípios
    plt.legend(municipios, title="Municípios", loc="upper left", bbox_to_anchor=(0.75, 0.85))  # Legenda ao lado do gráfico
    
    # Exibir o gráfico
    plt.show()  # Exibir o gráfico
