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
        Metodo invocato nel caso in cui il serpente si muove in una casella vuota. Si aggiorna quindi la lista del body
        e della scia, lasciando invece invariata la lunghezza.
        :param next_pos:
        :return:
        """
        def double_items(body: list) -> bool:
            """
            Funzione che controlla se sono presenti duplicati all'interno del corpo del serpente
            :param body: corpo del serpente
            :return: True se è presente almeno un duplicato, False altrimenti
            """
            seen = []
            duplicate_found = False
            for sublist in body:
                if sublist in seen:
                    duplicate_found = True
                    break
                else:
                    seen.append(sublist)
            return duplicate_found

        if not double_items(self.body):
            self.trail.append(self.body[0])  # aggiorno la scia.
            self.body.pop(0)  # elimino l'ultimo punto della coda.
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa in fondo alla lista.

    def eat(self, next_pos: tuple):
        """
        Metodo invocato nel caso in cui il serpente si muove in una casella che contiene il cibo. In questo caso la
        lunghezza viene incrementata e vengono aggiornata la lista relativa al corpo. Non viene quindi effettuato
        il pop del primo elemento della lista body in quando la lunghezza del corpo aumenta.
        :param next_pos:
        :return:
        """
        self.body.append(next_pos)  # aggiungo la nuova posizione della testa.
        self.lenght += 1  # aumento la lunghezza

    # GETTERS:
    def get_head(self):
        return self.body[len(self.body)-1]

    def get_body(self):
        return self.body

    def get_trail(self):
        return self.trail
