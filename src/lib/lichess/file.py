import os


def init_pgn_file() -> list:
    pgn_file: str = [
        filename for filename in os.listdir(".") if filename.startswith("lichess")
    ][0]
    with open(pgn_file, "r") as file:
        data = file.read().splitlines()

    return __remove_blank_lines(data)


def __remove_blank_lines(pgn_data: list) -> list:
    return [line for line in pgn_data if line != ""]
