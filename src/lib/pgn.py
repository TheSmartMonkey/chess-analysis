from typing import List


def pgn_to_list_of_moves(pgn: str) -> List[str]:
    pgn_split = pgn.split()
    return [
        item
        for item in pgn_split
        if "." not in item and "1-0" not in item and "0-1" not in item
    ]


def list_of_moves_to_pgn(game: List[str]) -> str:
    pgn = ""
    move_number = 1
    for index, move in enumerate(game):
        if index % 2 == 0:
            pgn += f"{move_number}. "
            move_number += 1

        pgn += f"{move} "

    return pgn
