import numpy as np

class Field:
    """
    Classe che definisce il campo da gioco, rappresentato con un numpy.ndarray bidimensionale in cui il valore di ogni
    elemento indica il contenuto di una casella del campo, in accordo con la codifica stabilita nella classe FieldColor.

    Attributi:
    field: numpy.ndarray, array bidimensionale rappresentante il contenuto delle caselle del campo da gioco;
                le caselle sono identificate nel campo da una coppia (riga,colonna):
                le righe sono crescenti verso il basso
                le colonne sono crescenti verso destra
    size:  tuple of ints, dimensioni del campo da gioco: (numero righe, numero colonne)

    Metodi:
        get_value: restituisce il valore dell'elemento di posizione specificata in ingresso
        get_size:  restituisce le dimensioni del campo da gioco
        pop_food:  rimuove il cibo presente nella casella specificata in ingresso
    """
    pass

