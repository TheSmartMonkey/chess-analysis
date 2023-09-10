import json
import operator
from typing import Dict, List, Tuple, TypedDict, Union, cast
from src.lib.pgn import list_to_pgn, pgn_to_list

from src.models.game_model import CountGames, Game

NUMBER_OF_MOVES = 7
NUMBER_OF_GAMES_SHOWED = 20
NUMBER_OF_OPENINGS_SHOWED = 8


def analyse_pgn(game_data: List[Game]) -> None:
    count_pgn = __count_same_pgn(game_data)
    sort_pgn = __sort_by_most_played(count_pgn)
    print("\nMost common lines:")
    for pgn in sort_pgn[:NUMBER_OF_GAMES_SHOWED]:
        print(f"{pgn[1]} games: {pgn[0]}")


def openings_stats(game_data: List[Game]) -> None:
    count_opening = __count_same_key(game_data, "opening")
    sort_opening = __sort_by_most_played(count_opening)
    print("\nMost played openings:")
    for opening in sort_opening[:NUMBER_OF_OPENINGS_SHOWED]:
        print(f"{opening[1]} games: {opening[0]}")


def result_stats(game_data: List[Game]) -> None:
    count_result = __count_same_key(game_data, "result")
    sort_result = __sort_by_most_played(count_result)
    print("\nPlayed result:")
    for result in sort_result:
        print(f"{result[0]}: {result[1]}")

    d = dict(sort_result)
    total = d["win"] + d["lose"] + d["equal"]
    print(f"\nwin: {round((d['win'] / total) * 100, 2)}%")
    print(f"lose: {round((d['lose'] / total) * 100, 2)}%")
    print(f"equal: {round((d['equal'] / total) * 100, 2)}%")


def __count_same_pgn(game_data: list) -> Dict[str, int]:
    data: Dict[str, int] = {}
    all_pgn_list = __all_pgn_to_list(game_data)
    for index in range(NUMBER_OF_MOVES, len(all_pgn_list)):
        for pgn_list in all_pgn_list:
            pgn_length = len(pgn_list)
            if pgn_length >= index:
                pgn = list_to_pgn(pgn_list[:index])
                if pgn not in data:
                    data[pgn] = 1
                else:
                    data[pgn] += 1

    return data


def __all_pgn_to_list(game_data: list) -> list:
    data = []
    for game in game_data:
        items = pgn_to_list(game["pgn"])
        data.append(items)

    return data


def __count_same_key(game_data: List[Game], key: str) -> CountGames:
    data: CountGames = cast(CountGames, {})
    for game in game_data:
        if game[key] not in data:
            data[game[key]] = 1
        else:
            data[game[key]] += 1

    return data


def __sort_by_most_played(count: Union[Dict[str, int], CountGames]) -> List[Tuple[str, int]]:
    items = count.items()
    return sorted(items, key=operator.itemgetter(1), reverse=True) # type: ignore
