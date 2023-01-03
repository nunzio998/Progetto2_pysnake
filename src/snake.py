class Snake:
    """
    Classe che definisce il serpente. Tale classe verrà instanziata dalla classe relativa al campo di gioco.
    Vengono implementati i metodi di get degli attributi e il metodo che consente al serpente di effettuare le
    mosse.
    """
    def __init__(self, x_iniziale, y_iniziale):
        self.lenght = 1
        self.pos_x = x_iniziale  # riga
        self.pos_y = y_iniziale  # colonna

    def get_lunghezza(self):
        return self.lenght

    def get_posizione(self):
        return [self.pos_x, self.pos_y]

    def muovi(self, mossa: str):
        """
        questo metodo consente di effettuare le mosse che il serpente dovrà compiere andando a modificare,
        in base al tipo di mossa che si fa, le coordinate x e y della testa di quest'ultimo. Nel caso in cui venga
        richiesto di fare una mossa che non sia una delle 8 consentite viene lanciata un'eccezione di tipo
        ValueError. In questo modo la seguente classe si occuperà solo di controllare che la mossa richiesta sia
        effettivamente una mossa. Non si effettuano controlli sulla validità della mossa nel campo di gioco, compito
        che viene invece lasciato alla classe del campo di gioco.
        :param mossa:
        :return:
        """
        match mossa:
            case "N":
                self.lenght += 1
                self.pos_x -= 1
            case "S":
                self.lenght += 1
                self.pos_x += 1
            case "E":
                self.lenght += 1
                self.pos_y += 1
            case "W":
                self.lenght += 1
                self.pos_y -= 1
            case "NE":
                self.lenght += 1
                self.pos_x -= 1
                self.pos_y += 1
            case "NW":
                self.lenght += 1
                self.pos_x -= 1
                self.pos_y -= 1
            case "SE":
                self.lenght += 1
                self.pos_x += 1
                self.pos_y += 1
            case "SW":
                self.lenght += 1
                self.pos_x += 1
                self.pos_y -= 1
            case _:
                raise ValueError("Il valore inserito non è una mossa possibile.")
