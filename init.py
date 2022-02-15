import os
import json


def init_pgn_file() -> list:
    pgn_file = [filename for filename in os.listdir(
        ".") if filename.startswith("lichess")][0]
    with open(pgn_file, "r") as file:
        data = file.read().splitlines()

    return __remove_blank_lines(data)


def __remove_blank_lines(pgn_data: list) -> list:
    return [line for line in pgn_data if line != ""]


def create_games_json_file(pgn_data: list):
    opening_name = __get_opening_name(pgn_data)
    result = __get_game_result(pgn_data)
    pgn = __get_pgn(pgn_data)

    data = [{
            "opening": opening_name[index],
            "result": result[index],
            "pgn": pgn[index]
            } for index in range(len(pgn))]

    with open("games.json", "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)


def __get_opening_name(pgn_data: list) -> list:
    return [line.replace("[Opening \"", "").replace("\"]", "") for line in pgn_data if line[:8] == "[Opening"]


def __get_game_result(pgn_data: list) -> bool:
    data = []
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


def __get_pgn(pgn_data: list) -> list:
    return [line for line in pgn_data if line[0] == "1"]


if __name__ == "__main__":
    pgn_data = init_pgn_file()
    create_games_json_file(pgn_data)
