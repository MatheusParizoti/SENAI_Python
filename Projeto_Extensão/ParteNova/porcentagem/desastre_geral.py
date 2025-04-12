import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("df_reduzido.xlsx")

# Limpar os valores da coluna 'PEPR_Indústria (R$)', removendo caracteres de moeda e espaços
df['grupo_de_desastre'] = df['grupo_de_desastre'].replace({'R\$': '', ',': '', ' ': ''}, regex=True)

# Verificar os valores não nulos na coluna 'grupo_de_desastre'
grupo_valores = df['grupo_de_desastre'].dropna()

# Contar a frequência absoluta de cada grupo
frequencia_absoluta = grupo_valores.value_counts()

# Calcular a frequência relativa (porcentagem)
frequencia_relativa = (frequencia_absoluta / grupo_valores.shape[0]) * 100

# Juntar em um DataFrame
df_grupos = pd.DataFrame({
    'Grupo': frequencia_absoluta.index,
    'Quantidade': frequencia_absoluta.values,
    'Porcentagem': frequencia_relativa.values
})

# Ordenar por quantidade (opcional)
df_grupos = df_grupos.sort_values(by='Quantidade', ascending=False)

# Exibir todos os grupos com quantidade e porcentagem
print("\nTodos os grupos de desastre com suas quantidades e porcentagens:")
print(df_grupos.to_string(index=False, formatters={'Porcentagem': '{:.2f}%'.format}))