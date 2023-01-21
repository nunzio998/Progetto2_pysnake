import json

from src.Field import Field
from src.FieldConverter import FieldConverter
from src.FieldFileReader import FieldReader, FieldReaderFactory
from src.Game import Game
from src.GameFileReader import GameFileReader
from src.Snake import Snake


def play(game_file: str) -> int:
    # scrivi qui il tuo codice

    # Leggo il file di gioco
    gameFile = GameFileReader(game_file)

    # Leggo il file del campo da gioco
    field_array_3d = FieldReaderFactory.create_reader(gameFile.getFieldIn()).read_file()

    # Converto l'array che contiene il campo da gioco 3d in un array 2d
    field_2d = FieldConverter(field_array_3d).RGB_to_int()

    # Creo l'oggetto Field
    field = Field(field_2d)

    # Creo l'oggetto Snake
    snake = Snake(gameFile.getStart())

    # Creo l'oggetto Game e gli passo Field, Snake e moves
    game = Game(field, snake, gameFile.getMoves())

    # Faccio partire il gioco col metodo run() di Game
    game.run()

    return snake.get_lenght()
