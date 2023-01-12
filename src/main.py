from FileReader import FileReaderFactory
from SnakeGame import SnakeGame
import json


def play(game_file: str) -> int:
    """
    Classe che riceve un file di gioco e restituisce la dimensione finale del serpente.
    :param game_file: file di gioco
    :return: Dimensione finale del serpente
    """
    with open(game_file, 'r') as f:
        data = json.load(f)

        # Crea un'istanza della classe FileReaderFactory
        factory = FileReaderFactory()

        # Utilizza il metodo create_reader() per ottenere un'istanza della classe concreta appropriata
        reader = factory.create_reader(data['field_in'])

        input_field = reader.read_file()

        # Genera una lista di mosse dalla stringa data['moves']
        moves = data['moves'].split(' ')

        # Crea un'istanza della classe SnakeGame inizializzandola con:
        # - Il campo specificato in data['field_in']
        # - La posizione iniziale del serpente in data['start']
        game_play = SnakeGame(input_field, data['start'])

        for move in moves:
            if game_play.snake_is_alive() and move != '':
                """
                Rimuovere il commento sottostante se si vuole visualizzare dinamicamente il gioco
                """
                # game_play.dynamic_play()
                game_play.move(move)

        # Metodo che archivia un'immagine contenente la situazione finale del gioco
        # sia nel caso in cui sono terminate la mosse sia nel caso il serpente sia morto
        game_play.save_game_state(data['field_out'])

        return game_play.snake_length()


