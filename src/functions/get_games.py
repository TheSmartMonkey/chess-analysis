from typing import List

from src.lib.lichess.data import create_games_json_file
from src.lib.lichess.file import init_pgn_file
from src.models.platform_model import Plateform


def get_games(game: Plateform) -> List[str]:
    if game == Plateform.LICHESS:
        pgn_data = init_pgn_file()
        create_games_json_file(pgn_data)
        return pgn_data
    return []
