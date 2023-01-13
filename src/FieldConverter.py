from enum import Enum
import numpy as np


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

    def RGB_to_number(self):
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

    def number_to_RGB(self):
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
