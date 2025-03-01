import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_excel("df_reduzido.xlsx")
    print(df.head())  # Para imprimir as primeiras linhas do DataFrame
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# # Estatísticas descritivas para a coluna de impacto na indústria
# industria_stats = df['PEPR_Indústria (R$)'].describe()
# print(industria_stats)

# plt.figure(figsize=(10, 6))
# sns.histplot(df['PEPR_Indústria (R$)'], kde=True, color='blue')
# plt.title('Distribuição dos Danos à Indústria (em R$)')
# plt.xlabel('Danos à Indústria (R$)')
# plt.ylabel('Frequência')
# plt.show()


# # Converter a coluna Data_Evento para datetime, caso necessário
# df['Data_Evento'] = pd.to_datetime(df['Data_Evento'], errors='coerce')

# # Agregar dados por ano
# df['Ano'] = df['Data_Evento'].dt.year
# industria_ano = df.groupby('Ano')['PEPR_Indústria (R$)'].sum()

# plt.figure(figsize=(10, 6))
# sns.lineplot(x=industria_ano.index, y=industria_ano.values, marker='o', color='green')
# plt.title('Evolução dos Danos à Indústria ao Longo dos Anos')
# plt.xlabel('Ano')
# plt.ylabel('Danos à Indústria (R$)')
# plt.show()

# # Agrupar por tipo de desastre e calcular a soma dos danos à indústria
# industria_tipologia = df.groupby('descricao_tipologia')['PEPR_Indústria (R$)'].sum().sort_values(ascending=False)

# plt.figure(figsize=(10, 6))
# sns.barplot(x=industria_tipologia.index, y=industria_tipologia.values, palette='viridis')
# plt.title('Danos à Indústria por Tipo de Desastre')
# plt.xlabel('Tipo de Desastre')
# plt.ylabel('Danos à Indústria (R$)')
# plt.xticks(rotation=90)
# plt.show()

# Agrupar por UF para visualizar os danos por estado
industria_uf = df.groupby('Sigla_UF')['PEPR_Indústria (R$)'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=industria_uf.index, y=industria_uf.values, palette='coolwarm')
plt.title('Danos à Indústria por Estado')
plt.xlabel('Estado (UF)')
plt.ylabel('Danos à Indústria (R$)')
plt.xticks(rotation=90)
plt.show()