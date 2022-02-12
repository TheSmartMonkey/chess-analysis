import os
import json


def init_pgn_file() -> list:
    pgn_file = [filename for filename in os.listdir(
        ".") if filename.startswith("lichess")][0]
    with open(pgn_file, "r") as file:
        lines = file.read().splitlines()

    return __remove_blank_lines(lines)


def __remove_blank_lines(lines) -> list:
    return [line for line in lines if line != ""]


def create_games_json_file(lines):
    opening_name = __get_opening_name(lines)
    # result = __get_game_result(lines)
    pgn = __get_pgn(lines)

    data = [{
            "opening": opening_name[index],
            # "win": result[index],
            "pgn": pgn[index]
            } for index in range(len(pgn))]

    with open("games.json", "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)


def __get_opening_name(lines) -> list:
    return [line.replace("[Opening \"", "").replace("\"]", "") for line in lines if line[:8] == "[Opening"]

# def __get_game_result(lines) -> bool:
#     pass


def __get_pgn(lines) -> list:
    return [line for line in lines if line[0] == "1"]


if __name__ == "__main__":
    lines = init_pgn_file()
    create_games_json_file(lines)
