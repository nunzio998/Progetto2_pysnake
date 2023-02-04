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
        :param moves: str
                    stringa contenente le mosse da convertire; deve essere composta da caratteri rappresentanti
                            le singole mosse separati da un numero qualsiasi di spazi, ad esempio: " N  S SE NE  "
        :return: list of ints
                    lista di interi che rappresentano le mosse
        """
        moves = moves.upper().split()
        moves_int = []
        for item in moves:
            moves_int.append(Moves[item].value)
        return moves_int
