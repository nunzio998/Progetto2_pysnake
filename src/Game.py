from Snake import Snake
from field import Field
from FieldConverter import FieldColor
import numpy as np


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

        # per ogni mossa
        for move in self.moves:
            head = self.snake.get_head()
            next_pos, elem = self.field.next_pos(tuple(head), move)
            # valuta l'esito della mossa e la fa eseguire al serpente
            match elem:
                case FieldColor.EMPTY.value:
                    successful_move = self.snake.move(next_pos)
                    if not successful_move:
                        return self.snake.lenght
                case FieldColor.FOOD.value:
                    successful_eat = self.snake.eat(next_pos)
                    if not successful_eat:
                        return self.snake.lenght
                case _:
                    print("Il gioco è terminato")
                    return self.snake.lenght

