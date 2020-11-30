import re


class Connect4:
    def __init__(self):
        self.gridMutable = list(("O" * 7 + ".") * 6)
        self.grid = "".join(self.gridMutable)
        self.playerTurn = "R"
        self.gameOn = True
        self.rounds = 0

    def __changePlayer(self):
        if self.playerTurn == "R":
            self.playerTurn = "Y"
        else:
            self.playerTurn = "R"

    def __returnMovePlace(self, move):
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

    def make_move(self, move):
        movePlace = self.__returnMovePlace(move)
        if movePlace is not None:
            self.gridMutable[movePlace] = self.playerTurn
            self.grid = "".join(self.gridMutable)
            self.rounds += 1
            self.__checkWinStatus()
            self.__changePlayer()
        if self.rounds == 42:
            self.gameOn = False
            print("Draw no one won")

    def __checkWinStatus(self):
        p1 = self.playerTurn * 4
        p2 = self.playerTurn + ".{7}" + self.playerTurn + ".{7}" + self.playerTurn + ".{7}" + self.playerTurn
        p3 = self.playerTurn + ".{6}" + self.playerTurn + ".{6}" + self.playerTurn + ".{6}" + self.playerTurn
        p4 = self.playerTurn + ".{8}" + self.playerTurn + ".{8}" + self.playerTurn + ".{8}" + self.playerTurn
        c1 = re.search(p1, self.grid)
        c2 = re.search(p2, self.grid)
        c3 = re.search(p3, self.grid)
        c4 = re.search(p4, self.grid)
        if c1 or c2 or c3 or c4:
            print(self.playerTurn, "Has won the game")
            self.gameOn = False

    def printBoard(self):
        gridUpside = self.grid[::-1]
        gridRightSide = gridUpside.split(".")
        for i in gridRightSide:
            print(i[::-1])


s = Connect4()
# s.printBoard()
import random
for _ in range(int(input())):
    while s.gameOn:
        # m = int(input("\nIt is {} turn please input the place where you want to drop your circle\n".format(s.playerTurn)))
        m = random.randint(0, 6)
        s.make_move(m)
    s.printBoard()
    s = Connect4()
