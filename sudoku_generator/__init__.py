#!/usr/bin/python3

""" Generates a Sudoku, solved or ready to solve in a JSON file
"""

from sudoku import Sudoku
from random import shuffle, randint

def create_axis_values (values_range:int=10) -> tuple[int]:
    values_set: list[int] = []

    for i in range(values_range - 1):
        values_set.append(i + 1)
    
    shuffle(values_set)
    print(values_set)
    return tuple(values_set)

def create_sudoku (num_rows:int, num_columns:int, width_sections:int=0, height_sections:int=0, values_range:int=10, solved:bool=True):
    sudoku_obj = Sudoku(num_rows, num_columns, width_sections, height_sections)
    # complete_axis: tuple[int] = create_axis_values(values_range)
    complete_axis: tuple[int] = (1, 9, 2, 6, 7, 4, 5, 3, 8)

    row_number: int = sudoku_obj.num_rows // 2
    column_number: int = sudoku_obj.num_column // 2
    passed_rows: set[int] = {row_number}
    passed_columns: set[int] = {column_number}
    index_rows: set[int] = {i in range(sudoku_obj.num_rows)}
    index_columns: set[int] = {i in range(sudoku_obj.num_columns)}
    number: int = complete_axis[0]

    while True:
        action_number = randint(1, 3)

        # Random Row Index
        if action_number == 1:
            remaining_rows = passed_rows ^ index_rows
            remaining_numbers = set(sudoku_obj.columns[column_number]) ^ set(complete_axis)
            if len(remaining_rows) > 0 and len(remaining_numbers) > 0:
                row_number = remaining_rows[randint(0, len(remaining_rows))]
                number = remaining_numbers[randint(0, len(remaining_numbers))]
                value = sudoku[row_number][column_number]
                
                is_in_row = sudoku_obj.check_row(row_number, number)
                is_in_column = sudoku_obj.check_column(column_number, number)
                is_in_section = sudoku_obj.check_section(
                        sudoku_obj.get_section_index(row_number, column_number),
                        number
                        )

                if not is_in_row and not is_in_column and not is_in_section and value is None:
                    sudoku[row_number, column_number] = number
                    passed_rows.add(row_number)

        # Random Colum Index
        elif action_number == 2:
            remaining_columns = passed_columns ^ index_columns
            remaining_numbers = set(sudoku_obj.rows[row_number]) ^ set(complete_axis)
            if len(remaining_columns) > 0 and len(remaining_numbers) > 0:
                column_number = remaining_columns[randint(0, len(remaining_columns))]
                number = remaining_numbers[randint(0, len(remaining_numbers))]
                value = sudoku[row_number][column_number]
                
                is_in_row = sudoku_obj.check_row(row_number, number)
                is_in_column = sudoku_obj.check_column(column_number, number)
                is_in_section = sudoku_obj.check_section(
                        sudoku_obj.get_section_index(row_number, column_number),
                        number
                        )

                if not is_in_row and not is_in_column and not is_in_section and value is None:
                    sudoku[row_number, column_number] = number
                    passed_columns.add(column_number)

        # Random Section Index
        elif action_number == 3:
            

    # iterations: int = 0

    # while iterations != (sudoku_obj.num_rows * sudoku_obj.num_columns):
        # row_number = randint(0, sudoku_obj.num_rows - 1)
        # column_number = randint(0, sudoku_obj.num_columns - 1)
        # number = complete_axis[randint(0, len(complete_axis) - 1)]
        # value = sudoku_obj[row_number][column_number]

        # is_in_row = sudoku_obj.check_row(row_number, number)
        # is_in_column = sudoku_obj.check_column(column_number, number)
        # is_in_section = sudoku_obj.check_section(
                # sudoku_obj.get_section_index(row_number, column_number),
                # number
                # )

        # print(row_number, column_number, number)

        # if not is_in_row and not is_in_column and not is_in_section and value is None:
            # sudoku_obj[row_number, column_number] = number
            # iterations += 1

    # row_number: int = 0
    # for row in sudoku_obj.rows:
        # column_number: int = 0
        # for value in row:
            # for number in complete_axis:
                # # print(row_number, column_number)
                # is_in_row = sudoku_obj.check_row(row_number, number)
                # is_in_column = sudoku_obj.check_column(column_number, number)
                # is_in_section = sudoku_obj.check_section(
                        # sudoku_obj.get_section_index(row_number, column_number),
                        # number
                        # )
                # if not is_in_row and not is_in_column and not is_in_section and value is None:
                    # sudoku_obj[row_number, column_number] = number
                    # break
            # column_number += 1
        # row_number += 1

    # for number in complete_axis:
        # row_number: int = 0
        # column_number: int = 0
        # for row in sudoku_obj.rows:
            # column_number = 0
            # for value in row:
                # is_in_row = sudoku_obj.check_row(row_number, number)
                # is_in_column = sudoku_obj.check_column(column_number, number)
                # print(row_number, column_number, value, number)
                # is_in_section = sudoku_obj.check_section(
                        # sudoku_obj.get_section_index(row_number, column_number),
                        # number
                # )
                # if not is_in_row and not is_in_column and not is_in_section and value is None:
                    # sudoku_obj[row_number, column_number] = number
                    # break
                # column_number += 1
            # row_number += 1

    print(str(sudoku_obj))
                    
if __name__ == "__main__":
    create_sudoku(9, 9, width_sections=3, height_sections=3)
