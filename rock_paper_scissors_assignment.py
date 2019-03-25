#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players.
The first player is a computer that is selected
at random from predefined profiles. While the second player is a human.
The human player initially choices if they wish
to play a game of best out of 1, 3 or 5.
The programme keeps track of the players'scores and reports them each round."""
import random
import time


moves = ['rock', 'paper', 'scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("Welcome to my Rock, Paper, "
                "Scissors game! You will be facing "
                "against a tough computer "
                "in just a moment. You will be Player 2 in this game.")


def number_game():
    while True:
        n = input("First, would you like to play a game "
                  "of best out of 1, 3 or 5? (please "
                  "enter the digit 1, 3 or 5 to make your choice)\n")
        if n == '1' or n == '3' or n == '5':
            return int(n)
        else:
            print("I don't understand. Please enter an odd either 1, 3 or 5")


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        m = random.choice(moves)
        return m


class HumanPlayer(Player):
    def move(self):
        while True:
            m = input("Do you want to play rock, paper or scissors?\n").lower()
            if m == "rock":
                return moves[0]
            elif m == "paper":
                return moves[1]
            elif m == "scissors":
                return moves[2]
            else:
                print("Sorry I don't understand")


class ReflectPlayer(Player):
    def __init__(self):
        self.move_temp = random.choice(moves)

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.move_temp = random.choice(moves)

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        if my_move == moves[0]:
            self.move_temp = moves[1]
        elif my_move == moves[1]:
            self.move_temp = moves[2]
        elif my_move == moves[2]:
            self.move_temp = moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2, n, score1, score2, counter):
        self.n = n
        self.p1 = p1
        self.p2 = p2
        self.score1 = score1
        self.score2 = score2
        self.counter = counter

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 != move2:
            if beats(move1, move2) is True:
                print("Player 1 wins this round!")
                self.score1.append(1)
                print("Current scores: Player 1: ",
                      len(self.score1), ", Player 2: ",
                      len(self.score2))
            else:
                print("Player 2 wins this round!")
                self.score2.append(1)
                print("Current scores: Player 1: ",
                      len(self.score1), ", Player 2: ",
                      len(self.score2))
        else:
            print("It's a tie!")

    def play_game(self):
        print("Game start!")
        while len(self.score1) < self.n and len(self.score2) < self.n:
            print(f"Round:", len(self.counter))
            self.counter.append(1)
            self.play_round()
        if len(self.score1) > len(self.score2):
            print("Player 1 wins! The final score is: "
                  "Player 1:", len(self.score1),
                  " Player 2:", len(self.score2))
        else:
            print("Player 2 wins! The final score is: "
                  "Player 2:", len(self.score2),
                  " Player 1:", len(self.score1))


if __name__ == '__main__':
    player_type = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    intro()
    game = Game(random.choice(player_type),
                HumanPlayer(), number_game(), [], [], [1])
    game.play_game()
