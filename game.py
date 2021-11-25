import pygame
import time
pygame.init()
import pygame
from pygame.locals import *
import pygame as pg

largura        = 800
altura         = 600

configTela     = (largura, altura)
gameDisplay    = pygame.display.set_mode(configTela)

black          = (0, 0, 0)
white          = (255, 255, 255)

pygame.display.set_caption(" Witch CAT")

icone          = pygame.image.load("assets/mucego.ico")

pygame.display.set_icon(icone)

ironMan        = pygame.image.load("assets/gatuso.png")
larguraIronMan = 90
alturaIronMan  = 90
fundo          = pygame.image.load("assets/fundo.png")
missel         = pygame.image.load("assets/mucego.png")
moleu          = pygame.image.load("assets/end.png")
explosaoSound  = pygame.mixer.Sound("assets/tapa2.wav")
misselSound    = pygame.mixer.Sound("assets/estrelaSound.wav")
pulo           = pygame.mixer.Sound("assets/pulo.wav")
misselSound.set_volume(0.2)
misselY        = 500
misselX        = 800
misselAltura   = 80
misselLargura = 80

def mostraIron(x, y):
    gameDisplay.blit(ironMan, (x, y))

def mostraMissel(x, y):
    gameDisplay.blit(missel, (x, y))

def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()

def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Pontuação:"+str(contador), True, white)
    gameDisplay.blit(texto, (10, 10))

def dead(x, y):
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    gameDisplay.fill(white)
    gameDisplay.blit(fundo, (0, 0))
    print(gameDisplay.blit(moleu, (x, y)))
    pygame.display.update()
    time.sleep(3)
    game()    


def game():
    pygame.mixer.music.load("assets/MCPOZE.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    misselVelocidade = 0
    misselY = 0
    misselX = 0
    desvios = 0
    
    ironPosicaoX = 10
    ironPosicaoY = 485
    vel          = 5
    isJump       = False
    jumpCount    = 10
    clock        = pygame.time.Clock()
    white        = (255, 255, 255)
    run          = True
   
    # pygame.mixer.Sound.play(misselSound)

    while run:
        # pega as ações da tela. Ex.: fechar, click de uma tecla ou do mouse

        acoes = pygame.event.get()
        
          # devolve uma lista de ações

        # [ini] mapeando as ações
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        # definindo o fundo do game]
        # escreverPlacar(desvios)
        # misselX = misselX - misselVelocidade
        # misselX = 0
        # mostraMissel(misselX, misselY)
        if misselX <= 0:
            misselX = 800
            desvios = desvios+1
            # misselVelocidade +=1
            # misselVelocidade = misselVelocidade -5
        if misselX > 0:
            misselY = 485
            misselX = misselX - misselVelocidade        
            misselVelocidade = 15
           
        mostraMissel(misselX, misselY)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and ironPosicaoX > vel: 
            ironPosicaoX -= vel

        if keys[pygame.K_RIGHT] and ironPosicaoX < 1400 - vel - ironPosicaoX:  
            ironPosicaoX += vel
            
        if not(isJump): 

            if keys[pygame.K_DOWN] and ironPosicaoY < 500 - ironPosicaoY - vel:
                ironPosicaoY += vel

            if keys[pygame.K_SPACE]:
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.Sound.play(pulo)
                isJump = True
        else:
            if jumpCount >= -10:
                ironPosicaoY -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
        
        gameDisplay.fill((0,0,0))

        if ironPosicaoX < misselX and ironPosicaoX+larguraIronMan > misselX and ironPosicaoY == misselY or ironPosicaoX > misselX and ironPosicaoX-larguraIronMan-45 < misselX and ironPosicaoY == misselY:
            while True:
                dead(265,130)
                break
                
        # analise de colisão com o IronMan
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))

        # definindo o fundo do game]
        escreverPlacar(desvios)
        mostraMissel(misselX, misselY)
        mostraIron(ironPosicaoX, ironPosicaoY)
        pygame.display.update()
        clock.tick(60)  # faz com que o while execute 60x por segundo
game()