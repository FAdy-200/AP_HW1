import pygame
import sys
from Connect4_GUI.Connect4 import Connect4


class connect4GUI:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 672, 622
        self.white = 254, 254, 254
        self.black_color = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.mouse = pygame.mouse.get_pos()
        self.game = Connect4()
        self.background = pygame.image.load("Connect4_GUI\Connect_4_Background.png")
        self.red = pygame.image.load("Connect4_GUI\R2.png")
        self.black = pygame.image.load("Connect4_GUI\B2.png")
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.saveCheck = False
        self.lastScreen = None
        self.translatingDictionary = {"R": self.red, "B": self.black}

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif self.game.gameOn:
                self._set_user_input(event)

    def _set_user_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.mouse[0] < 95:
                self.game.makeMove(0)
            elif self.mouse[0] < 190:
                self.game.makeMove(1)
            elif self.mouse[0] < 285:
                self.game.makeMove(2)
            elif self.mouse[0] < 380:
                self.game.makeMove(3)
            elif self.mouse[0] < 475:
                self.game.makeMove(4)
            elif self.mouse[0] < 570:
                self.game.makeMove(5)
            elif self.mouse[0] < 665:
                self.game.makeMove(6)
            print()
            for i in self.game.getBoard():
                print(i)

    def _draw_board(self):

        sg = self.game.getBoard()
        for i in range(6):
            for j in range(7):
                if sg[i][j] != "O":
                    self.screen.blit(self.translatingDictionary[sg[i][j]], (11 + 95.5 * j, 20 + 93 * i))

    def _play_a_round(self):
        self.mouse = pygame.mouse.get_pos()
        self.screen.fill(self.white)
        self.screen.blit(self.background,(0,0))
        self._draw_board()

    def _winner_screen(self):
        self.screen.fill(self.white)
        self.lastScreen = pygame.image.load("Connect4_GUI\last.png")
        self.lastScreen.set_alpha(100)
        self.screen.blit(self.lastScreen, (0, 0))
        t = self.font.render('Draw no one won', True, (0, 0, 0))
        tr = t.get_rect()
        tr.center = (self.width / 2, (self.height / 2))
        if self.game.winner is not None:
            self.screen.blit(self.translatingDictionary[self.game.winner], (self.width / 2 - 38, self.height / 2))
            t = self.font.render('Has won the game', True, (0, 0, 0))
            tr = t.get_rect()
            tr.center = (self.width / 2, (self.height / 2) + 100)

        self.screen.blit(t, tr)

    def start_playing(self):
        while True:
            self._check_events()
            if self.game.gameOn:
                self._play_a_round()
            else:
                if not self.saveCheck:
                    self._draw_board()
                    pygame.image.save(self.screen, "Connect4_GUI\last.png")
                    self.saveCheck = True
                self._winner_screen()
            pygame.display.flip()
