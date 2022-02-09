from dataclasses import dataclass
from tictactoe.iotput import IOutput


@dataclass
class Turn:
    i: int
    j: int


class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.iotput = IOutput()

    def get_turn(self, board):
        size = len(board)
        while True:
            index = int(self.iotput.get_input()) - 1
            i = index // size
            j = index % size
            if board[i][j] != " ":
                print("This cell is taken! Choose another one!")
                continue
            else:
                return Turn(i, j)
