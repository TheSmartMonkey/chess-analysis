import os
import json


pgn_file = [filename for filename in os.listdir('.') if filename.startswith("lichess")][0]

with open(pgn_file, "r") as file:
    lines = file.read().splitlines()

print(lines[0])

