from tictactoe.game import Game
from log.gamelogger import GameLogger
from tictactoe.player import Player
from tictactoe.iotput import IOutput
import sys


menu_options = {
    1: "Play game!",
    2: "Watch logs",
    3: "Clean up logs",
    4: "Exit",
}


def print_menu():
    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def main():
    while True:
        print_menu()
        try:
            val = int(input("Enter number of an option: "))
            if val not in ([i + 1 for i in range(4)]):
                print("Choose options fron 1 to 4!")
                continue
        except ValueError:
            print("Choose options fron 1 to 4!")
            continue
        else:
            if val == 1:
                iotput = IOutput()
                player1 = Player(input("Enter 1st player name(more than 2 letters): "))
                player2 = Player(input("Enter 2nd player name(more than 2 letters): "))
                names = [player1.name, player2.name, "friendship"]
                while True:
                    game = Game(x_player=player1, o_player=player2, iotput=iotput)
                    b = game.return_winner(game.game_flow())
                    gamelogger = GameLogger(result=b)
                    while True:
                        answer = input("Wanna play again?(y/n): ").lower()
                        if answer not in ("y", "n"):
                            print("ONLY y OR n!")
                            continue
                        else:
                            break
                    if answer == "y":
                        continue
                    elif answer == "n":
                        gamelogger.count_victories(names)
                        print("See you next ✨time✨!")
                        break
            elif val == 2:
                try:
                    gamelogger.read()
                except UnboundLocalError:
                    gamelogger = GameLogger()
                    gamelogger.read()
            elif val == 3:
                try:
                    gamelogger.flush()
                except UnboundLocalError:
                    print("You can't flush file without reading!")
                    continue
            elif val == 4:
                sys.exit("✨Bye!✨")


if __name__ == "__main__":
    main()
