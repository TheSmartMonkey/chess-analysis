import os
from typing import List


def init_lichess_pgn_file() -> List[str]:
    pgn_file: str = [
        filename for filename in os.listdir(".") if filename.startswith("lichess")
    ][0]
    with open(pgn_file, "r") as file:
        data = file.read().splitlines()

    return __remove_blank_lines(data)


def __remove_blank_lines(pgn_data: List[str]) -> List[str]:
    return [line for line in pgn_data if line != ""]
