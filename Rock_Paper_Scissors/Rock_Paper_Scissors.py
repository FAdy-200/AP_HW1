import random


class Rock_Paper_Scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.aiWins = 0
        self.humanWins = 0
        self.roundsPlayed = 0
        self.humanChoice = None
        self.aiChoice = None
        self.order = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        self.gameOn = True

    def __getRoundWinner(self):
        if self.order[self.humanChoice] == self.aiChoice:
            self.humanWins += 1
            self.roundsPlayed += 1
            return "Human"
        elif self.order[self.aiChoice] == self.humanChoice:
            self.aiWins += 1
            self.roundsPlayed += 1
            return "Computer"
        else:
            self.roundsPlayed += 1
            return "Draw"

    def getGameWinner(self):
        roundsLeft = self.rounds - self.roundsPlayed
        if abs(self.humanWins - self.aiWins) >= roundsLeft + 1:
            if self.humanWins > self.aiWins:
                print("The human has won the game")
            else:
                print("The computer has won the game")
            self.gameOn = False
        else:
            return

    def __getAiChoice(self):
        d = {0: "Scissors", 1: "Rock", 2: "Paper"}
        x = random.randint(0, 2)
        self.aiChoice = d[x]

    def playAround(self, choice):
        self.humanChoice = choice
        self.__getAiChoice()
        w = self.__getRoundWinner()
        if w != "Draw":
            print("Computer choose {}".format(self.aiChoice))
            print("{} has won this round".format(w))
        else:
            print("it was a draw the round will be counted form the total game played")
        self.getGameWinner()


d = {0: "Scissors", 1: "Rock", 2: "Paper"}
# n = int(input())
n = 100000
r = Rock_Paper_Scissors(n)
while r.gameOn:
    r.playAround(d[random.randint(0, 2)])
    # r.playAround(d[int(input())])
