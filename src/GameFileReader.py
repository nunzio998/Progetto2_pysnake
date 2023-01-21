import json

import matplotlib.image as mtp


class GameFileReader:
    """
    Classe che si occupa della lettura del file contenente le info sul campo da gioco. I campi presenti in tale file
    vengono poi salvati come attributi della classe in modo da renderli recuperabili in seguito.
    """

    def __init__(self, file: str):
        try:
            gameFile = open(file)
            game = json.load(gameFile)
            gameFile.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"Il file {file} non è presente..")

        self.field_in = game["field_in"]
        self.start = game["start"]
        self.moves = game["moves"]
        self.field_out = game["field_out"]  # Nome e ubicazione del file che verrà creato alla fine.

    # GETTERS:

    def getFieldIn(self):
        return self.field_in

    def getStart(self):
        return self.start

    def getMoves(self):
        return self.moves

    def getFieldOut(self):
        return self.field_out
