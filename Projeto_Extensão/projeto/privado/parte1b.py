import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_total_privado', removendo caracteres de moeda e espaços
df['PEPR_total_privado'] = df['PEPR_total_privado'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Converter a coluna 'PEPR_total_privado' para numérico, forçando erros para NaN
df['PEPR_total_privado'] = pd.to_numeric(df['PEPR_total_privado'], errors='coerce')

# Filtrar os dados pelas siglas de interesse
siglas_interesse = ['SP', 'RJ', 'MG', 'ES']
df_filtrado = df[df['Sigla_UF'].isin(siglas_interesse)]

# Definir as 4 alas para cada sigla (sem associar cidades)
# Agora, todas as siglas têm as 4 alas, mas sem associar municípios específicos
regioes = {
    'SP': ['Ala_Norte', 'Ala_Sul', 'Ala_Leste', 'Ala_Oeste'],
    'RJ': ['Ala_Norte', 'Ala_Sul', 'Ala_Leste', 'Ala_Oeste'],
    'MG': ['Ala_Norte', 'Ala_Sul', 'Ala_Leste', 'Ala_Oeste'],
    'ES': ['Ala_Norte', 'Ala_Sul', 'Ala_Leste', 'Ala_Oeste']
}

# Função para atribuir a ala para cada município, apenas com base na sigla
def atribuir_ala(sigla):
    # A função agora retorna uma aleatória ou fixa entre as 4 alas, já que não estamos usando cidades específicas
    if sigla == 'SP':
        return 'Ala_Norte'  # Você pode ajustar com a lógica que preferir (ex: escolher aleatoriamente, ou uma lógica fixa)
    elif sigla == 'RJ':
        return 'Ala_Leste'
    elif sigla == 'MG':
        return 'Ala_Sul'
    elif sigla == 'ES':
        return 'Ala_Oeste'
    else:
        return 'Desconhecido'

# Adicionar a coluna 'Ala' com a região correspondente
df_filtrado['Ala'] = df_filtrado['Sigla_UF'].apply(atribuir_ala)

# Filtrar para mostrar apenas valores maiores que zero
df_maiores_que_zero = df_filtrado[df_filtrado['PEPR_total_privado'] > 0]

# Contar os valores positivos por sigla e ala
contagem_positivos_por_ala = df_maiores_que_zero.groupby(['Sigla_UF', 'Ala']).size().unstack(fill_value=0)

# Exibir os resultados
print("\nContagem de valores positivos por sigla e ala:")
print(contagem_positivos_por_ala)