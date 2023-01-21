from Snake import Snake
from Field import Field
from FieldConverter import FieldColor


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
    def check_start(cls, field, snake) -> bool:
        """
        Metodo che esegue un controllo sulle condizioni iniziali della partita.
            * se start è su cibo: snake mangia subito
            * se start è su ostacolo: snake muore subito con lunghezza 1
            * se start è fuori dal campo: snake muore subito con lunghezza 1

        Se il serpente muore subito restituisce True

        :param field: Campo da gioco sul quale si sta giocando
        :param snake: Serpente con cui si sta giocando
        :return:
        """
        size = field.get_size()  # dimensioni del campo
        start = snake.get_head()  # posizione iniziale del serpente
        if 0 <= start[0] < size[0] and 0 <= start[1] < size[1]:  # se start è all'interno del campo da gioco
            what_in_start = field.get_value(start)
            match what_in_start:
                case FieldColor.FOOD.value:
                    snake.eat(start)
                case FieldColor.BLOCK.value:
                    return True
            return False  # se in start c'è campo vuoto o cibo, si continua a giocare
        return True  # se start è al di fuori del campo da gioco

    def run(self):
        """
        Metodo che gestisce la partita.
        ...

        :return:
        """
        if Game.check_start(self.field, self.snake):
            return
        # per ogni mossa
        for move in self.moves:
            head = self.snake.get_head()
            next_pos, elem = self.field.next_pos(tuple(head), move)
            # valuta l'esito della mossa e la fa eseguire al serpente
            match elem:
                case FieldColor.EMPTY.value:
                    if self.snake.intersects(next_pos):
                        return
                    else:
                        self.snake.move(next_pos)
                case FieldColor.FOOD.value:
                    if self.snake.intersects(next_pos):
                        return
                    else:
                        self.snake.eat(next_pos)
                        self.field.remove(next_pos)
                case _:
                    return
        return
