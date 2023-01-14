from src.Snake import Snake


def play(game_file: str) -> int:
    # scrivi qui il tuo codice
    pass


if __name__ == "__main__":
    snake = Snake((1, 2))
    snake.move((1, 3))
    snake.move((2, 4))
    snake.eat((2, 5))
    snake.move((2, 6))
    snake.eat((2, 7))
    snake.move((3, 6))
    print(snake.get_body())
    print(snake.get_trail())
    print(snake.get_head())
