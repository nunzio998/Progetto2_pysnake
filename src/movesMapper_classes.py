from enum import Enum


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
    Classe che si occupa di verificare la legalità delle mosse e convertirle da stringhe a numeri interi, come
    codificato nella classe Moves. Eventuali mosse non presenti nella classe Moves provocano un'eccezione di tipo
    KeyError.
    """

    @classmethod
    def moves_to_number(cls, moves: str) -> list:
        """
        Metodo che converte le mosse di tipo stringa in ingresso in valori interi e controlla la legalità della mossa,
        secondo la codifica stabilita nella classe Moves. Se una mossa presente nella stringa in ingresso non è
        una mossa legale, ovvero non definita in Moves, il metodo solleva un'eccezione di tipo KeyError.

        :param moves: str, stringa contenente le mosse da convertire; deve essere composta da caratteri rappresentanti
                            le singole mosse separati da un numero qualsiasi di spazi, ad esempio: " N  S SE NE  "
        :return: list of ints, lista di interi che rappresentano le mosse
        """
        return []
