from abc import ABC, abstractmethod
import json
from PIL import Image, ImageDraw


# Crea la classe astratta FileReader con un metodo astratto read_file()
class FileReader(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read_file(self):
        pass


# Crea la classe concreta PNGFileReader che estende FileReader e implementa read_file()
class PNGFileReader(FileReader):
    def read_file(self):
        image = Image.open(self.file_path)
        return image


# Crea la classe concreta JSONFileReader che estende FileReader e implementa read_file()
class JSONFileReader(FileReader):
    def read_file(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        # Prendi le dimensioni dell'immagine dal file JSON
        rows = data['rows']
        cols = data['cols']

        # Crea un'immagine nera con le dimensioni specificate
        image = Image.new('RGB', (cols, rows), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Disegna gli ostacoli come quadrati rossi
        for block in data['blocks']:
            row, col = block
            draw.rectangle((col, row, col, row), fill=(255, 0, 0))

        # Disegna il cibo come quadrati arancioni
        for food in data['food']:
            row, col = food
            draw.rectangle((col, row, col, row), fill=(255, 128, 0))
        image.save('image.png')

        return image


# Crea la classe di factory FileReaderFactory
class FileReaderFactory:
    # Definisce il metodo create_reader() che restituisce un'istanza della classe concreta appropriata
    def create_reader(self, file_path):
        if file_path.endswith('.png'):
            return PNGFileReader(file_path)
        elif file_path.endswith('.json'):
            return JSONFileReader(file_path)
        else:
            raise ValueError('Formato file non supportato')

