import os.path
from os import path
import tempfile
import logging
from datetime import datetime


class GameLogger:
    def __init__(
        self, result=None, path_to_file=os.path.join(tempfile.gettempdir(), "temp.log")
    ):
        self.path_to_file = path_to_file
        self.result = result
        logging.basicConfig(
            filename=path_to_file,
            filemode="w",
            format="%(asctime)s - %(message)s",
            level=logging.INFO,
        )
        logging.info("%s wins", result)

    def read(self):
        self.path_to_file = "permanent.log"
        if not os.path.exists(self.path_to_file):
            print("Such file doesn`t exist!")
        else:
            with open(self.path_to_file, "r") as f:
                data = f.read()
                print(data)

    def flush(self):
        self.path_to_file = "permanent.log"
        while True:
            answer = input("Are you sure? (y/n): ").lower()
            if answer not in ("y", "n"):
                print("ONLY y OR n!")
                continue
            else:
                if answer == "y":
                    with open(self.path_to_file, "w") as f:
                        f.flush()
                    print("All data is deleted!")
                    break
                elif answer == "n":
                    print("No data is deleted!")
                    break

    def count_victories(self, names):
        line_count = sum(1 for line in open(self.path_to_file))
        flakes = "*" * 50
        with open(self.path_to_file, "r+") as f:
            data = f.read()
        with open("permanent.log", "a") as f:
            if line_count == 1:
                f.write(data)
                f.write(f"{flakes}\n")
            else:
                date_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                for name in names:
                    count_names = data.count(name)
                    if name == "friendship":
                        f.write(f"{date_time}-tie {count_names} time(s)\n")
                    else:
                        f.write(f"{date_time}-{name} wins {count_names} time(s)\n")

                f.write(f"{flakes}\n")
