
from enum import Enum, auto
import sys
import numpy as np


class Cell(Enum):
    PLAYER1 = 1
    PLAYER2 = 2


class Status(Enum):
    PLAYER1_WON = auto()
    PLAYER2_WON = auto()
    DRAW = auto()
    PLAYING = auto()


class Field:

    def __init__(self):
        self.rows_l = np.matrix([
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]
        ])

    def __str__(self):
        field_s = "-" * self.get_column_size() + "\n"
        for row_l in self.rows_l:
            for cell in row_l:
                if cell is None:
                    field_s += " "
                else:
                    field_s += str(cell.value)
            field_s += "\n"
        field_s += "-" * self.get_column_size() + "\n"
        for i in range(self.get_column_size()):
            field_s += str(i)
        return field_s

    def play(self, player, col_i):
        for i in range(len(self.rows_l) - 1, -1, -1):
            if self.rows_l[i][col_i] is None:
                self.rows_l[i][col_i] = player
                return
        print("something is wrong!")

    def get_column_size(self):
        return len(self.rows_l[0])

    def status(self):
        # check winner
        # row
        for row_l in self.rows_l:
            for col_i in range(0, len(row_l) - 4):
                if row_l[col_i:col_i + 4] is [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if row_l[col_i:col_i + 4] is [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON
        # column
        for col_i in range(len(self.rows_l[0])):
            for row_i in range(len(self.rows_l) - 4):
                row1 = self.rows_l[row_i][col_i]
                row2 = self.rows_l[row_i + 1][col_i]
                row3 = self.rows_l[row_i + 2][col_i]
                row4 = self.rows_l[row_i + 3][col_i]
                if [row1, row2, row3, row4] is [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if [row1, row2, row3, row4] is [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON
        # skew
        for row_i in range(len(self.rows_l) - 4):
            for col_i in range(len(self.rows_l[0] - 4)):
                row1 = self.rows_l[row_i][col_i]
                row2 = self.rows_l[row_i + 1][col_i + 1]
                row3 = self.rows_l[row_i + 2][col_i + 2]
                row4 = self.rows_l[row_i + 3][col_i + 3]
                if [row1, row2, row3, row4] is [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if [row1, row2, row3, row4] is [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON
        for row_i in range(len(self.rows_l) - 4):
            for col_i in range(len(self.rows_l[0] - 4)):
                row1 = self.rows_l[row_i][col_i]
                row2 = self.rows_l[row_i + 1][col_i + 1]
                row3 = self.rows_l[row_i + 2][col_i + 2]
                row4 = self.rows_l[row_i + 3][col_i + 3]
                if [row1, row2, row3, row4] is [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if [row1, row2, row3, row4] is [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON

        return Status.DRAW
        return Status.PLAYING


field = Field()
print(field)
while True:
    for player in list(Cell):
        print("Please input your number 0 ~ ", field.get_column_size() - 1)
        print(player.name, end=": ")
        field.play(player, int(input()))

        print(field)
        if field.status() is Status.PLAYER1_WON:
            print("won by ", player.name)
            sys.exit(0)
        elif field.status() is Status.PLAYER2_WON:
            print("won by ", player.name)
            sys.exit(0)
        elif field.status() is Status.DRAW:
            print("draw")
            sys.exit(0)
        elif field.status() is Status.PLAYING:
            continue
        else:
            print("something is wrong!!!")
            sys.exit(0)
