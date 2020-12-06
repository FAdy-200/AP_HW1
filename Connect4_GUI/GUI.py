# CSE313 HW Assignment 1
#
# Topic: OOP and design patterns
# Author : Fadi Alahmad ALomar 120180049
# Date : 06/12/2020
# a GUI for the Connect4 game


import pygame
import sys
from Connect4_GUI.Connect4 import Connect4


class connect4GUI:
    """
    this class when called creates an instance of the screen of the game connect 4
    """
    def __init__(self):
        pygame.init()  # initiates the pygame library
        self.size = self.width, self.height = 672, 698  # initiates the size of the window
        self.white = 254, 254, 254  # defines the RGB values of the color white
        self.black_color = 0, 0, 0  # defines the RGB values of the color black
        self.screen = pygame.display.set_mode(self.size)  # initiates the window with the wanted size
        # defines the font that will be used to render texts on the screen
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.mouse = pygame.mouse.get_pos()  # gets the initial mouse position
        self.game = Connect4()  # creates an instance of the game Connect4
        # loading the needed images into the program
        self.background = pygame.image.load("Connect4_GUI\Connect_4_Background.png")
        self.red = pygame.image.load("Connect4_GUI\R2.png")
        self.black = pygame.image.load("Connect4_GUI\B2.png")
        self.saveCheck = False  # a flag to check if the last screen of the game was saved
        # an ending screen variable to have a pygame.surface object in it with the last played grid
        self.endingScreen = None
        # a translation dictionary to map the Connect4 instance variables into pygame images
        self.translatingDictionary = {"R": self.red, "B": self.black}

    def _check_events(self):
        """
        this function checks for the events that are happening on the screen
        :return:
        """
        for event in pygame.event.get():  # getting the events that are happening on the screen
            if event.type == pygame.QUIT:  # checking if the user quit the screen
                sys.exit()  # closing the program
            elif self.game.gameOn:  # checking if the game is still on and no one has won yet
                self._set_user_input(event)

    def _set_user_input(self, event):
        """
        this function checks if the user has pressed on one of the columns and makes a move accordingly
        :param event: pygame.event object
        :return: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:  # if the event was a mouse left click
            if self.mouse[1] > 98:  # if the mouse's vertical position was in the grid range
                # checkin on what column the mouse is and making a move accordingly
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

    def _draw_board(self):
        """
        this function updates the board portion of the screen and the players turn
        :return:
        """
        sb = self.game.getBoard()  # getting the board from the Connect4 instance
        player = self.game.playerTurn  # getting who's turn from the Connect4 instance
        # rendering the corresponding circle of the players turn next to the players turn text
        self.screen.blit(self.translatingDictionary[player], (70, 0))
        # players tun text to be rendered above the board
        playerText = self.font.render("It is          turn, press on the column to play", True, self.black_color)
        self.screen.blit(playerText, (0, 20))
        # updating the grid and adding the right colored circle in the right place according to the Connect4 board
        for i in range(6):
            for j in range(7):
                if sb[i][j] != "O":
                    self.screen.blit(self.translatingDictionary[sb[i][j]], (11 + 95.5 * j, 96 + 93 * i))

    def _play_a_round(self):
        """
        this function updates the screen with the new information
        :return:
        """
        self.mouse = pygame.mouse.get_pos()  # getting the mouse's position
        self.screen.fill(self.white)  # filling the screen with the color white
        self.screen.blit(self.background, (0, 76))  # rendering the background image in the right place
        self._draw_board()

    def _winner_screen(self):
        """
        this function renders the ending screen with it's text and images
        :return:
        """
        self.screen.fill(self.white)
        self.endingScreen = pygame.image.load("Connect4_GUI\last.png")
        self.endingScreen.set_alpha(100)  # sets the transparency level of the image 0 is max 200 is no transparency
        self.screen.blit(self.endingScreen, (0, 0))  # rendering the endingScreen
        t = self.font.render('Draw no one won', True, (0, 0, 0))  # initializing the text to be rendered on the screen
        tr = t.get_rect()  # getting the rectangle of the text
        tr.center = (self.width / 2, (self.height / 2))  # centering the text on the screen
        if self.game.winner is not None:  # if the game winner was a player
            # rendering the image of the wining player in the middle of the screen
            self.screen.blit(self.translatingDictionary[self.game.winner], (self.width / 2 - 38, self.height / 2))
            # changing the text that is to be rendered on the screen
            t = self.font.render('Has won the game', True, (0, 0, 0))
            tr = t.get_rect()
            # shifting the text down by 100 pixel to get it under the winners image
            tr.center = (self.width / 2, (self.height / 2) + 100)

        self.screen.blit(t, tr)  # rendering the text on the screen

    def start_playing(self):
        """
        this function orchestrate the other function to who the game window
        :return:
        """
        while True:
            self._check_events()
            if self.game.gameOn:
                self._play_a_round()
            else:
                if not self.saveCheck:
                    self._draw_board()
                    # saving the last screen before someone won to be used in _winner_screen method
                    pygame.image.save(self.screen, "Connect4_GUI\last.png")
                    self.saveCheck = True
                self._winner_screen()
            pygame.display.flip()  # updating the screen with the new rendered objects
