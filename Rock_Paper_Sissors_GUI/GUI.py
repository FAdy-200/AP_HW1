import pygame
import sys
from Rock_Paper_Scissors.Rock_Paper_Scissors import Rock_Paper_Scissors

pygame.init()
size = width, height = 672, 622
grey = 254, 254, 254
r = Rock_Paper_Scissors(1)
screen = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 20)
paperBig = pygame.image.load("Paper 1.png")
paperSmall = pygame.image.load("Paper 2.png")
rockBig = pygame.image.load("Rock 1.png")
rockSmall = pygame.image.load("Rock 2.png")
scissorsBig = pygame.image.load("Scissors 1.png")
scissorsSmall = pygame.image.load("Scissors 2.png")
text1 = font.render("Please enter the number of rounds you want to play", True, (0, 0, 0))
i = False
n = ""
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if not i:
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_RETURN:
                    n += event.unicode
                    print(n)
                else:
                    try:
                        n = int(n)
                        i = True
                        r = Rock_Paper_Scissors(n)
                    except:
                        n = ""
                        text1 = font.render("The input format were wrong please reenter the number of rounds", True, (0, 0, 0))

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 645 > mouse[1] > 460:
                    if 200 > mouse[0] > 100:
                        r.playAround("Rock")
                    elif 400 > mouse[0] > 300:
                        r.playAround("Paper")
                    elif 600 > mouse[0] > 500:
                        r.playAround("Scissors")
    mouse = pygame.mouse.get_pos()
    screen.fill(grey)
    if i:
        if r.gameOn:

            screen.blit(rockSmall, (100, 460))
            screen.blit(scissorsSmall, (500, 460))
            screen.blit(paperSmall, (300, 460))
            # screen.blit(paperBig, (200, 200))
        else:
            winner = font.render(r.getGameWinner(), True, (0, 0, 0))
            wr = winner.get_rect()
            wr.center = width / 2, height / 2
            screen.blit(winner, wr)
    else:
        tn = font.render("Number of rounds: " + n, True, (0, 0, 0))
        tnr = tn.get_rect()
        tnr.center = width / 2, height / 2 + 100
        tr = text1.get_rect()
        tr.center = width / 2, height / 2
        screen.blit(text1, tr)
        screen.blit(tn, tnr)
    pygame.display.flip()
