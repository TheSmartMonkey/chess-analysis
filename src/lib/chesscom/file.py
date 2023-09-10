import json
import os
from typing import List, cast

from models.chessscom_model import ChesscomParsedGames


def init_chesscom_pgn_file() -> List[ChesscomParsedGames]:
    json_file: str = [
        filename for filename in os.listdir(".") if filename.startswith("chesscom")
    ][0]
    with open(json_file, "r", encoding="utf8") as file:
        data = json.load(file)

    return cast(List[ChesscomParsedGames], data["parsedGames"])
