import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RendomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.avaluable_move())# it choose rendome avaluable spot
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +'\' s turn. Turn your move from(0-9)') # self.letter its a player
            try:
                val = int(square)
                if val not in game.avaluable_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalide square")
                print("test")
        return val



