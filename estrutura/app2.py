import pandas as pd
import hashlib

class Registro:
    def __init__(self, chave1, chave2, dados):
        self.chave1 = str(chave1)
        self.chave2 = str(chave2)
        self.dados = [dados]  # lista de dicionários
        self.dados_set = {self._dict_to_tuple(dados)}  # conjunto para checar duplicados
    
    def _dict_to_tuple(self, d):
        # Converte dict para uma tupla de pares ordenados para usar em set (deduplicação)
        return tuple(sorted(d.items()))
    
    def adicionar_dados(self, dados):
        dados_tuple = self._dict_to_tuple(dados)
        if dados_tuple not in self.dados_set:
            self.dados.append(dados)
            self.dados_set.add(dados_tuple)
            return True  # adicionou
        return False  # já existia
    
    def __repr__(self):
        return f"Registro({self.chave1}, {self.chave2}, {len(self.dados)} registros)"


class TabelaHash:
    def __init__(self, tamanho=1000):
        self.tabela = [[] for _ in range(tamanho)]
        self.tamanho = tamanho
        self.indice = {}  # dicionário para indexar registros pela chave (chave1, chave2)

    def funcao_hash(self, chave1, chave2):
        chave = f"{str(chave1)}|{str(chave2)}"
        hash_obj = hashlib.sha256(chave.encode())
        hash_hex = hash_obj.hexdigest()
        hash_int = int(hash_hex, 16)
        return hash_int % self.tamanho

    def inserir(self, chave1, chave2, dados):
        chave1 = str(chave1)
        chave2 = str(chave2)
        chave_composta = (chave1, chave2)

        # Verifica se já existe o registro no índice
        if chave_composta in self.indice:
            registro = self.indice[chave_composta]
            if registro.adicionar_dados(dados):
                print(f"🔄 Dados adicionados ao registro existente no índice da tabela hash")
            else:
                print(f"⚠️ Dados duplicados ignorados no índice da tabela hash")
            return

        # Se não existir, cria novo registro e insere no bucket e índice
        indice = self.funcao_hash(chave1, chave2)
        registro = Registro(chave1, chave2, dados)
        self.tabela[indice].append(registro)
        self.indice[chave_composta] = registro
        print(f"✅ Novo registro inserido no índice {indice}")

    def buscar(self, chave1, chave2):
        chave_composta = (str(chave1), str(chave2))
        return self.indice.get(chave_composta, None)

    def mostrar_tabela(self):
        print("\n📊 Estado atual da Tabela Hash:")
        for i, bucket in enumerate(self.tabela):
            print(f"Índice {i}: {bucket}")


# --- Uso com pandas ---

arquivo = 'mass.xlsx'
df = pd.read_excel(arquivo)

tabela_hash = TabelaHash(tamanho=1000)

chave1_coluna = 'Cumulative case rate'
chave2_coluna = 'Cases during this week'

for idx, row in df.iterrows():
    chave1 = row[chave1_coluna]
    chave2 = row[chave2_coluna]
    dados = row.to_dict()
    tabela_hash.inserir(chave1, chave2, dados)

# Mostrar tabela completa (pode comentar depois)
tabela_hash.mostrar_tabela()

# Interface para ver registros por índice
while True:
    try:
        indice_escolhido = int(input("\nDigite um índice de 0 a 999 para ver os registros daquele bucket (ou -1 para sair): "))
        if indice_escolhido == -1:
            print("Saindo...")
            break
        if 0 <= indice_escolhido < tabela_hash.tamanho:
            bucket = tabela_hash.tabela[indice_escolhido]
            if not bucket:
                print(f"Índice {indice_escolhido} está vazio.")
            else:
                print(f"\nRegistros no índice {indice_escolhido}:")
                for registro in bucket:
                    print(registro)
                    for i, registro_dados in enumerate(registro.dados, 1):
                        print(f"  Registro #{i}:")
                        for chave, valor in registro_dados.items():
                            print(f"    {chave}: {valor}")
        else:
            print("Índice fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro válido.")
