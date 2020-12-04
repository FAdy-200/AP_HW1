import random


class Rock_Paper_Scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.aiWins = 0
        self.humanWins = 0
        self.roundsPlayed = 0
        self.roundsLeft = self.rounds - self.roundsPlayed
        self.humanChoice = None
        self.aiChoice = None
        self.order = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        self.gameOn = True
        self.lastRoundWinner = ""

    def get_round_winner(self):
        if self.order[self.humanChoice] == self.aiChoice:
            self.humanWins += 1

            self.lastRoundWinner = "Human"
        elif self.order[self.aiChoice] == self.humanChoice:
            self.aiWins += 1
            self.lastRoundWinner = "Computer"
        else:
            self.lastRoundWinner = "Draw"
        self.roundsPlayed += 1
        self.roundsLeft -= 1

    def get_game_winner(self):
        if abs(self.humanWins - self.aiWins) >= self.roundsLeft + 1:
            if self.humanWins > self.aiWins:
                print("The human has won the game")
                self.gameOn = False
                return "Human"
            elif self.humanWins < self.aiWins:
                print("The computer has won the game")
                self.gameOn = False
                return "Computer"
        elif self.roundsLeft == 0:
            print("The game was a draw no one won")
            self.gameOn = False
            return "Draw"

    def __get_computer_choice(self):
        d = {0: "Scissors", 1: "Rock", 2: "Paper"}
        x = random.randint(0, 2)
        self.aiChoice = d[x]

    def play_a_round(self, choice):
        self.humanChoice = choice
        self.__get_computer_choice()
        self.get_round_winner()
        if self.lastRoundWinner != "Draw":
            print("Computer choose {}".format(self.aiChoice))
            print("{} has won this round".format(self.lastRoundWinner))
        else:
            print("it was a draw the round will be counted form the total game played")
        self.get_game_winner()

# d = {0: "Scissors", 1: "Rock", 2: "Paper"}
# n = int(input())
# # n = 100000
# r = Rock_Paper_Scissors(n)
# while r.gameOn:
# #     r.playAround(d[random.randint(0, 2)])
#     r.playAround(d[int(input())])
