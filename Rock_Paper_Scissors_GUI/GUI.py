# CSE313 HW Assignment 1
#
# Topic: OOP and design patterns
# Author : Fadi Alahmad ALomar 120180049
# Date : 06/12/2020
# a GUI for the game Rock Paper Scissors


import pygame
import sys
from Rock_Paper_Scissors_GUI.Rock_Paper_Scissors import Rock_Paper_Scissors


class RockPaperScissorsGUI:
    def __init__(self):
        pygame.init()  # initiates the pygame library
        self.size = self.width, self.height = 672, 622  # initiates the size of the window
        self.white = 254, 254, 254  # defines the RGB values of the color white
        self.black = 0, 0, 0  # defines the RGB values of the color black
        self.screen = pygame.display.set_mode(self.size)  # initiates the window with the wanted size
        # defines the font that will be used to render texts on the screen
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.paperBig = pygame.image.load("Rock_Paper_Scissors_GUI\Paper 1.png")  # loads the image for the big paper
        # loads the image for the small paper
        self.paperSmall = pygame.image.load("Rock_Paper_Scissors_GUI\Paper 2.png")
        self.rockBig = pygame.image.load("Rock_Paper_Scissors_GUI\Rock 1.png")  # loads the image of the big rock
        self.rockSmall = pygame.image.load("Rock_Paper_Scissors_GUI\Rock 2.png")  # loads the image of the small rock
        # loads the image of the big scissors
        self.scissorsBig = pygame.image.load("Rock_Paper_Scissors_GUI\Scissors 1.png")
        # loads the image of the small scissors
        self.scissorsSmall = pygame.image.load("Rock_Paper_Scissors_GUI\Scissors 2.png")
        # initiates the start screen text
        self.startScreenText = self.font.render("Please enter the number of rounds you want to play", True, self.black)
        # translation dictionary to map the choices to their respectful pygame image with the addition of a
        # blank text to be rendered when no choice have been made yet
        self.translatingDictionary = {"Rock": self.rockBig, "Scissors": self.scissorsBig, "Paper": self.paperBig,
                                      None: self.font.render("", True, self.white)}
        self.mouse = pygame.mouse.get_pos()  # getting the initial mouse position on the window
        # a flag to check  if the use has inputted the number of rounds and the game starts or not
        self.gameModeFlag = False
        self.numberOfRounds = ""
        self.gameWinner = None
        self.game = None  # a variable to store the instance of the Rock_Paper_Scissors class to be able to play

    def _check_events(self):
        """
        this function checks for the events that are happening on the screen
        :return:
        """
        for event in pygame.event.get():  # getting the events that are happening on the screen
            if event.type == pygame.QUIT:  # checking if the user quit the screen
                sys.exit()  # closing the program
            # if the game has not started yet and the user is still inputting the number of rounds
            if not self.gameModeFlag:
                # calling the function to set the number of rounds and passing the event that happened
                self._set_number_of_rounds(event)
            elif self.game.gameOn:  # if the game mode flag is True and the game is still on
                # calling the function to set the users choice and passing the event that happened
                self._set_user_input(event)

    def _set_number_of_rounds(self, event):
        """
        this function sets the number of rounds and changes the needed flags and parameters and creates
        the game instance when the user inputs the number of rounds in the correct format and prompts him to reenter the
        n umber of rounds if he pressed anything but numbers
        :param event: pygame.event object
        :return: None
        """
        if event.type == pygame.KEYDOWN:  # if the event was a keyboard press
            if event.key != pygame.K_RETURN:  # if the key pressed was not Enter
                self.numberOfRounds += event.unicode  # add the key pressed to the number of rounds
            else:  # if the key pressed was enter
                try:  # trying to change the numberOfRounds type to int
                    self.numberOfRounds = int(self.numberOfRounds)
                    self.gameModeFlag = True
                    # initiating the game with the number of rounds inputted
                    self.game = Rock_Paper_Scissors(self.numberOfRounds)
                except:  # if the user entered the number of rounds anything but numbers
                    self.numberOfRounds = ""  # resetting the number of rounds to an empty string
                    # changing the start screen text
                    self.startScreenText = self.font.render(
                        "The input format were wrong please reenter the number of rounds",
                        True,
                        self.black)

    def _set_user_input(self, event):
        """
        this function checks if the user has pressed on one of the choices he has and plays a round accordingly
        :param event: pygame.event object 
        :return: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:  # if the event was a mouse left click
            if 650 > self.mouse[1] > 420:  # if the mouse's vertical position was in the range of the inputs
                # if the mouse's horizontal position was in the range of the rock image
                if 200 > self.mouse[0] > 100:
                    self.game.play_a_round("Rock")  # plays a round with the human choice being Rock
                # if the mouse's horizontal position was in the range of the paper image
                elif 400 > self.mouse[0] > 300:
                    self.game.play_a_round("Paper")  # plays a round with the human choice being Paper
                # if the mouse's horizontal position was in the range of the scissors image
                elif 600 > self.mouse[0] > 500:
                    self.game.play_a_round("Scissors")  # plays a round with the human choice being Scissors

    def _center_text(self, text, mode=None):
        """
        this function takes a pygame surface object and centers it according to the param mode
        :param text:pygame surface object (the function is used for texts but can be used for any pygame.surface object)
        :param mode: defines where the texts center will be
        :return: pygame rectangle object
        """
        tr = text.get_rect()  # gets the rectangle of the text
        if mode is None:
            # sets the center of the rectangle to be in the center of the screen
            tr.center = self.width / 2, self.height / 2
        elif mode == "Center at 100":
            # sets the center of the rectangle to be in the horizontal center of the screen but the vertical to be 100
            tr.center = self.width / 2, 100
        elif mode == "Center shifted 100":
            # sets the center of the rectangle to be in the center of the screen but shifted 100 pixels down
            tr.center = self.width / 2, self.height / 2 + 100
        elif mode == "Center shifted 120":
            # sets the the center of the rectangle to be in the center of the screen but shifted 120 pixels down
            tr.center = self.width / 2, self.height / 2 + 120
        return tr

    def _draw_player_choices(self):
        """
        this function draws tha players choices on the screen
        :return: None
        """
        # rendering the image of the small rock on the screen on the right position
        self.screen.blit(self.rockSmall, (100, 460))
        # rendering the image of the small scissors on the screen on the right position
        self.screen.blit(self.scissorsSmall, (500, 460))
        # rendering the image of the small paper on the screen on the right position
        self.screen.blit(self.paperSmall, (300, 460))

    def _draw_computer_choice(self):
        """
        this function gets the computers choice and draws it on the screen
        :return:
        """
        computerChoice = self.game.computerChoice  # getting the computer choice
        # rendering the computer choices picture in the right place
        self.screen.blit(self.translatingDictionary[computerChoice], (self.width / 2 - 100, 150))
        t = self.font.render("The computer choose:", True, self.black)  # creating a pygame text object to be rendered
        tr = self._center_text(t, "Center at 100")
        self.screen.blit(t, tr)  # rendering the computer choices mage in the right position

    def _draw_round_winner(self):
        """
        this function draws the text to indicate who won
        :return:
        """
        winnerOfRound = self.game.lastRoundWinner  # getting the round winner
        if winnerOfRound == "Human" or winnerOfRound == "Computer":  # checking to see if the round was a Draw
            t = self.font.render(winnerOfRound + " has won this round", True, self.black)  # text to be  rendered
            tr = self._center_text(t, "Center shifted 100")  # centering the text
            self.screen.blit(t, tr)  # rendering he text on the screen
        elif winnerOfRound == "Draw":
            t1 = self.font.render(winnerOfRound + " no one has won this round", True, self.black)
            t1r = self._center_text(t1, "Center shifted 100")
            t2 = self.font.render(" but it will be counted as a played round", True, self.black)
            t2r = self._center_text(t2, "Center shifted 120")
            self.screen.blit(t1, t1r)
            self.screen.blit(t2, t2r)

    def _draw_game_statistics(self):
        """
        this function draws the number of rounds left and number of rounds humans or computer has won on the top left
        of the screen it uses a different font size that the rest to be smaller
        :return:
        """
        font = pygame.font.Font('freesansbold.ttf', 10)
        nrl = "Number of rounds left : {}".format(self.game.roundsLeft)
        nrh = "Number of rounds Human won : {}".format(self.game.humanWins)
        nrc = "Number of rounds the Computer won {}".format(self.game.computerWins)
        text = [font.render(nrl, True, self.black), font.render(nrh, True, self.black),
                font.render(nrc, True, self.black)]
        for i in range(len(text)):
            self.screen.blit(text[i], (0, 10 * i))

    def _draw_game_winner(self):
        """
        this function draws the text to indicate the game winner
        :return:
        """
        if self.gameWinner is None:  # checking if the game winner has been assigned
            self.gameWinner = self.game.get_game_winner()  # getting the game winner
        if self.gameWinner != "Draw":  # checking to see if the game winner was a Draw
            t = self.font.render(self.gameWinner + " has won the game", True, self.black)
            tr = self._center_text(t, "Center shifted 100")
            self.screen.blit(t, tr)
        else:
            t = self.font.render(self.gameWinner + " no one has won this game", True, self.black)
            tr = self._center_text(t, "Center shifted 100")
            self.screen.blit(t, tr)

    def _pre_game_screen(self):
        """
        this function draws the pre game screen
        :return:
        """
        tr = self._center_text(self.startScreenText)
        tn = self.font.render("Number of rounds = " + self.numberOfRounds, True, self.black)
        tnr = self._center_text(tn, "Center shifted 100")
        self.screen.blit(self.startScreenText, tr)
        self.screen.blit(tn, tnr)

    def start_playing(self):
        while True:  # infinitely showing the screen until the user closes teh window
            self.mouse = pygame.mouse.get_pos()  # updating the mouse's position
            self._check_events()
            self.screen.fill(self.white)  # filling the screen with the color white
            if self.gameModeFlag:  # checking the gameModeFlag to see if the user has inputted the number of rounds yet 
                if self.game.gameOn:  # checking to see if the game is still on
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
            pygame.display.flip()  # updating the screen with the new rendered images
