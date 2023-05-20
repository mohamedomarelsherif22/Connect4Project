import math
from board import Board
import time
def main() :
    board = Board()
    time.sleep(3)
    _,game_end = board.get_game_grid()
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        #board.print_grid(game_board)
        random_column = board.minimax(game_board, 6, -math.inf, math.inf, True)[0]
        if board.is_valid_location(game_board, random_column):
            board.select_column(random_column)
        time.sleep(3)

if __name__ == "__main__":
    main()