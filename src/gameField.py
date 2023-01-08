import numpy as np
from snake import Snake
from PIL import Image


class GameField:
    """
    Classe che definisce il campo da gioco.

    Attributi:
    - Il campo da gioco, rappresentato tramite un array numpy tridimensionale, in cui la prima dimensione rappresenta
      le righe, la seconda le colonne, la terza il colore delle celle, rappresentate in RGB;le righe e le colonne sono
      crescenti dalle posizioni alto-sinistra verso quelle basso-destra del campo da gioco; in questo modo
      la prima cella in alto a sinistra avrà valori: row=0 col=0
    - Un dizionario che indica il significato del colore delle celle
    - Un oggetto di tipo Snake

    Metodi:
    - Un metodo per verificare la legalità di una mossa ed eseguirla
    - Un metodo che restituisce la lunghezza del serpente
    """

    def __init__(self, field_image: Image, start: list):
        """
        Istanzia il campo da gioco.
        :param field_image: Image: immagine del campo da gioco
        :param start: list: lista che rappresenta la posizione iniziale [riga,colonna] della testa del serpente
        """
        self.field = np.array(field_image)
        self.size_field = self.field.shape[:2]
        self.color_dict = {'vuoto': [0, 0, 0], 'cibo': [255, 128, 0], 'ostacolo': [255, 0, 0],
                           'corpo': [0, 255, 0], 'scia': [128, 128, 128]}
        self.snake = Snake(start)
        self.field[start[0], start[1], :] = self.color_dict['corpo']

    def step(self, move: str) -> bool:
        """
        Metodo che verifica la legalità di una mossa richiesta e, se possibile, la esegue, restituendone l'esito.
        Se la mossa richiesta non è legale viene sollevata un'eccezione di tipo ValueError. L'esito della mossa è un
        valore booleano che indica se la mossa porta o meno alla terminazione.
        :param move: str: stringa che identifica la mossa da eseguire
        :return: False se la mossa eseguita porta al termine del gioco, True altrimenti
        """
        # verifica che la mossa sia legale
        if move not in ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']:
            raise ValueError("La mossa richiesta non è legale.")

        # calcola la nuova posizione della testa

        # valuta l'esito della mossa e la fa eseguire al serpente
        return False

    def get_snake_length(self) -> int:
        return self.snake.get_length()
