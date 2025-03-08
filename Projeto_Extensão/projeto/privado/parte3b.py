import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_total_privado', removendo caracteres de moeda e espaços
df['PEPR_total_privado'] = df['PEPR_total_privado'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_total_privado' para numérico, forçando erros para NaN
df['PEPR_total_privado'] = pd.to_numeric(df['PEPR_total_privado'], errors='coerce')

# Garantir que 'Data_Evento' seja do tipo datetime
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# Filtrar os dados pelas siglas de interesse
siglas_interesse = ['SP', 'RJ', 'MG', 'ES']
df_filtrado = df[df['Sigla_UF'].isin(siglas_interesse)]

# Filtrar os dados para considerar apenas valores positivos de 'PEPR_total_privado'
df_positivos = df_filtrado[df_filtrado['PEPR_total_privado'] > 0]

# Extrair o ano da coluna 'Data_Evento'
df_positivos['Ano'] = df_positivos['Data_Evento'].dt.year

# Agrupar por 'Sigla_UF', 'descricao_tipologia', e 'Ano' e contar as ocorrências
contagem_tipologia_por_ano_estado = df_positivos.groupby(['Sigla_UF', 'descricao_tipologia', 'Ano']).size().reset_index(name='Quantidade')

# Calcular o total de ocorrências por ano e sigla
total_por_ano_estado = contagem_tipologia_por_ano_estado.groupby(['Sigla_UF', 'Ano'])['Quantidade'].transform('sum')

# Calcular a porcentagem de cada tipologia dentro de cada ano e sigla
contagem_tipologia_por_ano_estado['Porcentagem'] = (contagem_tipologia_por_ano_estado['Quantidade'] / total_por_ano_estado) * 100

# Agora vamos criar o gráfico de pizza
for sigla, grupo_sigla in contagem_tipologia_por_ano_estado.groupby('Sigla_UF'):
    plt.figure(figsize=(8, 8))  # Ajuste o tamanho da figura
    for ano, grupo_ano in grupo_sigla.groupby('Ano'):
        # Excluir a coluna 'Ano' para o gráfico de pizza
        tipologia = grupo_ano['descricao_tipologia']
        quantidade = grupo_ano['Quantidade']

        # Plotar o gráfico de pizza para o ano atual e sigla
        plt.pie(quantidade, labels=tipologia, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(tipologia)))
        
        plt.title(f"Distribuição de Tipologias - Sigla {sigla} - Ano {ano}")
        plt.axis('equal')  # Garantir que o gráfico de pizza seja circular
        plt.legend(tipologia, title="Tipologia", loc="upper left", bbox_to_anchor=(1, 1))  # Adicionar legenda
        plt.show()  # Exibir o gráfico

