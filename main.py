import json

from src.functions.analysis import analyse_pgn, openings_stats, result_stats
from src.functions.get_games import get_games
from src.models.platform_model import Plateform


def init_games():
    pgn_data = get_games(Plateform.LICHESS)
    print("pgn_data: ", pgn_data)


def init_analysis():
    with open("games.json", "r") as file:
        data = json.load(file)

    result_stats(data)
    openings_stats(data)
    analyse_pgn(data)


if __name__ == "__main__":
    # init_games()
    init_analysis()
