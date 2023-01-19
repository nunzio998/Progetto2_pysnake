from Snake import Snake
from field import Field


class Game:
    """
    Classe che gestisce una partita del gioco Snake.

    Attributi:
    field: Field, il campo da gioco
    snake: Snake, il serpente
    moves: list of ints, la lista di mosse che rappresentano la partita

    Metodi:
    run: gestisce la partita
    check_start: esegue un controllo sulle condizioni iniziali della partita
    """

    def __init__(self, field: Field, snake: Snake, moves: list):
        self.field = field
        self.snake = snake
        self.moves = moves

    @classmethod
    def check_start(cls, *args) -> bool:  # rivedere parametri di ingresso
        """
        Metodo che esegue un controllo sulle condizioni iniziali della partita.
            * se start è su cibo: snake mangia subito
            * se start è su ostacolo: snake muore subito con lunghezza 1
            * se start è fuori dal campo: snake muore subito con lunghezza 1

        Se il serpente muore subito restituisce True
        :return:
        """
        pass

    def run(self) -> int:
        """
        Metodo che gestisce la partita.
        ...

        :return: int, lunghezza finale del serpente
        """
        if Game.check_start():  # aggiungere parametri di ingresso
            return -1  # rivedere il return, deve restituire la lunghezza finale del serpente

        # continue
        pass
