class Snake:
    """
    Classe che definisce il serpente.

    Attributi:
    Gli attributi dell'istanza sono la sua lunghezza (len) e la posizione di tutte
    le celle del campo su cui si trova il serpente. Le posizioni sono rappresentata tramite una coda (queue) di tipo
    [[r1,c1],[r2,c2],...,[rf,cf]], in cui ogni elemento è una lista [r,c] che contine la riga e la colonna della
    cella; in particolare [r1,c1] e [rf,cf] sono le posizioni delle celle relative alla testa e alla coda del sepente.

    Metodi:
    Sono implementati i metodi di get della lunghezza e della poeisione della testa del serpente, e i metodi che
    consentono al serpente di muoversi e di mangiare.
    """

    def __init__(self, init_pos: list):
        """
        Istanzia il serpente.
        :param init_pos: list: lista [riga,colonna] che indica la posizione iniziale della testa del serpente
        """
        self.len = 1
        self.queue = [init_pos]  # [[r1 c1],[r2 c2],...]

    def get_head(self) -> list:
        """
        Restituisce la posizione della cella realtiva alla testa del serpente.
        :return: list: [riga,colonna]
        """
        return [self.queue[0][0], self.queue[0][1]]

    def get_length(self) -> int:
        return self.len

    def move(self, next: list) -> list:
        """
        Metodo che consente al serpente di muoversi (senza mangiare) spostando la testa sulla cella indicata dalla
        lista in ingresso e spostando ogni suo punto nella posizione occupata dal punto precedente (verso la testa)
        prima della mossa.
        :param next: list: posizione della cella in cui si deve muovere la testa del serpente
        :return: list: posizione della cella su cui era posizionata la coda del serpente prima della mossa
        """
        self.queue.insert(0, next)
        return self.queue.pop()

    def eat(self, next: list):
        self.queue.insert(0, next)
        self.len += 1
