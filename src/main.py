import json
import os
from abc import abstractmethod, ABC
from enum import Enum

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


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
    game.run(dynamic_play=False)

    # Converto il field finale in RGB prima di salvarlo nel file di output
    field_3d = FieldConverter(game.get_game_state_2D()).int_to_RGB()

    # Salvo il risultato nel file finale
    PNGFileMaker.write_file(gameFile.getFieldOut(), field_3d)

    return snake.get_lenght()


class Snake:
    """
    Classe relativa al serpente. Gli attributi presenti sono in riferimento alla lunghezza, al corpo e alla scia del
    serpente. La classe implementa i metodi che permettono al serpente di muoversi e mangiare cibo, oltre ai vari
    getters.
    """

    def __init__(self, start: tuple):
        self.body = [start]
        self.lenght = 1
        self.trail = []

    def move(self, next_pos: tuple):
        """
        Metodo invocato nel caso in cui il serpente si muove in una casella vuota. Si aggiorna quindi la lista del body
        e della scia, lasciando invece invariata la lunghezza.
        :param next_pos:
        :return:
        """
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa in fondo alla lista.
        if self.body[0] != self.body[1]:
            self.trail.append(self.body[0])  # aggiorno la scia.
        self.body.pop(0)  # elimino l'ultimo punto della coda.

    def eat(self, next_pos: tuple):
        """
        Metodo invocato nel caso in cui il serpente si muove in una casella che contiene il cibo. In questo caso la
        lunghezza viene incrementata e vengono aggiornata la lista relativa al corpo. Non viene quindi effettuato
        il pop del primo elemento della lista body in quando la lunghezza del corpo aumenta.
        :param next_pos:
        :return:
        """
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa.
        self.lenght += 1  # aumento la lunghezza

    # GETTERS:
    def get_head(self):
        return self.body[len(self.body) - 1]

    def get_body(self):
        return self.body

    def get_trail(self):
        return self.trail

    def get_lenght(self):
        return self.lenght

    def intersects(self, next_pos) -> bool:
        """

        :param next_pos:
        :return: True se la mossa porta a intersezione del serpente, False altrimenti
        """
        intersects = False
        head = self.body[-1]
        if next_pos in self.body[1:-1]:
            intersects = True
        if (next_pos[0] - head[0]) * (next_pos[1] - head[1]) != 0:  # se va in diagonale
            # controlla che entrambe le seguenti due caselle non appartengano al body
            to_check1 = [next_pos[0], head[1]]
            to_check2 = [head[0], next_pos[1]]
            if to_check1 in self.body[1:-1] and to_check2 in self.body[1:-1]:
                intersects = True
        return intersects


