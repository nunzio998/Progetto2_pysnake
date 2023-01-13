import os


class FileChecker:
    def __init__(self, file_path):
        self.file_path = file_path

    def check(self):
        # Controlla se il file esiste
        if not os.path.isfile(self.file_path):
            # solleva un'eccezione di tipo FileNotFoundError
            raise FileNotFoundError("File non trovato nella posizione specificata")
