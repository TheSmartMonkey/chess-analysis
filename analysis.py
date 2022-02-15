import json
import operator


NUMBER_OF_MOVES = 7
NUMBER_OF_GAMES_SHOWED = 20
NUMBER_OF_OPENINGS_SHOWED = 8


def analyse_pgn(game_data: json):
    count_pgn = __count_same_pgn(game_data)
    sort_pgn = __sort_by_most_played(count_pgn)
    print("\nMost common lines:")
    for pgn in sort_pgn[:NUMBER_OF_GAMES_SHOWED]:
        print(f"{pgn[1]} games: {pgn[0]}")


def openings_stats(game_data: json):
    count_opening = __count_same_key(game_data, "opening")
    sort_opening = __sort_by_most_played(count_opening)
    print("\nMost played openings:")
    for opening in sort_opening[:NUMBER_OF_OPENINGS_SHOWED]:
        print(f"{opening[1]} games: {opening[0]}")


def result_stats(game_data: json):
    count_result = __count_same_key(game_data, "result")
    sort_result = __sort_by_most_played(count_result)
    print("\nPlayed result:")
    for result in sort_result:
        print(f"{result[0]}: {result[1]}")

    d = dict(sort_result)
    total = d['win'] + d['lose'] + d['equal']
    print(f"\nwin: {round((d['win'] / total) * 100, 2)}%")
    print(f"lose: {round((d['lose'] / total) * 100, 2)}%")
    print(f"equal: {round((d['equal'] / total) * 100, 2)}%")


def __count_same_pgn(game_data: list) -> json:
    data = {}
    all_pgn_list = __all_pgn_to_list(game_data)
    for index in range(NUMBER_OF_MOVES, len(all_pgn_list)):
        for pgn_list in all_pgn_list:
            pgn_length = len(pgn_list)
            if pgn_length >= index:
                pgn = __list_to_pgn(pgn_list[:index])
                if pgn not in data:
                    data[pgn] = 1
                else:
                    data[pgn] += 1

    return data


def __all_pgn_to_list(game_data: list) -> list:
    data = []
    for game in game_data:
        items = __pgn_to_list(game["pgn"])
        data.append(items)

    return data


def __pgn_to_list(pgn: str) -> list:
    pgn_split = pgn.split()
    return [item for item in pgn_split if "." not in item and "1-0" not in item and "0-1" not in item]


def __list_to_pgn(game: list) -> list:
    pgn = ""
    move_number = 1
    for index, move in enumerate(game):
        if index % 2 == 0:
            pgn += f"{move_number}. "
            move_number += 1

        pgn += f"{move} "

    return pgn


def __count_same_key(game_data: list, key: str) -> json:
    data = {}
    for game in game_data:
        if game[key] not in data:
            data[game[key]] = 1
        else:
            data[game[key]] += 1

    return data


def __sort_by_most_played(count: json) -> list:
    items = count.items()
    return sorted(items, key=operator.itemgetter(1), reverse=True)


if __name__ == "__main__":
    with open("games.json", "r") as file:
        data = json.load(file)

    result_stats(data)
    openings_stats(data)
    analyse_pgn(data)
