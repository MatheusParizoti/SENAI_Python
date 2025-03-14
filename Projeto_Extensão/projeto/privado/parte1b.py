import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Supondo que a base de dados seja chamada df
df = pd.read_excel("df_reduzido.xlsx")
# 1. Filtrar os dados para as siglas de interesse
siglas_sudeste = ['SP', 'MG', 'RJ', 'ES']
df_sudeste = df[df['Sigla_UF'].isin(siglas_sudeste)]

# 2. Criar uma coluna "Sudeste"
df_sudeste['Sudeste'] = df_sudeste['Sigla_UF'].apply(lambda x: 'Sudeste')

# 3. Converter a coluna Data_Evento para datetime e extrair o ano
df_sudeste['Data_Evento'] = pd.to_datetime(df_sudeste['Data_Evento'], errors='coerce')
df_sudeste['Ano'] = df_sudeste['Data_Evento'].dt.year

# 4. Agrupar por Ano e Sudeste e calcular a soma do PEPR_Indústria
df_ano_sudeste = df_sudeste.groupby(['Ano', 'Sudeste'])['PEPR_total_privado'].sum().reset_index()

# 5. Arredondar os valores de PEPR_total_privado para 7 casas decimais
df_ano_sudeste['PEPR_total_privado'] = df_ano_sudeste['PEPR_total_privado'].round(7)

# 6. Plotar o gráfico exponencial (logaritmo de PEPR_Indústria)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_ano_sudeste, x='Ano', y='PEPR_total_privado', hue='Sudeste', marker='o')

# Ajuste no gráfico para visualização melhor
plt.title('Evolução Exponencial da Indústria no Sudeste (SP, MG, RJ, ES)', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('PEPR da Indústria (R$)', fontsize=12)
plt.legend(title='Região', loc='upper left')

plt.grid(True)
plt.show()
