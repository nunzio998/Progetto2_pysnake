from abc import ABC, abstractmethod


# Crea la classe astratta FieldReader con un metodo astratto read_file()
class FieldReader(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read_file(self):
        pass


# Crea la classe concreta PNGFieldReader che estende FileReader e implementa read_file()
class PNGFieldReader(FieldReader):
    def read_file(self):
        pass


# Crea la classe concreta JSONFieldReader che estende FileReader e implementa read_file()
class JSONFieldReader(FieldReader):
    def read_file(self):
        pass


# Crea la classe di factory FieldReaderFactory
class FieldReaderFactory:
    # Definisce il metodo create_reader() che restituisce un'istanza della classe concreta appropriata
    def create_reader(self, file_path):
        if file_path.endswith('.png'):
            return PNGFieldReader(file_path)
        elif file_path.endswith('.json'):
            return JSONFieldReader(file_path)
        else:
            raise ValueError('Formato file non supportato')