class Field:
    """
    Classe che definisce il campo da gioco, rappresentato con un numpy.ndarray bidimensionale; il valore di ogni
    elemento indica il contenuto di una casella del campo, in accordo con la codifica stabilita nella classe FieldColor.

    Attributi:
        field: numpy.ndarray, array bidimensionale rappresentante il contenuto delle caselle del campo da gioco;
        ogni casella è identificata dalla sua posizine, rappresentata con una coppia di indici (riga,colonna), in cui:
        - le righe partono da zero e sono crescenti verso il basso
        - le colonne partono da zero e sono crescenti verso destra
        size:  tuple of ints, dimensioni del campo da gioco: (numero righe, numero colonne)

    Metodi:
        get_value: restituisce il valore dell'elemento di posizione specificata in ingresso
        get_size:  restituisce le dimensioni del campo da gioco
        pop_food:  rimuove il cibo presente nella casella specificata in ingresso
        next_pos:  restituisce la posizione e il contenuto della casella risultate da una mossa
    """

    def __init__(self, field: np.ndarray):
        """
        Costruttore che prende in ingresso un array numpy rappresentante il campo e istanzia l'oggetto campo da gioco

        :param field: numpy.ndarray, array numpy rappresentante il campo da gioco
        """
        self.field = field
        self.size = field.shape

    def get_value(self, pos: tuple) -> int:
        """
        Metodo che restituisce il valore della casella del campo di posizione specificata in ingresso. Se la posizione
        indicata in ingresso eccede le dimensioni del campo viene sollevata un'eccezione di tipo IndexError
        :param pos: tuple of ints, identifica una casella del campo
        :return: int
        """
        return self.field[pos[0], pos[1]]

    def get_size(self) -> tuple:
        """
        Metodo che restituisce le dimensioni del campo da gioco (numero righe, numero colonne)
        :return: tuple of ints
        """
        return self.size[0], self.size[1]

    def get_field(self):
        return self.field

    def remove(self, pos: tuple):
        """
        Rimuove un oggetto dal campo portando la casella specificata al valore di casella vuota;
        viene usato per rimuovere il cibo da una casella quando il serpente la attraversa
        :param pos:
        :return:
        """
        self.field[pos[0], pos[1]] = FieldColor.EMPTY.value

    def next_pos(self, init_pos: tuple, move: int) -> tuple:
        """
        Metodo che si occupa di determinare la posizione risultante dall'applicazione di una specifica mossa ad una
        specifica casella di partenza. Restituisce la posizione della casella finale e il suo contenuto.

        :param init_pos: tuple, posizione iniziale dalla quale ci si vuole spostare applicando una mossa [riga,colonna]
        :param move: int, intero rappresentante una delle mosse legali definite nella classe Moves
        :return: tuple, posizione finale e valore: (riga,colonna,valore)
        """
        try:
            self.get_value(init_pos)
        except:
            print("Posizione iniziale non valida, non compresa nei limiti del campo!")
            return -1,
        position = list(init_pos)  # crea un nuovo oggetto di tipo lista
        match move:
            case 0:
                position[0] = position[0] - 1 if position[0] >= 1 else self.size[0] - 1
            case 4:
                position[0] = (position[0] + 1) % self.size[0]
            case 2:
                position[1] = (position[1] + 1) % self.size[1]
            case 6:
                position[1] = position[1] - 1 if position[1] >= 1 else self.size[1] - 1
            case 1:
                position[0] = position[0] - 1 if position[0] >= 1 else self.size[0] - 1
                position[1] = (position[1] + 1) % self.size[1]
            case 7:
                position[0] = position[0] - 1 if position[0] >= 1 else self.size[0] - 1
                position[1] = position[1] - 1 if position[1] >= 1 else self.size[1] - 1
            case 3:
                position[0] = (position[0] + 1) % self.size[0]
                position[1] = (position[1] + 1) % self.size[1]
            case 5:
                position[0] = (position[0] + 1) % self.size[0]
                position[1] = position[1] - 1 if position[1] >= 1 else self.size[1] - 1
        return position, self.field[position[0], position[1]]


class FieldColor(Enum):
    """
    Enum per rappresentare i valori della matrice bidimensionale
    """
    EMPTY = 0  # Campo vuoto
    SNAKE = 1  # Serpente
    SNAKE_TRAIL = 2  # Scia del serpente
    FOOD = 3  # Cibo
    BLOCK = 4  # Ostacolo


