from Field import Field
from FieldConverter import FieldConverter
from FieldFileReader import FieldReaderFactory
from Game import Game
from GameFileReader import GameFileReader
from MovesMapper_classes import MovesMapper
from PNGFileMaker import PNGFileMaker
from Snake import Snake

# La variabile è impostata come globale per non alterare la signature della funzione play.
dynamic_play = False


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

    # mosse dal gamefile
    moves = gameFile.getMoves()

    # Conversione mosse
    moves_mapped = MovesMapper().moves_to_numbers(moves)

    # Creo l'oggetto Game e gli passo Field, Snake e moves
    game = Game(field, snake, moves_mapped)

    # Faccio partire il gioco col metodo run() di Game
    game.run(dynamic_play=dynamic_play)

    # Converto il field finale in RGB prima di salvarlo nel file di output
    field_3d = FieldConverter(game.get_game_state_2D()).int_to_RGB()

    # Salvo il risultato nel file finale
    PNGFileMaker.write_file(gameFile.getFieldOut(), field_3d)

    return snake.get_lenght()


# Quando specifico
if __name__ == "__main__":
    user_input = input("Inserire il nome del file di gioco: ")
    dynamic_mode = input("Vuoi eseguire in modalità dinamica? (y/[n]) ")
    if dynamic_mode == "y" or dynamic_mode == "yes" or dynamic_mode == "Y":
        dynamic_play = True
    play(user_input)
    print("ESECUZIONE TERMINATA.")
