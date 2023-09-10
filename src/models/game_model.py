from typing import TypedDict


class Game(TypedDict):
    opening: str
    pgn: str
    result: str


class CountGames(TypedDict):
    win: int
    lose: int
    equal: int