class FieldConverter:
    def __init__(self, field_array):
        self.field_array = field_array

    def RGB_to_int(self):
        """
        Converte la matrice tridimensionale in una matrice bidimensionale utilizzando i valori
        RGB delle celle come chiavi per determinare i valori numeri corrispondenti
        """
        # Crea un dizionario per la conversione RGB -> intero
        RGB_to_number_dict = {(0, 0, 0): FieldColor.EMPTY.value,
                              (0, 255, 0): FieldColor.SNAKE.value,
                              (128, 128, 128): FieldColor.SNAKE_TRAIL.value,
                              (255, 128, 0): FieldColor.FOOD.value,
                              (255, 0, 0): FieldColor.BLOCK.value
                              }

        # Sostituisce i valori RGB della matrice tridimensionale con i valori corrispondenti
        # dell'Enum utilizzando il dizionario

        def translate_rgb_to_number(rgb):
            """
            Funzione per effettuare la conversione su ogni elemento dell'array
            :param rgb:
            :return:
            """
            return RGB_to_number_dict.get(tuple(rgb), "Chiave non trovata")

        # Utilizza la funzione per effettuare la conversione sull'array tridimensionale
        numpy_array_2d = np.apply_along_axis(translate_rgb_to_number, 2, self.field_array)

        # restituisce l'array 2D
        return numpy_array_2d

    def int_to_RGB(self):
        """
        Converte la matrice bidimensionale in una matrice tridimensionale utilizzando i valori
        numerici delle celle come chiavi per determinare i valori RGB corrispondenti
        """
        # Crea un dizionario per la conversione intero -> RGB
        number_to_RGB_dict = {FieldColor.EMPTY.value: (0, 0, 0),
                              FieldColor.SNAKE.value: (0, 255, 0),
                              FieldColor.SNAKE_TRAIL.value: (128, 128, 128),
                              FieldColor.FOOD.value: (255, 128, 0),
                              FieldColor.BLOCK.value: (255, 0, 0)
                              }

        # Crea una matrice vuota con le stesse dimensioni dell'array 2D originale
        field_array_3d = np.empty(self.field_array.shape + (3,), dtype=np.uint8)

        # itera attraverso gli elementi dell'array 2D
        for i in range(self.field_array.shape[0]):
            for j in range(self.field_array.shape[1]):
                # estrae il valore RGB corrispondente dal dizionario
                # usando l'elemento corrente dell'array 2D come indice
                color = number_to_RGB_dict[self.field_array[i, j]]
                # assegna i valori RGB estratti alle rispettive posizioni nell'array 3D
                field_array_3d[i, j, 0] = color[0]
                field_array_3d[i, j, 1] = color[1]
                field_array_3d[i, j, 2] = color[2]

        # restituisce l'array 3D
        return field_array_3d


