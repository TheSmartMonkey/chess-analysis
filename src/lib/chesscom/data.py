import json
import re
from typing import List

from models.chessscom_model import ChesscomParsedGames


def create_chesscom_games_json_file(
    chesscom_parsed_games: List[ChesscomParsedGames],
) -> None:
    result = __get_game_result(chesscom_parsed_games)
    pgn = __get_pgn(chesscom_parsed_games)

    data = [
        {
            "opening": chesscom_parsed_games[index]["opening"],
            "result": result[index],
            "pgn": pgn[index],
        }
        for index in range(len(chesscom_parsed_games))
    ]

    with open("games.json", "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)


def __get_game_result(chesscom_parsed_games: List[ChesscomParsedGames]) -> List[str]:
    data: List[str] = []
    for game in chesscom_parsed_games:
        result = game["result"]
        if result in ["win", "checkmated"]:
            data.append("win")
        elif result in ["agreed", "stalemate", "repetition"]:
            data.append("equal")
        else:
            data.append("lose")

    return data


def __get_pgn(chesscom_parsed_games: List[ChesscomParsedGames]) -> List[str]:
    pgns: List[str] = []
    for game in chesscom_parsed_games:
        pgn = game["pgn"]
        pgn = pgn[pgn.find("\n\n") :]  # Remove description
        pgn = pgn.replace("\n", "")
        pgn = re.sub("{.+?}", "", pgn)  # Remove time annotations
        pgn = re.sub(r"\d+\.\.\. ", "", pgn)
        pgns.append(pgn)

    return pgns
