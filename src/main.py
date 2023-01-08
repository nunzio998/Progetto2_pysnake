import json

import numpy as np
from PIL import Image
from FileReader import *
from gameField import GameField


def play(game_file: str) -> int:
    """

    :param game_file: str, path relativo del file in formato .json contenente le informazioni sulla partita
    :return: int, lunghezza finale del corpo del serpente
    """

    # SETUP
    game = open(game_file)
    game_dict = json.load(game)
    # import dynamic gameField from .png or .json
    factory = FileReaderFactory()
    # Utilizza il metodo create_reader() della factory per ottenere un'istanza della classe concreta appropriata
    reader = factory.create_reader(game_dict['field_in'])
    # Utilizza il metodo read_file() dell'oggetto reader per leggere il contenuto del file
    input_field = reader.read_file()
    # import moves
    moves = game_dict['moves'].split()
    #print(f"il numero di mosse totali è {len(moves)}")

    # GAME
    gameField = GameField(input_field, game_dict['start'])
    # for each move
    for i, move in enumerate(moves):
        try:
            if not gameField.step(move):
                break
        except ValueError as message:
            print(f"*** errore nella mossa numero {i+1}: {move} *** {message}")
    #print(f"Il gioco è terminato alla mossa numero {i + 1}")

    # OUT
    im = Image.fromarray(gameField.field)
    im.save(game_dict["field_out"])
    return gameField.snake.get_length()


# SIMULAZIONE
"""
print(f"--------------------------------------------------\nSIMULAZIONE:\n"
      f"la lunghezza finale è {play('data/gamefile_02.json')}")
"""
