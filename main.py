import json

from src.functions.analysis import analyse_pgn, openings_stats, result_stats
from src.functions.get_games import get_games
from src.models.platform_model import Plateform


def init_games(plateform: Plateform) -> None:
    get_games(plateform)


def init_analysis() -> None:
    with open("games.json", "r") as file:
        data = json.load(file)

    result_stats(data)
    openings_stats(data)
    analyse_pgn(data)


if __name__ == "__main__":
    init_games(Plateform.CHESSCOM)
    init_analysis()
