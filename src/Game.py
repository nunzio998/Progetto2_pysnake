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
    check_start: esegue un controllo sulle condizioni iniziali della partita
    run: gestisce la partita
    get_game_state_2D:
    dynamic_play:

    """

    def __init__(self, field: Field, snake: Snake, moves: list):
        self.field = field
        self.snake = snake
        self.moves = moves

    @classmethod
    def check_start(cls, field: Field, snake: Snake) -> bool:
        """
        Metodo che esegue un controllo sulle condizioni iniziali della partita, in particolare:
            * se start è su cibo: snake "mangia" subito, risultando con lunghezza 2 e con body costituito da due
                posizioni uguali tra loro e pari alla posizione di start
            * se start è su una casella contenente un ostacolo: snake "muore" subito con lunghezza 1
            * se start è fuori dal campo: snake "muore" subito con lunghezza 1

        :param field: Field
                    Campo da gioco sul quale si sta giocando
        :param snake: Snake
                    Serpente con cui si sta giocando
        :return: bool
                    True se a causa delle condizioni iniziali il serpente muore immediatamente
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
        Metodo che gestisce la partita. In particolare:
         - esegue il check delle condizioni iniziali
         - per ogni mossa della partita, esegue la valutazione dello spostamento del serpente e controlla l'esito
            di tale mossa, richiedendo l'esecuzione delle operazioni corrispondenti ad essa.

        :param: dynamic_play: bool
                    True se è richiesta la visualizzazione dinamica della partita, False altrimenti
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
        :return: current_field
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
        """
        Metodo che crea e aggiorna un' immagine per la visualizzazione dinamica della partita
        :return:
        """
        image = FieldConverter(Game.get_game_state_2D(self)).int_to_RGB()
        plt.ion()  # Attiva l'interactive mode
        plt.imshow(image)  # Visualizza l'immagine
        plt.show()  # Mostra la finestra con l'immagine
        plt.draw()  # Forza il ridisegno della finestra
        plt.pause(0.01)  # Aspetta 0.01 secondi e aggiorna l'immagine



