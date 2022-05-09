#!/usr/bin/python3

""" Generates a Sudoku, solved or ready to solve in a JSON file
"""

from sudoku import Sudoku
from random import shuffle

def create_axis_values (values_range:int=10) -> tuple[int]:
    values_set: list[int] = []

    for i in range(values_range - 1):
        values_set.append(i + 1)
    
    print(values_set)
    shuffle(values_set)
    print(values_set)
    return tuple(values_set)

def create_sudoku (num_rows:int, num_columns:int, values_range:int=10, solved:bool=True):
    sudoku_obj = Sudoku(num_rows, num_columns)
    complete_axis: tuple[int] = create_axis_values(values_range)
    
    for number in complete_axis:
        row_number: int = 0
        column_number: int = 0
        for row in sudoku_obj.rows:
            column_number = 0
            for column in row:
                if number not in row and number not in sudoku_obj.columns[column_number] and column is None:
                    sudoku_obj[row_number, column_number] = number
                    break
                column_number += 1
            row_number += 1
    # for row in sudoku_obj.rows:
        # column_number = 0
        # for value in row:
            # for number in complete_axis:
                # if number not in row and number not in sudoku_obj.columns[column_number]:
                    # sudoku_obj[row_number, column_number] = number
                    # break

    print(str(sudoku_obj))
                    
if __name__ == "__main__":
    create_sudoku(9, 9)
