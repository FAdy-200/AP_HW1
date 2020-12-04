import pygame
import sys
import Rock_Paper_Scissors_GUI.GUI as RPS
import Connect4_GUI.GUI as C4


class startingScreen:
    """
    this class when called creates the starting screen of which the player chooses the game he/she wants to play
    """
    def __init__(self):
        pygame.init()  # initiates the pygame library
        self.size = self.width, self.height = 672, 622  # initiates the size of the window
        self.white = 254, 254, 254  # defines the RGB values of the color white
        self.black = 0, 0, 0  # defines the RGB values of the color black
        self.screen = pygame.display.set_mode(self.size)  # initiates the window with the wanted size
        self.font = pygame.font.Font('freesansbold.ttf', 20)  # defines the font that will be used to render texts on the screen
        self.mouse = pygame.mouse.get_pos()  # gets the initial mouse position

    def _center_text(self, text, mode=None):
        """
        this function takes a pygame surface object and centers it according to the param mode
        :param text: pygame surface object (the function is used for texts but can be used for anything)
        :param mode: defines where the texts center will be
        :return: pygame rectangle object
        """
        tr = text.get_rect()  # gets the rectangle of the text
        if mode is None:
            tr.center = self.width / 2, self.height / 2  # sets the center of the rectangle to be in the center of the screen
        elif mode == "left":
            tr.center = self.width / 2 + 100, self.height / 2 + 100  # sets the center of the rectagnle to be under the center of the screen shifted to the left
        elif mode == "right":
            tr.center = self.width / 2 - 100, self.height / 2 + 100  # sets the center of the rectagnle to be under the center of the screen shifted to the right
        return tr

    @property
    def game_chooser(self):
        """
        this function renders the screen
        :return: RPS or C4 according to the users choice
        """
        # self.font.render takes the text to be rendered, if it will get antialiased and the color as parameters
        text = self.font.render("Please Choose the Game you want to play", True, self.black)  # text to be rendered on the screen
        c4 = self.font.render("Connect 4", True, self.black)  # text to be rendered on the screen
        rps = self.font.render("Rock Paper Scissors", True, self.black)  # text to be rendered on the screen
        tr = self._center_text(text)  # centering the text accordingly
        c4r = self._center_text(c4, "left")  # centering the text accordingly
        rpsr = self._center_text(rps, "right")  # centering the text accordingly
        while True:  # infinitely showing the screen until the user chooses
            for event in pygame.event.get():  # getting the events that are happening on the screen
                if event.type == pygame.QUIT:  # checking if the user quit the screen
                    sys.exit()  # closing the program
                if event.type == pygame.MOUSEBUTTONDOWN:  # checking if the user pressed the left click on the screen
                    if 430 > self.mouse[1] > 370:  # checking if the mouse is on the vertical range of the tow choices
                        if 360 > self.mouse[0] > 120:  # checking to see if the mouse is in the horizontal range of RPS
                            return "RPS"  # ending the function and returning RPS
                        elif 500 > self.mouse[0] > 360:  # checking to see if the mouse is in the horizontal range of C4
                            return "C4"  # ending the function and returning C4
            self.mouse = pygame.mouse.get_pos()  # getting the mouse's position on the screen
            self.screen.fill(self.white)  # filling the screen with the color white
            self.screen.blit(text, tr)  # rendering the text on the screen in the right position
            self.screen.blit(c4, c4r)  # rendering the text on the screen in the right position
            self.screen.blit(rps, rpsr)  # rendering the text on the screen in the right position
            pygame.display.flip()  # updates the screen with the new rendered objects


s = startingScreen()
game = s.game_chooser
# choosing which class to initiate and to start playing
if game == "RPS":
    g = RPS.RockPaperScissorsGUI()
else:
    g = C4.connect4GUI()
g.start_playing()
