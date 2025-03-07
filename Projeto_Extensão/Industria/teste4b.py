# # Filtrar os dados para considerar apenas valores positivos de 'PEPR_Indústria (R$)'
# df_positivos = df_filtrado[df_filtrado['PEPR_Indústria (R$)'] > 0]

# # Agrupar por 'Sigla_UF' e 'descricao_tipologia' e contar as ocorrências, mas apenas para os valores positivos
# contagem_tipologia_por_estado = df_positivos.groupby(['Sigla_UF', 'descricao_tipologia']).size().reset_index(name='Quantidade')

# # Exibir os resultados
# print("\nContagem de Tipologias Positivas por Estado:")
# for sigla, grupo in contagem_tipologia_por_estado.groupby('Sigla_UF'):
#     print(f"\nSigla {sigla}:")
#     for _, row in grupo.iterrows():
#         print(f"  Tipologia: {row['descricao_tipologia']} - Quantidade: {row['Quantidade']}")

# # Filtrar os dados para considerar apenas valores positivos de 'PEPR_Indústria (R$)'
# df_positivos = df_filtrado[df_filtrado['PEPR_Indústria (R$)'] > 0]

# # Agrupar por 'Sigla_UF' e 'descricao_tipologia' e contar as ocorrências, mas apenas para os valores positivos
# contagem_tipologia_por_estado = df_positivos.groupby(['Sigla_UF', 'descricao_tipologia']).size().reset_index(name='Quantidade')

# # Calcular o total de valores positivos por estado
# total_por_estado = df_positivos.groupby('Sigla_UF').size()