# Crea la classe astratta FieldReader con un metodo astratto read_file()
class FieldReader(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read_file(self):
        pass


# Crea la classe concreta PNGFieldReader che estende FileReader e implementa read_file()
class PNGFieldReader(FieldReader):
    """
    Riceve il path a un'immagine di tipo PNG e restituisce un numpy array 3D
    relativo all'immagine
    """

    def read_file(self):
        with Image.open(self.file_path) as field_image:
            return np.array(field_image)


# Crea la classe concreta JSONFieldReader che estende FileReader e implementa read_file()
class JSONFieldReader(FieldReader):
    """
    Riceve il path a un file in formato JSON e restituisce un numpy array 3D
    relativo file
    """

    def read_file(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        # Prendi le dimensioni dell'immagine dal file JSON
        rows = data['rows']
        cols = data['cols']

        # crea un array 3D vuoto settando tutti i valori a (0,0,0)
        field_array = np.zeros((rows, cols, 3), dtype=np.uint8)

        # imposta le celle relative al cibo arancioni
        for x, y in data["food"]:
            field_array[x, y] = [255, 128, 0]

        # imposta le celle relative agli ostacoli rosse
        for x, y in data["blocks"]:
            field_array[x, y] = [255, 0, 0]

        return field_array


# Crea la classe di factory FieldReaderFactory
class FieldReaderFactory:
    # Definisce il metodo create_reader() che restituisce un'istanza della classe concreta appropriata
    @staticmethod
    def create_reader(file_path):
        # crea un'istanza di FileChecker
        file_checker = FileChecker(file_path)
        try:
            # controlla se il file esiste
            file_checker.check()
            if file_path.endswith('.png'):
                return PNGFieldReader(file_path)
            elif file_path.endswith('.json'):
                return JSONFieldReader(file_path)
            else:
                raise ValueError('Formato file non supportato')
        except FileNotFoundError as e:
            raise e


class FileChecker:
    def __init__(self, file_path):
        self.file_path = file_path

    def check(self):
        # Controlla se il file esiste
        if not os.path.isfile(self.file_path):
            # Solleva un'eccezione di tipo FileNotFoundError
            raise FileNotFoundError("File non trovato nella posizione specificata")


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
                    continue
                case _:
                    return
        return

    def get_game_state_2D(self):
        """
        Metodo che serve a visualizzare dinamicamente la partita
        come si sta evolvendo.
        :return:
        """
        # Crea un'immagine vuota con le dimensioni del campo da gioco
        rows, cols = self.field.size
        current_field = self.field.get_field()

        # Colora ogni casella del campo
        for row in range(rows):
            for col in range(cols):
                if [row, col] in self.snake.get_body():
                    # Colora il corpo del serpente di verde
                    current_field[row, col] = FieldColor.SNAKE.value
                elif [row, col] in self.snake.get_trail():
                    # Colora la scia del serpente di grigio
                    current_field[row, col] = FieldColor.SNAKE_TRAIL.value
        return current_field

    def dynamic_play(self):
        image = FieldConverter(Game.get_game_state_2D(self)).int_to_RGB()
        plt.ion()  # Attiva l'interactive mode
        plt.imshow(image)  # Visualizza l'immagine
        plt.show()  # Mostra la finestra con l'immagine
        plt.draw()  # Forza il ridisegno della finestra
        plt.pause(0.01)  # Aspetta 0.01 secondi e aggiorna l'immagine


class GameFileReader:
    """
    Classe che si occupa della lettura del file contenente le info sul campo da gioco. I campi presenti in tale file
    vengono poi salvati come attributi della classe in modo da renderli recuperabili in seguito.
    """

    def __init__(self, file: str):
        try:
            gameFile = open(file)
            game = json.load(gameFile)
            gameFile.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"Il file {file} non è presente..")

        self.field_in = game["field_in"]
        self.start = game["start"]
        self.moves = game["moves"]
        self.field_out = game["field_out"]  # Nome e ubicazione del file che verrà creato alla fine.

    # GETTERS:

    def getFieldIn(self):
        return self.field_in

    def getStart(self):
        return self.start

    def getMoves(self):
        return self.moves

    def getFieldOut(self):
        return self.field_out


class Moves(Enum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7


class MovesMapper:
    """
    Classe che si occupa di verificare la legalità delle mosse e della conversione da stringhe a numeri interi, come
    codificato nella classe Moves. In presenza di mosse non legali viene sollevata un'eccezione di tipo KeyError.
    """

    @staticmethod
    def moves_to_numbers(moves: str) -> list:
        """
        Metodo che converte le mosse di tipo stringa in ingresso in valori interi e controlla la legalità della mossa,
        secondo la codifica stabilita nella classe Moves. Se una mossa presente nella stringa in ingresso non è
        una mossa legale, ovvero non definita in Moves (a meno di caratteri minuscoli), il metodo solleva un'eccezione
        di tipo KeyError.
        :param moves: str, stringa contenente le mosse da convertire; deve essere composta da caratteri rappresentanti
                            le singole mosse separati da un numero qualsiasi di spazi, ad esempio: " N  S SE NE  "
        :return: list of ints, lista di interi che rappresentano le mosse
        """
        moves = moves.upper().split()
        moves_int = []
        for item in moves:
            moves_int.append(Moves[item].value)
        return moves_int


class PNGFileMaker:
    """
    Classe contentente unicamente un metodo statico che si occupa di salvare il campo da gioco
    finale in formato png.
    """

    @staticmethod
    def write_file(path: str, np_3d: np.ndarray):
        """
        Metodo statico che riceve in input un path e un numpy array che contiene in ogni sua casella una tupla
        di tre elementi che rappresentano un colore. L'nparray viene quindi convertito in formato png
        e salvato nel path specificato in input.
        :param path:
        :param np_3d:
        :return:
        """
        image = Image.fromarray(np_3d)
        image.save(path)
