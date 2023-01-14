import numpy as np
from PIL import Image


class PNGFileMaker:
    """
    Classe contentente unicamente un metodo statico che si occupa di salvare il campo da gioco
    finale in formato png.
    """
    @staticmethod
    def write_file(path: str, np_3d: np.ndarray):
        """
        Metodo statico che riceve in input un path e un numpy array che contiene in ogni sua casella una tupla
        di tre elementi che rappresentano un colore. L'nparray viene quindi convertito in formato png
        e salvato nel path specificato in input.
        :param path:
        :param np_3d:
        :return:
        """
        image = Image.fromarray(np_3d)
        image.save(path)
