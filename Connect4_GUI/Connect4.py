# CSE313 HW Assignment 1
#
# Topic: OOP and design patterns
# Author : Fadi Alahmad ALomar 120180049
# Date : 06/12/2020
# a backend implementing the connect 4 game logic


import re


class Connect4:
    def __init__(self):
        # creating the mutable grid as a list of strings where there is a . (dot) between each row
        self.gridMutable = list(("O" * 7 + ".") * 5 + ("O" * 7))
        # joining the mutable grid into ine string to be used in Regex searching
        self.grid = "".join(self.gridMutable)
        self.playerTurn = "R"
        self.gameOn = True
        self.rounds = 0
        self.winner = None

    def _changePlayer(self):
        """
        this function changes the playerTurn when needed
        :return:
        """
        if self.playerTurn == "R":
            self.playerTurn = "B"
        else:
            self.playerTurn = "R"

    def _returnMovePlace(self, move):
        """
        this function translates the inputted move place to it is right place in out grid it does that by
        adding 8 to the move if the value of its place in the gridMutable is not an empty space or an O
        if the index gets out of range or the inputted value is above 7 the move is out of range and the
        :param move: int
        :return: None or int depending in the move
        """
        if move > 7:
            print("Move out of range")
            return None
        movePlace = move
        try:
            while self.grid[movePlace] != "O":
                movePlace += 8
            return movePlace
        except IndexError:
            print("Move out of range")
            return None

    def makeMove(self, move):
        """
        this function changes the grid according to the player's move
        :param move: int
        :return:
        """

        movePlace = self._returnMovePlace(move)  # getting the translated place of the users input
        if movePlace is not None:  # if the function returned an int thus the move is valid
            self.gridMutable[movePlace] = self.playerTurn  # changing the translated place of the move in the grid
            self.grid = "".join(self.gridMutable)  # rejoining the mutable grid
            self.rounds += 1
            self._checkWinStatus()
            self._changePlayer()
        if self.rounds == 42:  # if the number if turns is 42 then there is no place left and the game is a draw
            self.gameOn = False  # changing the gameOn flag to indicate the game is over
            print("Draw no one won")

    def _checkWinStatus(self):
        """
        this function checks for the winner by creating four regex patterns and checking if any one of them exist in
        the non mutable grid for example the 4's that are next to each other have the pattern p1 RRRR if the playerTurn
        is R the dot separating the rows comes into play here as without it the rows will be considered as one big row
        and p1 would find a match if the end of the first row is RR and the star of the second one is RR
        and teh vertically connected pattern is p2 as it is R.{7}R.{7}R.{7}R where in our non mutable grid the points
        are above each other if the difference between their indices is 7 and in Regex a . (dot) indicates that there
        should be a value in this place but i dont care what it is
        :return:
        """
        p1 = self.playerTurn * 4
        p2 = self.playerTurn + ".{7}" + self.playerTurn + ".{7}" + self.playerTurn + ".{7}" + self.playerTurn
        p3 = self.playerTurn + ".{6}" + self.playerTurn + ".{6}" + self.playerTurn + ".{6}" + self.playerTurn
        p4 = self.playerTurn + ".{8}" + self.playerTurn + ".{8}" + self.playerTurn + ".{8}" + self.playerTurn
        # searching the grid for the four patterns
        c1 = re.search(p1, self.grid)
        c2 = re.search(p2, self.grid)
        c3 = re.search(p3, self.grid)
        c4 = re.search(p4, self.grid)
        if c1 or c2 or c3 or c4:  # if any pattern is found thn we haev a winner
            self.winner = self.playerTurn
            print(self.playerTurn, "Has won the game")
            self.gameOn = False

    def getBoard(self):
        """
        this function translates the grid into a list which has each row as an element in the list
        and reverse the order because we print the top row first not the bottom one
        :return:
        """
        gridUpside = self.grid
        gridRightSide = gridUpside.split(".")[::-1]
        return gridRightSide

    def printBoard(self):
        """
        this function prints the board in the console when called
        :return:
        """
        print()
        for i in self.getBoard():
            print(i)
