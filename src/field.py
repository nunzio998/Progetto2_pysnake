import numpy as np


class Field:
    """
    Classe che definisce il campo da gioco, rappresentato con un numpy.ndarray bidimensionale in cui il valore di ogni
    elemento indica il contenuto di una casella del campo, in accordo con la codifica stabilita nella classe FieldColor.

    Attributi:
        field: numpy.ndarray, array bidimensionale rappresentante il contenuto delle caselle del campo da gioco;
        le caselle sono identificate nel campo da una coppia (riga,colonna):
        - le righe sono crescenti verso il basso
        - le colonne sono crescenti verso destra
        size:  tuple of ints, dimensioni del campo da gioco: (numero righe, numero colonne)

    Metodi:
        get_value: restituisce il valore dell'elemento di posizione specificata in ingresso
        get_size:  restituisce le dimensioni del campo da gioco
        pop_food:  rimuove il cibo presente nella casella specificata in ingresso
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


array = np.array([[2, 4, 5, 6, 0], [1, 3, 6, 3, 2], [0, 0, 4, 1, 4], [1, 3, 4, 1, 0]])
campo = Field(array)
print(type(campo.get_size()))
print(campo.get_value((7, 3)))
