from tictactoe.game import *


class IOutput:
    cell_nums = [str(i + 1) for i in range(9)]

    def show_board(self, board):
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                cell = board[i][j]
                if cell == "X":
                    print("❌", end="┃")
                elif cell == "O":
                    print("🔵", end="┃")
                else:
                    print(self.cell_nums[i * len(row) + j], end=" ┃")
            print()
        print()

    def show_winner(self, name=None):
        if name is None:
            print("✨friendship✨ wins!")
        else:
            print(f"Congrats! ✨{name}✨, you win this game!")

    def get_input(self):
        while True:
            answer = input("Enter number of a cell: ")
            if answer not in ([str(i + 1) for i in range(9)]):
                print("Enter only cell numbers!🤮")
                continue
            else:
                return answer
