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

    def move(self, next_pos: tuple):
        """
        Metodo invocato nel caso in cui il serpente si muova in una casella vuota. Si aggiorna quindi la lista del body
        e della scia, lasciando invece invariata la lunghezza.
        La condizione di aggiornamento della scia prevede che l'ultimo e il penultimo elemento del body siano diversi,
        questo permette l'implementazione del caso in cui lo start coincida con una casella contenente cibo: in questo
        caso il serpente ha body formato da due posizioni uguali (lo start), e quindi al primo movimento in una casella
        vuota deve aggiornare il body ma non la scia.
        :param next_pos: tuple
                    posizione su cui si deve spostare la testa del serpente
        :return:
        """
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa in fondo alla lista.
        if self.body[0] != self.body[1]:
            self.trail.append(self.body[0])  # aggiorno la scia.
        self.body.pop(0)  # elimino l'ultimo punto della coda.

    def eat(self, next_pos: tuple):
        """
        Metodo invocato nel caso in cui il serpente si muova in una casella che contiene il cibo. In questo caso la
        lunghezza viene incrementata e viene aggiornato il body, senza effettuare il pop del primo elemento
        in quando la lunghezza del corpo aumenta.
        :param next_pos: tuple
                    posizione su cui si deve spostare la testa del serpente
        :return:
        """
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa.
        self.lenght += 1  # aumento la lunghezza

    # GETTERS:
    def get_head(self):
        return self.body[len(self.body) - 1]

    def get_body(self):
        return self.body

    def get_trail(self):
        return self.trail

    def get_lenght(self):
        return self.lenght

    def intersects(self, next_pos) -> bool:
        """
        Metodo che verifica se la mossa successiva porta o meno all'intersezione del corpo del serpente in una qualsiasi
        direzione (orizzontale, verticale, diagonale).
        :param next_pos: tuple
                    posizione su cui si dovrebbe spostare la testa del serpente per compiere la mossa per la quale si
                    vuole controllare l'eventuale presenza di intersezione
        :return: bool
                    True se la mossa porta a intersezione del corpo del serpente, False altrimenti
        """
        intersects = False
        head = self.body[-1]
        if next_pos in self.body[1:-1]:
            intersects = True
        if (next_pos[0] - head[0]) * (next_pos[1] - head[1]) != 0:  # se va in diagonale
            # controlla che entrambe le seguenti due caselle non appartengano al body
            to_check1 = [next_pos[0], head[1]]
            to_check2 = [head[0], next_pos[1]]
            if to_check1 in self.body[1:-1] and to_check2 in self.body[1:-1]:
                intersects = True
        return intersects
