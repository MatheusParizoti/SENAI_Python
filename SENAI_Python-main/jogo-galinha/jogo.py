import pygame
import random

# Inicializa o pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galinha Atravessando a Rua")

# Cores
WHITE = (255, 255, 255)
PONTUACAO_COLOR = (255, 255, 255)  # Cor para a pontuação (branca)

# Carregar imagens
galinha_img_normal = pygame.image.load('dudu.png')  # Galinha normal (padrão)
galinha_img_esquerda = pygame.image.load('duduE.png')  # Galinha virada para a esquerda
galinha_img_direita = pygame.image.load('dudu.png')  # Galinha virada para a direita
carro_img = pygame.image.load('carro1.png')  # Substitua pelo caminho correto da imagem
rua_img = pygame.image.load('onibus.jpg')  # Rua inicial
rua_img_2 = pygame.image.load('trem.webp')  # Rua para 5 pontos
rua_img_3 = pygame.image.load('rua.webp')  # Rua para 8 pontos
seta_esquerda_img = pygame.image.load('duduE.png')  # Substitua pelo caminho da seta esquerda
seta_direita_img = pygame.image.load('dudu.png')  # Substitua pelo caminho da seta direita

# Redimensionar as imagens de fundo para ocupar toda a tela
rua_img = pygame.transform.scale(rua_img, (screen_width, screen_height))
rua_img_2 = pygame.transform.scale(rua_img_2, (screen_width, screen_height))
rua_img_3 = pygame.transform.scale(rua_img_3, (screen_width, screen_height))

# Definir o novo tamanho desejado para a galinha
novo_tamanho = (70, 70)  # (largura, altura)

# Redimensionar as imagens da galinha
galinha_img_normal = pygame.transform.scale(galinha_img_normal, novo_tamanho)
galinha_img_esquerda = pygame.transform.scale(galinha_img_esquerda, novo_tamanho)
galinha_img_direita = pygame.transform.scale(galinha_img_direita, novo_tamanho)

# Dimensões da galinha redimensionada
galinha_width = galinha_img_normal.get_width()
galinha_height = galinha_img_normal.get_height()

# Dimensões do carro
carro_width = carro_img.get_width()
carro_height = carro_img.get_height()

# Definir o tamanho da área de colisão do carro (diminuindo ainda mais)
carro_colisao_width = carro_width - 20  # Reduzindo ainda mais a largura da área de colisão
carro_colisao_height = carro_height - 20  # Reduzindo ainda mais a altura da área de colisão

# Definir o relógio
clock = pygame.time.Clock()

# Função de exibir a pontuação
def exibir_pontuacao(pontos):
    font = pygame.font.SysFont(None, 55)
    texto = font.render(f"Pontos: {pontos}", True, PONTUACAO_COLOR)
    screen.blit(texto, (10, 10))

# Função principal
def jogo():
    pontos = 0
    galinha_x = screen_width // 2
    galinha_y = screen_height - galinha_height - 10
    galinha_speed = 25
    galinha_img = galinha_img_normal  # Começa com a galinha normal
    rua_img_atual = rua_img  # Começa com a imagem inicial da rua

    # Listas para armazenar carros
    carros = []
    linhas_de_carros = [100, 200, 300, 400]  # Linhas diferentes para carros

    for i in range(2):  # Diminuindo o número de carros para 2
        carro_x = random.randint(-carro_width, 0)  # Começam fora da tela à esquerda
        carro_y = random.choice(linhas_de_carros)  # Carro em linha aleatória
        direction = random.choice([-1, 1])  # Direção aleatória (1 para direita, -1 para esquerda)
        carros.append([carro_x, carro_y, direction])

    # Loop principal do jogo
    jogo_rodando = True
    while jogo_rodando:
        screen.fill(WHITE)  # Preencher a tela com a cor branca
        screen.blit(rua_img_atual, (0, 0))  # Desenha a rua de acordo com a pontuação
        screen.blit(galinha_img, (galinha_x, galinha_y))  # Desenha a galinha

        # Mover carros na horizontal
        for carro in carros:
            carro[0] += 5 * carro[2]  # Move o carro na direção escolhida
            if carro[0] < -carro_width:  # Se o carro sair pela esquerda, voltar à direita
                carro[0] = screen_width
                carro[1] = random.choice(linhas_de_carros)  # Escolhe uma nova linha para o carro
            if carro[0] > screen_width:  # Se o carro sair pela direita, voltar à esquerda
                carro[0] = -carro_width
                carro[1] = random.choice(linhas_de_carros)  # Escolhe uma nova linha para o carro

            screen.blit(carro_img, (carro[0], carro[1]))  # Desenha o carro

            # Verificar colisões (somente quando a galinha estiver na mesma linha que o carro)
            if (galinha_x + galinha_width > carro[0] and galinha_x < carro[0] + carro_width and
                galinha_y + galinha_height > carro[1] and galinha_y < carro[1] + carro_height):
                jogo_rodando = False  # Galinha perde ao colidir com um carro

        # Captura eventos (movimento da galinha)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and galinha_x > 0:
                    galinha_x -= galinha_speed
                    galinha_img = galinha_img_esquerda  # Troca para a imagem da galinha virada para a esquerda
                if evento.key == pygame.K_RIGHT and galinha_x < screen_width - galinha_width:
                    galinha_x += galinha_speed
                    galinha_img = galinha_img_direita  # Troca para a imagem da galinha virada para a direita
                if evento.key == pygame.K_UP and galinha_y > 0:
                    galinha_y -= galinha_speed
                if evento.key == pygame.K_DOWN and galinha_y < screen_height - galinha_height:
                    galinha_y += galinha_speed

        # Atualizar a pontuação
        if galinha_y <= 0:
            pontos += 1
            galinha_y = screen_height - galinha_height - 10  # Resetar a posição da galinha
            if pontos == 5:
                rua_img_atual = rua_img_2  # Muda para a rua 2 quando chegar a 5 pontos
            if pontos == 8:
                rua_img_atual = rua_img_3  # Muda para a rua 3 quando chegar a 8 pontos
            if pontos == 10:
                jogo_rodando = False  # Finaliza o jogo se a pontuação chegar a 10

        exibir_pontuacao(pontos)  # Exibir a pontuação

        # Atualizar a tela
        pygame.display.update()

        # Definir a taxa de quadros por segundo (FPS)
        clock.tick(30)

    # Exibir a pontuação final
    font = pygame.font.SysFont(None, 75)
    texto_final = font.render(f"Você fez {pontos} pontos!", True, (0, 0, 0))
    screen.blit(texto_final, (screen_width // 2 - texto_final.get_width() // 2, screen_height // 2))
    pygame.display.update()

    # Aguardar um tempo antes de fechar
    pygame.time.wait(3000)
    pygame.quit()

# Chamar a função para rodar o jogo
jogo()
