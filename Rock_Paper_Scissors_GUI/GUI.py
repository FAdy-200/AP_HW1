import pygame
import sys
from Rock_Paper_Scissors_GUI.Rock_Paper_Scissors import Rock_Paper_Scissors


class RockPaperScissorsGUI:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 672, 622
        self.white = 254, 254, 254
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.paperBig = pygame.image.load("Rock_Paper_Scissors_GUI\Paper 1.png")
        self.paperSmall = pygame.image.load("Rock_Paper_Scissors_GUI\Paper 2.png")
        self.rockBig = pygame.image.load("Rock_Paper_Scissors_GUI\Rock 1.png")
        self.rockSmall = pygame.image.load("Rock_Paper_Scissors_GUI\Rock 2.png")
        self.scissorsBig = pygame.image.load("Rock_Paper_Scissors_GUI\Scissors 1.png")
        self.scissorsSmall = pygame.image.load("Rock_Paper_Scissors_GUI\Scissors 2.png")
        self.startScreenText = self.font.render("Please enter the number of rounds you want to play", True, self.black)
        self.translatingDictionary = {"Rock": self.rockBig, "Scissors": self.scissorsBig, "Paper": self.paperBig,
                                      None: self.font.render("", True, self.white)}
        self.mouse = pygame.mouse.get_pos()
        self.gameModeFlag = False
        self.numberOfRounds = ""
        self.game = None

    def _set_number_of_rounds(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_RETURN:
                self.numberOfRounds += event.unicode
            else:
                try:
                    self.numberOfRounds = int(self.numberOfRounds)
                    self.gameModeFlag = True
                    self.game = Rock_Paper_Scissors(self.numberOfRounds)
                    return True
                except:
                    self.numberOfRounds = ""
                    self.startScreenText = self.font.render(
                        "The input format were wrong please reenter the number of rounds",
                        True,
                        self.black)

    def _set_user_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 650 > self.mouse[1] > 420:
                if 200 > self.mouse[0] > 100:
                    self.game.play_a_round("Rock")
                elif 400 > self.mouse[0] > 300:
                    self.game.play_a_round("Paper")
                elif 600 > self.mouse[0] > 500:
                    self.game.play_a_round("Scissors")

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not self.gameModeFlag:
                self._set_number_of_rounds(event)
            elif self.game.gameOn:
                self._set_user_input(event)

    def _center_text(self, text, mode=None):
        tr = text.get_rect()
        if mode is None:
            tr.center = self.width / 2, self.height / 2
        elif mode == "Computer Choice":
            tr.center = self.width / 2, 100
        elif mode == "Pre Game":
            tr.center = self.width / 2, self.height / 2 + 100
        elif mode == "Draw":
            tr.center = self.width / 2, self.height / 2 + 120
        return tr

    def _draw_player_choices(self):
        self.screen.blit(self.rockSmall, (100, 460))
        self.screen.blit(self.scissorsSmall, (500, 460))
        self.screen.blit(self.paperSmall, (300, 460))

    def _draw_computer_choice(self):
        aic = self.game.aiChoice
        self.screen.blit(self.translatingDictionary[aic], (self.width / 2 - 100, 150))
        t = self.font.render("The computer choose:", True, self.black)
        tr = self._center_text(t, "Computer Choice")
        self.screen.blit(t, tr)

    def _draw_round_winner(self):
        winnerOfRound = self.game.lastRoundWinner
        if winnerOfRound == "Human" or winnerOfRound == "Computer":
            t = self.font.render(winnerOfRound + " has won this round", True, self.black)
            tr = self._center_text(t, "Pre Game")
            self.screen.blit(t, tr)
        elif winnerOfRound == "Draw":
            t1 = self.font.render(winnerOfRound + " no one has won this round", True, self.black)
            t1r = self._center_text(t1, "Pre Game")
            t2 = self.font.render(" but it will be counted as a played round", True, self.black)
            t2r = self._center_text(t2, "Draw")
            self.screen.blit(t1, t1r)
            self.screen.blit(t2, t2r)

    def _draw_game_winner(self):
        winnerOfGame = self.game.get_game_winner()
        if winnerOfGame != "Draw":
            t = self.font.render(winnerOfGame + " has won the game", True, self.black)
            tr = self._center_text(t, "Pre Game")
            self.screen.blit(t, tr)
        else:
            t = self.font.render(winnerOfGame + " no one has won this game", True, self.black)
            tr = self._center_text(t, "Pre Game")
            self.screen.blit(t, tr)

    def _draw_game_statistics(self):
        font = pygame.font.Font('freesansbold.ttf', 10)
        nrl = "Number of rounds left : {}".format(self.game.roundsLeft)
        nrh = "Number of rounds Human won : {}".format(self.game.humanWins)
        nrc = "Number of rounds the Computer won {}".format(self.game.aiWins)
        text = [font.render(nrl, True, self.black), font.render(nrh, True, self.black),
                font.render(nrc, True, self.black)]
        for i in range(len(text)):
            self.screen.blit(text[i], (0, 10 * i))

    def _pre_game_screen(self):
        tr = self._center_text(self.startScreenText)

        tn = self.font.render("Number of rounds = " + self.numberOfRounds, True, self.black)
        tnr = self._center_text(tn, "Pre Game")
        self.screen.blit(self.startScreenText, tr)
        self.screen.blit(tn, tnr)

    def start_playing(self):
        while True:
            self._check_events()
            self.mouse = pygame.mouse.get_pos()
            self.screen.fill(self.white)
            if self.gameModeFlag:
                if self.game.gameOn:
                    self._draw_player_choices()
                    self._draw_computer_choice()
                    self._draw_round_winner()
                    self._draw_game_statistics()
                else:
                    self._draw_game_winner()
                    self._draw_computer_choice()
                    self._draw_game_statistics()
            else:
                self._pre_game_screen()
            pygame.display.flip()
