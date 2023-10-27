import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Configurações
screen_width = 600
screen_height = 80
background_color = (0, 0, 0)
text_color = (255, 0, 0)
font_size = 36
text_to_scroll = "#UP3d_DF ----- Modeling-----3d Print-------KC 390 MODELING----------SUBSCRIBE (INSCREVA-SE)"

# Crie a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frase Rolando")

# Carregue a fonte
font = pygame.font.Font(None, font_size)

# Obtenha a largura da frase
text_width, text_height = font.size(text_to_scroll)

# Inicialize as coordenadas X e Y da frase
x = screen_width
y = (screen_height - text_height) // 2
# Defina a velocidade de rolagem

scroll_speed = 0.02

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpe a tela
    screen.fill(background_color)

    # Desenhe a frase na tela
    text_surface = font.render(text_to_scroll, True, text_color)
    screen.blit(text_surface, (x, y))

    # Atualize a posição da frase
    x -= scroll_speed

    # Verifique se a frase saiu da tela
    if x + text_width < 0:
        x = screen_width

    # Atualize a tela
    pygame.display.update()

# Encerre o Pygame
pygame.quit()

# Saia do programa
sys.exit()
