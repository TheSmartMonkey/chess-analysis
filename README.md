# chess-analysis

Analyse your own games get some good insights that helps you to improve at chess

## Getting started

### Lichess

1. Go to https://lichess.org/@/{your_name}/download

1. Download you opening file with this include settings

![APP IMAGE](https://github.com/TheSmartMonkey/chess-analysis/blob/main/.github/lichess-import.PNG)

1. Add the file at the root of the project

### Chess.com

1. Go to https://chessinsights.xyz/

1. Enter the players name and export file

1. Add the file at the root of the project

1. Rename the file and put `chesscom_` on front

### Next steps

1. Install pipx : https://pypa.github.io/pipx/

1. Avalable commands with `npm run` (`npm run start` runes your code)

```
start
    py main.py
test
    python -m pipenv run pytest
lint
    python -m pipenv run mypy .
format
    python -m black . && python -m isort -y
format:check
    python -m black --check . && python -m isort --check-only
coverage
    python -m pipenv run pytest --cov --cov-fail-under=90
```

Result exemple :

```
Played result:
win: 105
lose: 58
equal: 5

win: 62.5%
lose: 34.52%
equal: 2.98%

Most played openings:
75 games: Queen's Pawn Game: Mason Variation
32 games: Indian Defense
15 games: Horwitz Defense
7 games: Queen's Pawn Game
5 games: Englund Gambit
5 games: Modern Defense
4 games: Mikenas Defense
3 games: French Defense: Franco-Hiva Gambit 

Most common lines:
8 games: 1. d4 d5 2. Bf4 Nf6 3. e3 e6 4. Bd3 
6 games: 1. d4 d5 2. Bf4 Nc6 3. e3 Bf5 4. c4 
6 games: 1. d4 d5 2. Bf4 Bf5 3. e3 e6 4. c4 
6 games: 1. d4 Nf6 2. Bf4 g6 3. Nc3 Bg7 4. e4 
4 games: 1. d4 d5 2. Bf4 e6 3. e3 Nf6 4. Bd3 
4 games: 1. d4 d5 2. Bf4 Nc6 3. e3 f6 4. Nf3 
4 games: 1. d4 d5 2. Bf4 Nf6 3. e3 Bf5 4. c4 
4 games: 1. d4 d5 2. Bf4 e6 3. e3 Bd6 4. Bg3 
4 games: 1. d4 Nf6 2. Bf4 d6 3. Nc3 g6 4. e4 
4 games: 1. d4 d5 2. Bf4 Nf6 3. e3 c5 4. c3 
4 games: 1. d4 d5 2. Bf4 Nc6 3. e3 Bf5 4. c4 e6         
4 games: 1. d4 d5 2. Bf4 Nf6 3. e3 e6 4. Bd3 c5         
4 games: 1. d4 Nf6 2. Bf4 g6 3. Nc3 Bg7 4. e4 d6        
4 games: 1. d4 d5 2. Bf4 Nf6 3. e3 e6 4. Bd3 c5 5. c3   
4 games: 1. d4 Nf6 2. Bf4 g6 3. Nc3 Bg7 4. e4 d6 5. Qd2 
3 games: 1. d4 d5 2. Bf4 Nc6 3. e3 Nf6 4. Nf3 
3 games: 1. d4 d5 2. Bf4 e6 3. e3 c5 4. c3 
3 games: 1. d4 d5 2. Bf4 e6 3. e3 Bd6 4. Bg3 Bxg3       
3 games: 1. d4 d5 2. Bf4 Nf6 3. e3 Bf5 4. c4 c6         
3 games: 1. d4 d5 2. Bf4 Bf5 3. e3 e6 4. c4 c6 
```

## Current Functionalities

1. Give the most played lines (then you know were to train)

## Upcoming Functionalities

1. Analyse the most common mistakes in the opening

1. Give alternative moves to improve your games

1. Machine leaning (https://github.com/mptedesco/python-chess-analysis)
