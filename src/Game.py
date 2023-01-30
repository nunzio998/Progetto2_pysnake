from matplotlib import pyplot as plt

from Field import Field
from FieldConverter import FieldColor, FieldConverter
from Snake import Snake


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

    def run(self, dynamic_play: bool):
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
            if dynamic_play:
                Game.dynamic_play(self)
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
                case FieldColor.SNAKE_TRAIL.value:
                    if self.snake.intersects(next_pos):
                        return
                    else:
                        self.snake.move(next_pos)
                case _:
                    return
        return

    def get_game_state_2D(self):
        """
        Metodo che serve a visualizzare dinamicamente la partita
        come si sta evolvendo.
        :return:
        """
        # Crea un'immagine con la situazione del campo corrente senza snake
        current_field = self.field.get_field()

        # Inserisci trail e snake
        for [row, col] in self.snake.get_trail():
            # Colora la scia del serpente di grigio
            current_field[row, col] = FieldColor.SNAKE_TRAIL.value
        for [row, col] in self.snake.get_body():
            # Colora il corpo del serpente di verde
            current_field[row, col] = FieldColor.SNAKE.value
        return current_field

    def dynamic_play(self):
        image = FieldConverter(Game.get_game_state_2D(self)).int_to_RGB()
        plt.ion()  # Attiva l'interactive mode
        plt.imshow(image)  # Visualizza l'immagine
        plt.show()  # Mostra la finestra con l'immagine
        plt.draw()  # Forza il ridisegno della finestra
        plt.pause(0.01)  # Aspetta 0.01 secondi e aggiorna l'immagine



