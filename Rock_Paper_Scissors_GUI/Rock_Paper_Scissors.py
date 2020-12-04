import random


class Rock_Paper_Scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.computerWins = 0
        self.humanWins = 0
        self.roundsPlayed = 0
        self.roundsLeft = self.rounds - self.roundsPlayed
        self.humanChoice = None
        self.computerChoice = None
        self.order = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        self.gameOn = True
        self.lastRoundWinner = ""
        if self.rounds <= 0:
            self.get_game_winner()

    def get_round_winner(self):
        if self.order[self.humanChoice] == self.computerChoice:
            self.humanWins += 1
            self.lastRoundWinner = "Human"
        elif self.order[self.computerChoice] == self.humanChoice:
            self.computerWins += 1
            self.lastRoundWinner = "Computer"
        else:
            self.lastRoundWinner = "Draw"
        self.roundsPlayed += 1
        self.roundsLeft -= 1

    def get_game_winner(self):
        if abs(self.humanWins - self.computerWins) >= self.roundsLeft + 1 >= 1:
            if self.humanWins > self.computerWins:
                print("The human has won the game")
                self.gameOn = False
                return "Human"
            elif self.humanWins < self.computerWins:
                print("The computer has won the game")
                self.gameOn = False
                return "Computer"
        elif self.roundsLeft <= 0:
            print("The game was a draw no one won")
            self.gameOn = False
            return "Draw"

    def _get_computer_choice(self):
        d = {0: "Scissors", 1: "Rock", 2: "Paper"}
        x = random.randint(0, 2)
        self.computerChoice = d[x]

    def play_a_round(self, choice):
        self.humanChoice = choice
        self._get_computer_choice()
        self.get_round_winner()
        if self.lastRoundWinner != "Draw":
            print("Computer choose {}".format(self.computerChoice))
            print("{} has won this round".format(self.lastRoundWinner))
        else:
            print("it was a draw the round will be counted form the total game played")
        self.get_game_winner()
