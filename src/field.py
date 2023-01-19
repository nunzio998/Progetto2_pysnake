import numpy as np


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
