import pandas as pd

# Caminho do arquivo Excel
arquivo = 'mass.xlsx'

# Lê o arquivo Excel (por padrão lê a primeira planilha)
df = pd.read_excel(arquivo)

# Mostra o número de colunas
print(f"Número de colunas: {len(df.columns)}")

# Mostra os nomes das colunas
print("Colunas:")
print(df.columns.tolist())
