import pygame
import sys
import Rock_Paper_Scissors_GUI.GUI as RPS
import Connect4_GUI.GUI as C4


class startingScreen:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 672, 622
        self.white = 254, 254, 254
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.mouse = pygame.mouse.get_pos()

    def _center_text(self, text, mode=None):
        tr = text.get_rect()
        if mode is None:
            tr.center = self.width / 2, self.height / 2
        elif mode == "left":
            tr.center = self.width / 2 + 100, self.height / 2 + 100
        elif mode == "right":
            tr.center = self.width / 2 - 100, self.height / 2 + 100
        return tr

    def game_chooser(self):
        text = self.font.render("Please Choose the Game you want to play", True, self.black)
        c4 = self.font.render("Connect 4", True, self.black)
        rps = self.font.render("Rock Paper Scissors", True, self.black)
        tr = self._center_text(text)
        c4r = self._center_text(c4, "left")
        rpsr = self._center_text(rps, "right")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 430 > self.mouse[1] > 370:
                        if 360 > self.mouse[0] > 120:
                            return "RPS"
                        elif 500 > self.mouse[0] > 360:
                            return "C4"
            self.mouse = pygame.mouse.get_pos()
            self.screen.fill(self.white)
            self.screen.blit(text, tr)
            self.screen.blit(c4, c4r)
            self.screen.blit(rps, rpsr)
            pygame.display.flip()


s = startingScreen()
game = s.game_chooser()
if game == "RPS":
    g = RPS.RockPaperScissorsGUI()
else:
    g = C4.connect4GUI()
g.start_playing()
