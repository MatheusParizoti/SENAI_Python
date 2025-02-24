import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Mapeamento dos estados para suas respectivas regiões do Brasil
regioes_brasil = {
    'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Centro-Oeste': ['GO', 'MT', 'MS', 'DF'],
    'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'Sul': ['PR', 'RS', 'SC']
}

# Supondo que o DataFrame já esteja carregado em `df`
try:
    df = pd.read_excel("df_reduzido.xlsx")
    print(df.head())  # Para imprimir as primeiras linhas do DataFrame
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Verifique se a coluna 'grupo_de_desastre' existe e tem valores nulos
print(df['grupo_de_desastre'].isnull().sum())  # Verifique se há valores nulos na coluna

# Se necessário, remova ou substitua valores nulos
df = df.dropna(subset=['grupo_de_desastre', 'Sigla_UF'])

# Adicionando coluna de Região ao DataFrame com base na coluna 'Sigla_UF' (estado)
def mapear_regiao(estado):
    for regiao, estados in regioes_brasil.items():
        if estado in estados:
            return regiao
    return None

df['regiao'] = df['Sigla_UF'].apply(mapear_regiao)

# Agora vamos contar o grupo de desastre mais frequente por região
# Vamos agrupar os dados por região e grupo de desastre
grupo_frequente_regiao = df.groupby(['regiao', 'grupo_de_desastre']).size().reset_index(name='contagem')

# Para cada região, selecionamos o grupo de desastre com maior contagem
grupo_frequente_regiao = grupo_frequente_regiao.loc[grupo_frequente_regiao.groupby('regiao')['contagem'].idxmax()]

# Plotando o gráfico para mostrar o maior grupo de desastre por região
plt.figure(figsize=(10, 6))  # Definir tamanho da figura

# Gráfico de barras para mostrar o maior grupo de desastre por região
sns.barplot(data=grupo_frequente_regiao, x='regiao', y='contagem', hue='grupo_de_desastre', palette='viridis')

# Adicionando título e rótulos
plt.title('Grupo de Desastre Mais Frequente por Região do Brasil', fontsize=16)
plt.xlabel('Região', fontsize=14)
plt.ylabel('Número de Ocorrências', fontsize=14)

# Ajustando a rotação dos rótulos no eixo x para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibindo o gráfico
plt.tight_layout()
plt.show()
