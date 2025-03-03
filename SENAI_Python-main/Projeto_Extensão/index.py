import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_excel("df_reduzido.xlsx")
    print(df.head())  # Para imprimir as primeiras linhas do DataFrame
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Definindo as regiões do Brasil com as siglas dos estados
sudeste = ['SP', 'RJ', 'MG', 'ES']
sul = ['PR', 'SC', 'RS']
norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'MA']
nordeste = ['BA', 'CE', 'SE', 'AL', 'PE', 'PB', 'RN', 'PI', 'MA', 'GO']
centro_oeste = ['MT', 'MS', 'DF']

# Criando uma coluna de região no DataFrame com base na sigla do estado
def definir_regiao(sigla):
    if sigla in sudeste:
        return 'Sudeste'
    elif sigla in sul:
        return 'Sul'
    elif sigla in norte:
        return 'Norte'
    elif sigla in nordeste:
        return 'Nordeste'
    elif sigla in centro_oeste:
        return 'Centro-Oeste'


df['Regiao'] = df['Sigla_UF'].apply(definir_regiao)

# Função para criar gráfico de barras das 5 maiores 'descricao_tipologia' por região
def plotar_top_5_tipologia_por_regiao(regiao):
    # Filtrando os dados para a região específica
    df_regiao = df[df['Regiao'] == regiao]

    # Verificando se há dados na região
    if df_regiao.empty:
        print(f"Não há dados para a região {regiao}")
        return

    # Contagem das tipologias por grupo de desastre
    tipologia_por_desastre = df_regiao.groupby('descricao_tipologia').size().reset_index(name='contagem')

    # Ordenando pela contagem em ordem decrescente e pegando as 5 maiores
    top_5_tipologias = tipologia_por_desastre.sort_values(by='contagem', ascending=False).head(5)

    # Criando o gráfico de barras
    plt.figure(figsize=(10, 6))

    sns.barplot(data=top_5_tipologias, x='descricao_tipologia', y='contagem', palette='viridis')

    # Adicionando título e rótulos
    plt.title(f'Top 5 Tipologias de Desastre mais Frequentes na Região {regiao}', fontsize=16)
    plt.xlabel('Tipologia de Desastre', fontsize=14)
    plt.ylabel('Número de Ocorrências', fontsize=14)

    # Ajustando a rotação dos rótulos
    plt.xticks(rotation=45, ha='right')

    # Exibindo o gráfico
    plt.tight_layout()
    plt.show()

# Criar gráficos para cada região
for regiao in ['Sudeste', 'Sul', 'Norte', 'Nordeste', 'Centro-Oeste']:
    plotar_top_5_tipologia_por_regiao(regiao)
