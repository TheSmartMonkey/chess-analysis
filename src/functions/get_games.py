from typing import List
from src.lib.lichess.file import init_pgn_file
from src.models.games_model import Games


def get_games(game: Games) -> List[str]:
    if game == Games.LICHESS:
        return init_pgn_file()
    return []
