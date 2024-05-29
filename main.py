import pygame
pygame.init()
tamanho = (800,600) 
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron Man")
branco = (255, 255, 255)
preto = (0, 0, 0)
posicaoXPersona = 400
posicaoYPersona = 300
movimentoXPersona = 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPersona =  + 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPersona =  - 5 
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPersona =  + 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPersona =  - 5 
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPersona =  0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPersona =  0 
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPersona =  0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPersona =  0
    tela.fill(branco)
    pygame.draw.circle(tela, preto, (400, 300), 40, 0)
    pygame.display.update()
    relogio.tick(60)