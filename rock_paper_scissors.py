#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    '#making the list of moves, a class variable'
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        '#Initialising a list of moves to be used'
        '#by the CyclePlayer subclass as a reference'
        self.my_move = self.moves
        '#random choice for the first round to be used'
        '#by both ReflectPlayer and CycelPlayer subclasses'
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        '#Stores both players move to be used by the other one'
        '#in case both players are non-human players'
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        '#The Player class objects always play rock'
        return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        '#Plays a random move'
        return random.choice(self.moves)


class HumanPLayer(Player):
    def move(self):
        '#Takes human player input and returnes it as their move'
        while True:
            response = input('Rock, paper, scissors? > ').lower()
            if response in self.moves:
                return response


class ReflectPlayer(Player):
    def move(self):
        '#returns the learned opponent move for'
        '#each round that plays after the first round'
        return self.their_move


class CyclePlayer(Player):
    '#Cycles through a list of pre-defined moves'
    '#based on the position of the said move in the list'
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        '#intitilising player scores as instance variables'
        '#so they can be updated with each iteration of play_round()'
        self.p1_Score = 0
        self.p2_Score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1}  Opponent played: {move2}")
        if beats(move1, move2) is True:
            print('**You win**')
            self.p1_Score += 1
        elif beats(move2, move1) is True:
            print('**Opponent wins**')
            self.p2_Score += 1
        else:
            print('**TIE**')
        print(f'Score: You: {self.p1_Score} Opponent: {self.p2_Score}')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    '#putting a human player against a random choice'
    '#of three other non-human subclasses of players'
    game = Game(HumanPLayer(), random.choice(
        [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
