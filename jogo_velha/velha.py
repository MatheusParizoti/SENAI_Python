# Inicializando o tabuleiro
tabuleiro = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

jogador_atual = "X"

# Laço principal do jogo
for rodada in range(9):  # No máximo 9 jogadas
    # Exibindo o tabuleiro
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")
    
    # Pedir ao jogador para escolher um número de 1 a 9
    print(f"Jogador {jogador_atual}, é sua vez!")
    escolha = int(input("Escolha um número de 1 a 9: "))
    
    # Calcular linha e coluna a partir da escolha
    linha = (escolha - 1) // 3
    coluna = (escolha - 1) % 3

    # Verificar se a posição está disponível
    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Essa posição já está ocupada! Tente novamente.")
        continue
    
    # Colocar a jogada no tabuleiro
    tabuleiro[linha][coluna] = jogador_atual

    # Verificar se o jogador atual ganhou
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador_atual:
            print(f"Jogador {jogador_atual} ganhou!")
            exit()

    # Verificar colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador_atual:
            print(f"Jogador {jogador_atual} ganhou!")
            exit()

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador_atual:
        print(f"Jogador {jogador_atual} ganhou!")
        exit()
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador_atual:
        print(f"Jogador {jogador_atual} ganhou!")
        exit()

    # Trocar o jogador
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"

# Se todas as jogadas foram feitas e ninguém ganhou
print("O jogo terminou em empate!")
