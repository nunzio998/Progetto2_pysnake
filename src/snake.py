class Snake:
    """
    Classe che definisce il serpente. Gli attributi di un'istanza di serpente sono la lunghezza (len) e la posizione
    della testa del serpente nel campo da gioco. Quest'ultima è rappresentata tramite un valore per la riga (row) e
    un valore per la colonna (col); le righe e le colonne sono crescenti dalle posizioni alto-sinistra verso quelle
    basso-destra del campo da gioco; in questo modo la prima cella in alto a sinistra avrà valori: row=0 col=0.
    Vengono implementati i metodi di get degli attributi e il metodo che consente al serpente di verificare la legalità
    delle mosse ed effettuarle.
    """
    def __init__(self, pos_iniziale):
        """
        Istanzia il serpente.
        :param pos_iniziale: list: lista [riga,colonna] che indica la posizione iniziale della testa del serpente
        """
        self.len = 1
        self.row = pos_iniziale[0]  # riga
        self.col = pos_iniziale[1]  # colonna

    def get_lunghezza(self) -> int:
        return self.len

    def get_posizione(self) -> list:
        """
        Restituisce la posizione della testa del serpente.
        :return: list: [riga,colonna]
        """
        return [self.row, self.col]

    def increase_lenght(self):
        self.len += 1

    def muovi(self, mossa: str):
        """
        Questo metodo verifica che la mossa richiesta sia legale e, in tal caso, la effettua modificando i valori
        row e col della testa del serpente. Una mossa è legale se rientra in una tra [N,S,E,W,NE,NW,SE,SW]. Nel caso
        di una mossa non legale viene sollevata un'eccezione di tipo ValueError.
        :param mossa: str
        :return:
        """
        match mossa:
            case "N":
                self.row -= 1
            case "S":
                self.row += 1
            case "E":
                self.col += 1
            case "W":
                self.col -= 1
            case "NE":
                self.row -= 1
                self.col += 1
            case "NW":
                self.row -= 1
                self.col -= 1
            case "SE":
                self.row += 1
                self.col += 1
            case "SW":
                self.row += 1
                self.col -= 1
            case _:
                raise ValueError("Il valore inserito non è una mossa possibile.")
