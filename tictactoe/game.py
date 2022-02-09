from tictactoe.player import Turn


class Game(object):
    def __init__(self, x_player=None, o_player=None, iotput=None):
        self.board = [[" " for j in range(3)] for i in range(3)]
        self.x_player = x_player
        self.o_player = o_player
        self.iotput = iotput
        self.is_x_turn = True

    def check_winning_set(self, iterable):
        unique = set(iterable)
        return " " not in unique and len(unique) == 1

    def check_winner(self):
        for row in self.board:
            if self.check_winning_set(row):
                return row[0]

        for column in [*zip(*self.board)]:
            if self.check_winning_set(column):
                return column[0]

        size = len(self.board)
        major_diagonal = [self.board[i][i] for i in range(size)]
        if self.check_winning_set(major_diagonal):
            return major_diagonal[0]

        minor_diagonal = [self.board[i][size - i - 1] for i in range(size)]
        if self.check_winning_set(minor_diagonal):
            return minor_diagonal[0]

    def is_board_empty(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def is_game_over(self):
        winner = self.check_winner()
        if winner is not None:
            return winner
        return self.is_board_empty()

    def make_turn(self, turn: Turn, taken_cell):
        self.board[turn.i][turn.j] = taken_cell
        self.is_x_turn = not self.is_x_turn

    def show_board(self):
        self.iotput.show_board(self.board)

    def show_winner(self, winner):
        if winner == "X":
            self.iotput.show_winner(self.x_player.name)
        elif winner == "O":
            self.iotput.show_winner(self.o_player.name)
        else:
            self.iotput.show_winner()

    def return_winner(self, winner):
        if winner == "X":
            return self.x_player.name
        elif winner == "O":
            return self.o_player.name
        else:
            return "friendship"

    def game_flow(self):
        self.show_board()
        while not self.is_game_over():
            if self.is_x_turn:
                turn = self.x_player.get_turn(self.board)
                taken_cell = "X"
            else:
                turn = self.o_player.get_turn(self.board)
                taken_cell = "O"
            self.make_turn(turn, taken_cell)
            self.show_board()
        winner = self.is_game_over()
        self.show_winner(winner)
        return winner
