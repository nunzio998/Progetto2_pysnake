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
        next_pos = self.snake.get_head()  # [riga,colonna]; righe e colonne crescono da alto-sinista verso basso-destra
        match move:
            case "N":
                next_pos[0] = next_pos[0] - 1 if next_pos[0] >= 1 else self.size_field[0] - 1
            case "S":
                next_pos[0] = (next_pos[0] + 1) % self.size_field[0]
            case "E":
                next_pos[1] = (next_pos[1] + 1) % self.size_field[1]
            case "W":
                next_pos[1] = next_pos[1] - 1 if next_pos[1] >= 1 else self.size_field[1] - 1
            case "NE":
                next_pos[0] = next_pos[0] - 1 if next_pos[0] >= 1 else self.size_field[0] - 1
                next_pos[1] = (next_pos[1] + 1) % self.size_field[1]
            case "NW":
                next_pos[0] = next_pos[0] - 1 if next_pos[0] >= 1 else self.size_field[0] - 1
                next_pos[1] = next_pos[1] - 1 if next_pos[1] >= 1 else self.size_field[1] - 1
            case "SE":
                next_pos[0] = (next_pos[0] + 1) % self.size_field[0]
                next_pos[1] = (next_pos[1] + 1) % self.size_field[1]
            case "SW":
                next_pos[0] = (next_pos[0] + 1) % self.size_field[0]
                next_pos[1] = next_pos[1] - 1 if next_pos[1] >= 1 else self.size_field[1] - 1

        # valuta l'esito della mossa e la fa eseguire al serpente
        if list(self.field[next_pos[0], next_pos[1], :]) in [self.color_dict['vuoto'], self.color_dict['scia']] and \
                not self.intersects(next_pos, move):
            left_pos = self.snake.move(next_pos)
            # colora la testa del serpente
            self.field[next_pos[0], next_pos[1], :] = self.color_dict['corpo']
            # colora la posizione lasciata
            self.field[left_pos[0], left_pos[1], :] = self.color_dict['scia']
            return True
        elif list(self.field[next_pos[0], next_pos[1], :]) == self.color_dict['cibo']:
            # fai fare la mossa al serpente
            self.snake.eat(next_pos)
            # colora la testa del serpente
            self.field[next_pos[0], next_pos[1], :] = self.color_dict['corpo']
            return True
        else:
            return False

    def intersects(self, next_pos: list, move: str) -> bool:
        if move in ["N", "S", "E", "W"]:
            return False
        head = np.array(self.snake.get_head())
        delta = np.array(next_pos) - head
        to_check1 = head + np.array([delta[0], 0])
        to_check2 = head + np.array([0, delta[1]])
        if np.array_equal(self.field[to_check1[0], to_check1[1], :], self.color_dict['corpo']) and \
                np.array_equal(self.field[to_check2[0], to_check2[1], :], self.color_dict['corpo']):
            return True
        return False

    def get_snake_length(self) -> int:
        return self.snake.get_length()
