class Snake:
    """
    Classe relativa al serpente. Gli attributi presenti sono in riferimento alla lunghezza, al corpo e alla scia del
    serpente. La classe implementa i metodi che permettono al serpente di muoversi e mangiare cibo, oltre ai vari
    getters.
    """

    def __init__(self, start: tuple):
        self.body = [start]
        self.lenght = 1
        self.trail = []

    def move(self, next_pos: tuple) -> bool:
        """
        Metodo invocato nel caso in cui il serpente si muove in una casella vuota. Si aggiorna quindi la lista del body
        e della scia, lasciando invece invariata la lunghezza.
        :param next_pos:
        :return: True se la mossa è riuscita, False se non è riuscita a causa di intersezione del serpente
        """
        if self.intersects(next_pos):
            return False
        self.trail.append(self.body[0])  # aggiorno la scia.
        self.body.pop(0)  # elimino l'ultimo punto della coda.
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa in fondo alla lista.
        return True

    def eat(self, next_pos: tuple) -> bool:
        """
        Metodo invocato nel caso in cui il serpente si muove in una casella che contiene il cibo. In questo caso la
        lunghezza viene incrementata e vengono aggiornata la lista relativa al corpo. Non viene quindi effettuato
        il pop del primo elemento della lista body in quando la lunghezza del corpo aumenta.
        :param next_pos:
        :return: True se la mossa è riuscita, False se non è riuscita a causa di intersezione del serpente
        """
        if self.intersects(next_pos):
            return False
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa.
        self.lenght += 1  # aumento la lunghezza
        return True

    # GETTERS:
    def get_head(self):
        return self.body[len(self.body) - 1]

    def get_body(self):
        return self.body

    def get_trail(self):
        return self.trail

    def intersects (self, next_pos) -> bool:
        """

        :param next_pos:
        :return: True se la mossa porta a intersezione del serpente, False altrimenti
        """
        intersects = False
        head = self.body[-1]
        if next_pos in self.body[2:-1]:
            intersects = True
        if (next_pos[0] - head[0]) * (next_pos[1] - head[1]) != 0:  # se va in diagonale
            # controlla che entrambe le seguenti due caselle non appartengano al body
            to_check1 = (next_pos[0], head[1])
            to_check2 = (head[0], next_pos[1])
            if to_check1 in self.body[1:-1] and to_check2 in self.body[1:-1]:
                intersects = True
        return intersects
