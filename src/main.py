import json
from FileReader import *

# Crea un'istanza della classe FileReaderFactory
factory = FileReaderFactory()

# Utilizza il metodo create_reader() della factory per ottenere un'istanza della classe concreta appropriata
reader = factory.create_reader('data/field_03.png')

# Utilizza il metodo read_file() dell'oggetto reader per leggere il contenuto del file
input_field = reader.read_file()

# Visualizza il campo di partenza
print(input_field)


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