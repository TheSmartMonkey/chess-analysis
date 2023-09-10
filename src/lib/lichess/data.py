import json
from typing import List


def create_lichess_games_json_file(pgn_data: List[str]) -> None:
    opening_name = __get_opening_name(pgn_data)
    result = __get_game_result(pgn_data)
    pgn = __get_pgn(pgn_data)

    data = [
        {"opening": opening_name[index], "result": result[index], "pgn": pgn[index]}
        for index in range(len(pgn))
    ]

    with open("games.json", "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)


def __get_opening_name(pgn_data: List[str]) -> List[str]:
    return [
        line.replace('[Opening "', "").replace('"]', "")
        for line in pgn_data
        if line[:8] == "[Opening"
    ]


def __get_game_result(pgn_data: List[str]) -> List[str]:
    data: List[str] = []
    for line in pgn_data:
        if line[:2] == "1.":
            pgn_split = line.split()
            result = pgn_split[-1]
            if result == "1-0":
                data.append("win")
            elif result == "1/2-1/2":
                data.append("equal")
            else:
                data.append("lose")

    return data


def __get_pgn(pgn_data: List[str]) -> List[str]:
    return [line for line in pgn_data if line[0] == "1"]
