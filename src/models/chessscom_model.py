from typing import List, TypedDict


class ChesscomParsedGames(TypedDict):
    opening: str
    pgn: str
    result: str
    userColor: str


class Chesscom(TypedDict):
    userName: str
    playerStats: dict  # type: ignore
    openings: str
    parsedGames: List[ChesscomParsedGames]
