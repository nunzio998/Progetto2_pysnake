import json


def play(game_file: str) -> int:
    """

    :param game_file: str, path relativo del file in formato .json contenente le informazioni sulla partita
    :return: int, lunghezza finale del corpo del serpente
    """

# SETUP
    game = open(game_file)
    game_dict = json.load(game)

    #import dynamic field from .png or .json

    #import moves

# GAME
    #check next move

    #if next move is legal, update dynamic field

    #else end game

# OUT
    return -1

play("data/gamefile_01.json")