from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


class SnakeGame:
    def __init__(self, field, start):
        self.field = field
        self.snake = [(start[0], start[1])]
        self.running = True
        self.scia = [(start[0], start[1])]

    def move(self, move):
        # Aggiorna la posizione della testa del serpente in base alla direzione
        head_row, head_col = self.snake[0]
        if move == 'N':
            head_row -= 1
        elif move == 'S':
            head_row += 1
        elif move == 'E':
            head_col += 1
        elif move == 'W':
            head_col -= 1
        elif move == 'NE':
            head_row -= 1
            head_col += 1
        elif move == 'NW':
            head_row -= 1
            head_col -= 1
        elif move == 'SE':
            head_row += 1
            head_col += 1
        elif move == 'SW':
            head_row += 1
            head_col -= 1
        else:
            raise ValueError(f"Invalid direction: {move}")

        # Controlla se il serpente sbatte contro la parete, in caso riappare dall'altra parte
        cols, rows = self.field.size
        if head_row < 0:
            head_row = rows - 1
        elif head_row >= rows:
            head_row = 0
        if head_col < 0:
            head_col = cols - 1
        elif head_col >= cols:
            head_col = 0

        # Controlla se il serpente passa sulla coda o sbatte contro un ostacolo
        if (head_row, head_col) in self.snake[1:] or self.field.getpixel((head_col, head_row)) == (255, 0, 0):
            # Il serpente muore
            self.running = False

        # Controlla se il serpente è passato sulla sua coda in diagonale in direzione NW
        elif move == 'NW' and (head_row, head_col + 1) and (head_row + 1, head_col) in self.snake:
            # Il serpente muore
            self.running = False

        # Controlla se il serpente è passato sulla sua coda in diagonale in direzione NE
        elif move == 'NE' and (head_row, head_col - 1) and (head_row + 1, head_col) in self.snake:
            # Il serpente muore
            self.running = False

        # Controlla se il serpente è passato sulla sua coda in diagonale in direzione SE
        elif move == 'SE' and (head_row, head_col - 1) and (head_row - 1, head_col) in self.snake:
            # Il serpente muore
            self.running = False

        # Controlla se il serpente è passato sulla sua coda in diagonale in direzione SW
        elif move == 'SW' and (head_row - 1, head_col) and (head_row, head_col + 1) in self.snake:
            # Il serpente muore
            self.running = False

        else:
            # Aggiorna la posizione della testa del serpente
            self.snake = [(head_row, head_col)] + self.snake

            # Aggiorna la lista della scia
            self.scia.append((head_row, head_col))

            # Controlla se il serpente deve crescere
            if self.field.getpixel((head_col, head_row)) == (255, 128, 0):
                # Rimuove il cibo una volta mangiato
                self.field.putpixel((head_col, head_row), (0, 0, 0))
            else:
                # Rimuovi la coda del serpente se non deve crescere
                self.snake.pop()

    def get_field(self):
        return self.field

    def snake_is_alive(self):
        return self.running

    def snake_length(self):
        return len(self.snake)

    def dynamic_play(self):
        """
        Metodo che serve a visualizzare dinamicamente la partita
        come si sta evolvendo.
        :return:
        """
        # Crea un'immagine vuota con le dimensioni del campo da gioco
        cols, rows = self.field.size
        image = Image.new('RGB', (cols, rows), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Colora ogni casella del campo
        for row in range(rows):
            for col in range(cols):
                color = self.field.getpixel((col, row))
                if (row, col) in self.snake:
                    # Colora il corpo del serpente di verde
                    color = (0, 255, 0)
                elif (row, col) in self.scia:
                    # Colora la scia del serpente di grigio
                    color = (128, 128, 128)
                draw.point((col, row), fill=color)

        plt.ion()  # Attiva l'interactive mode
        plt.imshow(image)  # Visualizza l'immagine
        plt.show()  # Mostra la finestra con l'immagine
        plt.draw()  # Forza il ridisegno della finestra
        plt.pause(0.01)  # Aspetta 0.01 secondi e aggiorna l'immagine

    def save_game_state(self, file_path):
        """
        Metodo che salva l'immagine della situazione a fine partita.
        :param file_path: path di destinazione
        :return:
        """
        # Crea un'immagine vuota con le dimensioni del campo da gioco
        cols, rows = self.field.size
        image = Image.new('RGB', (cols, rows), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Colora ogni casella del campo
        for row in range(rows):
            for col in range(cols):
                color = self.field.getpixel((col, row))
                if (row, col) in self.snake:
                    # Colora il corpo del serpente di verde
                    color = (0, 255, 0)
                elif (row, col) in self.scia:
                    # Colora la scia del serpente di grigio
                    color = (128, 128, 128)
                draw.point((col, row), fill=color)

        # Salva l'immagine in un file
        image.save(file_path)
