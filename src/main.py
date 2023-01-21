import json

from src.Field import Field
from src.FieldConverter import FieldConverter
from src.FieldFileReader import FieldReaderFactory
from src.Game import Game
from src.GameFileReader import GameFileReader
from src.PNGFileMaker import PNGFileMaker
from src.Snake import Snake
from src.movesMapper_classes import MovesMapper


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

    moves = gameFile.getMoves()

    moves_mapped = MovesMapper().moves_to_numbers(moves)

    # Creo l'oggetto Game e gli passo Field, Snake e moves
    game = Game(field, snake, moves_mapped)

    # Faccio partire il gioco col metodo run() di Game
    game.run()

    # Converto il field finale in RGB prima di salvarlo nel file di output
    field_3d = FieldConverter(field.get_field()).int_to_RGB()

    # Salvo il risultato nel file finale
    PNGFileMaker.write_file(gameFile.getFieldOut(), field_3d)

    return snake.get_lenght()
