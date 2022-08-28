from player import RendomComputerPlayer, HumanPlayer
import time
import math

class TicTocToe():
    def __init__(self):
        self.board = [' ' for i in range (9)]
        self.current_winner = None


    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_number():
        board_number = [[str(i) for i in range(j*3, (j+1)*3)] for j in range (3)]
        for row in board_number:
            print("| " + " | ".join(row) + " |")

    def avaluable_move(self):
        #moves = []
        #for i, spot in enumerate(self.board):# enumarate creat a list with tuples with index i and value spot
        #    if spot == " ":
         #       moves.append(i)
        #return moves
        return [i for i, spot in enumerate(self.board) if spot==" "] # the same code but in one line

    def empty_squares(self):
        return ' ' in self.board

    def  num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        row_ind= math.floor(square /3)
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all( [spot == letter for spot in row]):
            return True
        col_ind = square % 3
        colum = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in colum]):
            return True
        if square % 2 == 0:
            diagonl1 = [self.board[i] for i in [0, 4, 8]]
            if all( [spot ==letter for spot in diagonl1]):
                return True
            diagonl2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonl2]):
                return True
        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_number()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' letter made move to square {square}')
                game.print_board()
                print(" ")
            if game.current_winner:
                if print_game:
                    print(letter + f' wins')
                return letter
            letter = 'O' if letter == 'X' else 'X'  # the same code in one line
       # if letter =='X':
        #    letter = 'O'
        #else:
        #    letter = 'X'
        time.sleep(.8)
    if print_game:
        print("it's a tie")
if __name__ == '__main__':
    x_player = HumanPlayer("X")
    o_player = RendomComputerPlayer("O")
    t = TicTocToe()
    play(t, o_player, x_player, print_game =True)



