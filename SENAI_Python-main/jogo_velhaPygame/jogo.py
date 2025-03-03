import pygame as pg

pg.init()

# Configuração da tela
tela = pg.display.set_mode((600, 600), 0, 32)
pg.display.set_caption('Jogo Da Velha')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Função para desenhar o tabuleiro
def desenhar_tabu():
    # Linhas horizontais
    pg.draw.line(tela, BRANCO, (0, 200), (600, 200), 10)
    pg.draw.line(tela, BRANCO, (0, 400), (600, 400), 10)
    # Linhas verticais
    pg.draw.line(tela, BRANCO, (200, 0), (200, 600), 10)
    pg.draw.line(tela, BRANCO, (400, 0), (400, 600), 10)

# Função para desenhar X e O
def desenhar_jogada(jogadas):
    font = pg.font.Font(None, 150)
    for i in range(3):
        for j in range(3):
            if jogadas[i][j] == 'X':
                texto = font.render('X', True, AZUL)
                tela.blit(texto, (j * 200 + 50, i * 200 + 50))
            elif jogadas[i][j] == 'O':
                texto = font.render('O', True, VERMELHO)
                tela.blit(texto, (j * 200 + 50, i * 200 + 50))

# Função para verificar se alguém ganhou
def verificar_vitoria(jogadas):
    for i in range(3):
        # Verificar linhas e colunas
        if jogadas[i][0] == jogadas[i][1] == jogadas[i][2] and jogadas[i][0] != '':
            return jogadas[i][0]
        if jogadas[0][i] == jogadas[1][i] == jogadas[2][i] and jogadas[0][i] != '':
            return jogadas[0][i]
    # Verificar diagonais
    if jogadas[0][0] == jogadas[1][1] == jogadas[2][2] and jogadas[0][0] != '':
        return jogadas[0][0]
    if jogadas[0][2] == jogadas[1][1] == jogadas[2][0] and jogadas[0][2] != '':
        return jogadas[0][2]
    return None

# Função para verificar empate
def verificar_empate(jogadas):
    for i in range(3):
        for j in range(3):
            if jogadas[i][j] == '':
                return False
    return True

# Função para exibir a imagem do vencedor
def exibir_imagem_vencedor(vencedor):
    if vencedor == 'X':
        img = pg.image.load('win.webp')
    elif vencedor == 'O':
        img = pg.image.load('win.webp')
    else:
        img = pg.image.load('empate.jpg')
    img = pg.transform.scale(img, (600, 600))  # Ajuste para preencher toda a tela
    tela.blit(img, (0, 0))
    pg.display.update()

# Inicialização das variáveis
jogadas = [['' for _ in range(3)] for _ in range(3)]
estado = 'JOGANDO'
vez = 'JOGADOR1'
escolha = 'X'

# Loop principal
while True:
    tela.fill(PRETO)
    desenhar_tabu()
    desenhar_jogada(jogadas)

    # Verifica se alguém venceu
    vencedor = verificar_vitoria(jogadas)
    if vencedor:
        exibir_imagem_vencedor(vencedor)
        pg.time.delay(2000)  # Espera 2 segundos antes de fechar
        pg.quit()
        exit()
    elif verificar_empate(jogadas):
        exibir_imagem_vencedor('Empate')
        pg.time.delay(2000)  # Espera 2 segundos antes de fechar
        pg.quit()
        exit()

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
        
        if evento.type == pg.MOUSEBUTTONDOWN and estado == 'JOGANDO':
            x, y = evento.pos
            linha = y // 200
            coluna = x // 200
            if jogadas[linha][coluna] == '':
                jogadas[linha][coluna] = escolha
                if vez == 'JOGADOR1':
                    escolha = 'O'
                    vez = 'JOGADOR2'
                else:
                    escolha = 'X'
                    vez = 'JOGADOR1'

    pg.display.update()
