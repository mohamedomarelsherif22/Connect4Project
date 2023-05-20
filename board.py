# board class
from PIL import ImageGrab
import pyautogui
import random
import math
import numpy as np
LEFT = 595
TOP = 236
RIGHT = 1336
BOTTOM = 860
######################
EMPTY = 0
RED = 1
BLUE = 2
#########################
ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
PLAYER_PIECE = RED
AI_PIECE = BLUE

class Board:
    def _init_(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]

    def print_grid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == RED:
                    print("R", end=" \t")
                elif grid[i][j] == BLUE:
                    print("B", end=" \t")
            print("\n")
        print("-----------------------------------------------------------------------------")
