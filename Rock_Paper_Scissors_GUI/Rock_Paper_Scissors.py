# CSE313 HW Assignment 1
#
# Topic: OOP and design patterns
# Author : Fadi Alahmad ALomar 120180049
# Date : 06/12/2020
# a backend implementing the logic of the game rock paper scissors


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
        # a dictionary used to indicate who wins as each key beats it is value
        self.order = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        self.gameOn = True
        self.lastRoundWinner = ""
        if self.rounds <= 0:
            self.get_game_winner()

    def get_round_winner(self):
        """
        this function changes the parameter lastRoundWinner according to the winner it does that by checking to see
        if the computer choice/human choice is the key to the others choice in the dictionary order
        as this indicates the key beats it is value. thus if we check for this twice but each time changing the order
        we can find out who won and if both times the others choice is not the value of the key then the game is a
        draw
        :return:
        """
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
        """
        this function checks to see if the game has ended and prints\returns the winner
        :return: str
        """
        # if the difference between the scores is bigger or equal to the rounds left + 1 then we have a winner
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
        """
        this function change the parameter computerChoice according to the output of the random function
        :return:
        """
        d = {0: "Scissors", 1: "Rock", 2: "Paper"}
        x = random.randint(0, 2)
        self.computerChoice = d[x]

    def play_a_round(self, choice):
        """
        this function plays a round it takes Rock,Paper and Scissors as the parameter choice
        :param choice: str
        :return:
        """
        self.humanChoice = choice
        self._get_computer_choice()
        self.get_round_winner()
        if self.lastRoundWinner != "Draw":
            print("Computer choose {}".format(self.computerChoice))
            print("{} has won this round".format(self.lastRoundWinner))
        else:
            print("it was a draw the round will be counted form the total game played")
        self.get_game_winner()
