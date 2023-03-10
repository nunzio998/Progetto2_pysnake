import numpy as np
from FieldConverter import FieldColor


class Field:
    """
    Classe che definisce il campo da gioco, rappresentato con un numpy.ndarray bidimensionale; il valore di ogni
    elemento indica il contenuto di una casella del campo, in accordo con la codifica stabilita nella classe FieldColor.

    Attributi:
        field: numpy.ndarray, array bidimensionale rappresentante il contenuto delle caselle del campo da gioco;
        ogni casella è identificata dalla sua posizione, rappresentata con una coppia di indici (riga,colonna), in cui:
        - le righe partono da zero e sono crescenti verso il basso
        - le colonne partono da zero e sono crescenti verso destra
        size:  tuple of ints, dimensioni del campo da gioco: (numero righe, numero colonne)

    Metodi:
        get_value: restituisce il valore dell'elemento di posizione specificata in ingresso
        get_size:  restituisce le dimensioni del campo da gioco
        get_field: restituisce tutto il campo da gioco
        remove:  rimuove dal campo il contenuto della casella specificata in ingresso
        next_pos:  restituisce la posizione e il contenuto della casella risultate da una mossa
    """

    def __init__(self, field: np.ndarray):
        """
        Costruttore che prende in ingresso un array numpy rappresentante il campo e istanzia l'oggetto campo da gioco

        :param field: numpy.ndarray
                    array numpy rappresentante il campo da gioco
        """
        self.field = field
        self.size = field.shape

    def get_value(self, pos: tuple) -> int:
        """
        Metodo che restituisce il valore della casella del campo di posizione specificata in ingresso. Se la posizione
        indicata in ingresso eccede le dimensioni del campo viene sollevata un'eccezione di tipo IndexError
        :param pos:
                tuple of ints, identifica una casella del campo
        :return: int
        """
        return self.field[pos[0], pos[1]]

    def get_size(self) -> tuple:
        """
        Metodo che restituisce le dimensioni del campo da gioco (numero righe, numero colonne)
        :return: tuple of ints
        """
        return self.size[0], self.size[1]

    def get_field(self) -> np.ndarray:
        """
        Metodo che restituisce l'intero campo da gioco
        :return: np.ndarray
        """
        return self.field

    def remove(self, pos: tuple):
        """
        Rimuove un oggetto dal campo portando la casella specificata al valore di casella vuota;
        viene usato per rimuovere il cibo da una casella quando il serpente la attraversa
        :param pos: tuple
        :return:
        """
        self.field[pos[0], pos[1]] = FieldColor.EMPTY.value

    def next_pos(self, init_pos: tuple, move: int) -> tuple:
        """
        Metodo che si occupa di determinare la posizione risultante dall'applicazione di una specifica mossa ad una
        specifica casella di partenza. Restituisce la posizione della casella finale e il suo contenuto.

        :param init_pos: tuple
                    posizione iniziale dalla quale ci si vuole spostare applicando una mossa [riga,colonna]
        :param move: int
                    intero rappresentante una delle mosse legali definite nella classe Moves
        :return: tuple
                    posizione finale e valore: (riga,colonna,valore)
        """
        try:
            self.get_value(init_pos)
        except:
            print("Posizione iniziale non valida, non compresa nei limiti del campo!")
            return -1,
        position = list(init_pos)  # crea un nuovo oggetto di tipo lista
        if move == 0:
            position[0] = position[0] - 1 if position[0] >= 1 else self.size[0] - 1
        elif move == 4:
            position[0] = (position[0] + 1) % self.size[0]
        elif move == 2:
            position[1] = (position[1] + 1) % self.size[1]
        elif move == 6:
            position[1] = position[1] - 1 if position[1] >= 1 else self.size[1] - 1
        elif move == 1:
            position[0] = position[0] - 1 if position[0] >= 1 else self.size[0] - 1
            position[1] = (position[1] + 1) % self.size[1]
        elif move == 7:
            position[0] = position[0] - 1 if position[0] >= 1 else self.size[0] - 1
            position[1] = position[1] - 1 if position[1] >= 1 else self.size[1] - 1
        elif move == 3:
            position[0] = (position[0] + 1) % self.size[0]
            position[1] = (position[1] + 1) % self.size[1]
        elif move == 5:
            position[0] = (position[0] + 1) % self.size[0]
            position[1] = position[1] - 1 if position[1] >= 1 else self.size[1] - 1
        return position, self.field[position[0], position[1]]
