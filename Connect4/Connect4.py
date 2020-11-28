import re


class Connect4:
    def __init__(self):
        self.grid = list(("O" * 7+".") * 6)
        self.player = "R"
        self.gameOn = True

    def _Changeplayer(self):
        if self.player == "R":
            self.player = "Y"
        else:
            self.player = "R"

    def make_move(self, move):
        if move > 7:
            print("Move out of range")
            return
        while True:
            try:
                if self.grid[move] != "O":
                    move += 8
                else:
                    self.grid[move] = self.player
                    self._check_win_status()
                    self._Changeplayer()
                    break
            except:
                print("Move out of range")
                break

    def _check_win_status(self):
        p1 = self.player * 4
        p3 = self.player + ".{7}" + self.player + ".{7}" + self.player + ".{7}" + self.player
        c1 = re.search(p1, "".join(self.grid))
        c3 = re.search(p3, "".join(self.grid))
        if c1 or c3:
            print(self.player, "Has won the game")
            self.gameOn = False

    def printBoard(self):
        j = 1
        tempGrid = []
        g = []
        i = 0
        while i < len(self.grid):
            if j % 7 == 0:
                g.append(self.grid[i])
                tempGrid.append("".join(g))
                g = []
                j += 1
                i += 2

            else:

                g.append(self.grid[i])
                j += 1
                i += 1
        for i in range(1, len(tempGrid)+1):
            print(tempGrid[-i])

s = Connect4()
# s.printBoard()
import random
for _ in range(int(input())):
    while s.gameOn:
        m = int(input("\nIt is {} turn please input the place where you want to drop your circle\n".format(s.player)))
        # m = random.randint(0, 6)
        s.make_move(m)
        s.printBoard()
    s = Connect4()

