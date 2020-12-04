import pygame
import sys
from Connect4.Connect4 import Connect4
import random
s = Connect4()
pygame.init()

size = width, height = 672, 622
white = 254, 254, 254

screen = pygame.display.set_mode(size)

background = pygame.image.load("Connect_4_Background.png")
red = pygame.image.load("R2.png")
black = pygame.image.load("B2.png")
font = pygame.font.Font('freesansbold.ttf', 32)
save = 0
d = {"R": red, "B": black}
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and s.gameOn:
            if mouse[0] < 100:
                s.makeMove(0)
            elif mouse[0] < 200:
                s.makeMove(1)
            elif mouse[0] < 300:
                s.makeMove(2)
            elif mouse[0] < 400:
                s.makeMove(3)
            elif mouse[0] < 500:
                s.makeMove(4)
            elif mouse[0] < 600:
                s.makeMove(5)
            elif mouse[0] < 700:
                s.makeMove(6)
            print()
            for i in s.getBoard():
                print(i)
    if s.gameOn:
        s.makeMove(random.randint(0, 6))
        mouse = pygame.mouse.get_pos()
        screen.fill(white)
        screen.blit(background, (0, 0))
        sg = s.getBoard()
        for i in range(6):
            for j in range(7):
                if sg[i][j] != "O":
                    screen.blit(d[sg[i][j]], (11 + 95.5 * j, 20 + 93 * i))
    else:
        if save == 0:
            sg = s.getBoard()
            for i in range(6):
                for j in range(7):
                    if sg[i][j] != "O":
                        screen.blit(d[sg[i][j]], (11 + 95.5 * j, 20 + 93 * i))
            pygame.image.save(screen, "last.png")
            save = 1
        screen.fill(white)
        image = pygame.image.load("last.png")
        image.set_alpha(100)
        screen.blit(image, (0, 0))
        if s.winner is not None:
            screen.blit(d[s.winner], ((width / 2) - 38, height / 2))
            text = font.render('Has won the game', True, (0, 0, 0))
            textrect = text.get_rect()
            textrect.center = (width / 2, (height / 2) + 100)
            screen.blit(text, textrect)
        else:
            text = font.render('Draw no one won', True, (0, 0, 0))
            textrect = text.get_rect()
            textrect.center = (width / 2, (height / 2))
            screen.blit(text, textrect)
        s=Connect4()
    pygame.display.flip()
