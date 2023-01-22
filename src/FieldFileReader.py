import json
from abc import ABC, abstractmethod

import numpy as np
from PIL import Image

from FileChecker import FileChecker


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
