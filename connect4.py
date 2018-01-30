
from enum import Enum, auto
import sys


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
        self.table = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]
        ]

    def __str__(self):
        field_s = "-" * self.get_column_size() + "\n"
        for row_l in self.table:
            for cell in row_l:
                if cell is None:
                    field_s += " "
                else:
                    field_s += str(cell.value)
            field_s += "\n"
        field_s += "-" * self.get_column_size() + "\n"
        for i in range(self.get_column_size()):
            field_s += str(i + 1)
        return field_s

    def play(self, player, col_i):
        for i in range(len(self.table) - 1, -1, -1):
            if self.table[i][col_i] is None:
                self.table[i][col_i] = player
                return
        raise ValueError

    def get_column_size(self):
        return len(self.table[0])

    def status(self):
        # check winner
        # row
        for row_l in self.table:
            for col_i in range(0, len(row_l) - 4):
                if row_l[col_i:col_i + 4] == [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if row_l[col_i:col_i + 4] == [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON
        # column
        for col_i in range(len(self.table[0])):
            for row_i in range(len(self.table) - 4):
                row1 = self.table[row_i][col_i]
                row2 = self.table[row_i + 1][col_i]
                row3 = self.table[row_i + 2][col_i]
                row4 = self.table[row_i + 3][col_i]
                if [row1, row2, row3, row4] == [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if [row1, row2, row3, row4] == [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON
        # skew
        for row_i in range(len(self.table) - 4):
            for col_i in range(len(self.table[0]) - 4):
                row1 = self.table[row_i][col_i]
                row2 = self.table[row_i + 1][col_i + 1]
                row3 = self.table[row_i + 2][col_i + 2]
                row4 = self.table[row_i + 3][col_i + 3]
                if [row1, row2, row3, row4] == [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if [row1, row2, row3, row4] == [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON
        for row_i in range(len(self.table) - 4):
            for col_i in range(len(self.table[0]) - 4):
                row1 = self.table[row_i][col_i]
                row2 = self.table[row_i + 1][col_i + 1]
                row3 = self.table[row_i + 2][col_i + 2]
                row4 = self.table[row_i + 3][col_i + 3]
                if [row1, row2, row3, row4] == [Cell.PLAYER1] * 4:
                    return Status.PLAYER1_WON
                if [row1, row2, row3, row4] == [Cell.PLAYER2] * 4:
                    return Status.PLAYER2_WON
        if self.table[0].count(None) == 0:
            return Status.DRAW
        return Status.PLAYING

field = Field()
print(field)
while True:
    for player in list(Cell):
        print("It's " + player.name + " turn")
        while True:
            print("Please input number: ")
            try:
                input_value = int(input())
            except ValueError:
                print("You can input number only")
                continue
            try:
                field.play(player, input_value - 1)
                break
            except IndexError:
                print("You can input 1 ~ ", field.get_column_size())
            except ValueError:
                print("You can input available number only")
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
            raise SystemError
