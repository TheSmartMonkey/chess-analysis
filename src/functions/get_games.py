from typing import List, Union

from lib.chesscom.data import create_chesscom_games_json_file
from lib.chesscom.file import init_chesscom_pgn_file
from models.chess_model import ChessColors

from models.chessscom_model import ChesscomParsedGames
from src.lib.lichess.data import create_lichess_games_json_file
from src.lib.lichess.file import init_lichess_pgn_file
from src.models.platform_model import Plateform


def get_games(game: Plateform, chessColors: ChessColors) -> Union[List[str], List[ChesscomParsedGames]]:
    if game.value == Plateform.LICHESS.value:
        pgn_data = init_lichess_pgn_file()
        create_lichess_games_json_file(pgn_data)
        return pgn_data

    if game.value == Plateform.CHESSCOM.value:
        pgn_data = init_chesscom_pgn_file()
        create_chesscom_games_json_file(pgn_data, chessColors)
        return pgn_data

    return []
