#!/usr/bin/python3

""" Creates a Sudoku Obj, which values can be returned as a 
    row, column, and invidiualy.
"""

class SudokuAxis ():
    """ Axis of the Sudoku. Works as Columns or Rows. 
        Each axis, and axis value, can be access using []
    """
    def __init__ (self, num_values:int, num_lines:int):
        """ Creates and fills a list with None 
            This list contains each axis and its values
        """
        self.axis_values: list[list[int]] = [[None for _ in range(num_values)] for _ in range(num_lines)]

    def __getitem__ (self, index:int):
        """ Returns axis element """
        return self.axis_values[index]

    def __setitem__ (self, index:int, value:int):
        """ Sets axis element """
        self.axis_values[index] = value

    def __iter__ (self):
        """ Returns the axis values list as a iterable element """
        return iter(self.axis_values)

class Sudoku ():
    """ Sudoku Obj, stores the rows and columns values, 
        can return them by accessing with [] or using each axis 
        property and access values with []
    """
    def __init__ (self, num_rows:int, num_columns:int, section_width:int=0, section_height:int=0):
        """ States the number of rows, columns
            size of inter sections (cubes),
            then creates a SudokuAxis instance for each 
            axis with the given number size.
            If the size of inter sections is not passed, they'll be
            the same as the number of rows and columns
        """
        self.num_rows: int = num_rows
        self.num_columns: int = num_columns
        self.rows = SudokuAxis(num_columns, num_rows)
        self.columns = SudokuAxis(num_rows, num_columns)

        if section_width <= 0 or section_height <= 0:
            self.section_width: int = self.num_rows
            self.section_height: int = self.num_columns
        else:
            self.section_width: int = section_width
            self.section_height: int = section_height

    def __getitem__ (self, index:int):
        """ Returns row element """
        return self.rows[index]

    def __setitem__ (self, index:tuple[int, int], value:int):
        """ Checks if index is [x, y] and changes the value 
            in the row "x" and cloumn "y" with the given value
        """
        if len(index) != 2:
            raise IndexError("Index must be [x, y]")

        i, j = index

        self.rows[i][j] = value
        self.columns[j][i] = value

    def __str__ (self):
        """ Converts all sudoku values, rows and columns separated, into a string """
        string: str = ""

        index: int = 0
        string += "Row ->\n"
        for row in self.rows:
            string += f"{index} | {row}\n"
            index += 1
    
        index: int = 0
        string += "Column ->\n"
        for column in self.columns:
            string += f"{index} | {column}\n"
            index += 1

        return string
    
    @property
    def __num_squares (self):
        """ Calculates the number of inter sections on the sudoku with
            the number or rows and columns or the sudoku, divided by 
            the width and height of each section
        """
        squares_by_rows: int = self.num_rows // self.section_width
        squares_by_columns: int = self.num_columns // self.section_height
        total_squares: int = squares_by_rows * squares_by_columns

        return total_squares

    def __get_square(self, square_index:int):
        """ Gets the values of a Inter Section in the sudoku by a given index
            using the values of rows and number of rows, columns of the sudoku and 
            width, height of each section.
            Returns the values in a tuple in this order (row[0][value_1], row[0][value_n], row[n][value_1] ...)
        """
        if square_index > (self.__num_squares - 1) or square_index < 0:
            raise IndexError("Square Index out of range")

        square_values: list[int] = []

        row_index: int = (square_index // (self.num_rows // self.section_width)) * self.section_height
        value_index: int = (square_index % (self.num_columns // self.section_height)) * self.section_height
    
        for row in self.rows[row_index:(row_index + self.section_width)]:
            for j in range(self.section_height):
                square_values.append(row[j + value_index])

        return tuple(square_values)

    def check_row (self, row_index:int, value:int):
        """ Checks if values is in given square by index """
        return value in self.rows[row_index]

    def check_column (self, column_index:int, value:int):
        """ Checks if value is in given square by index """
        return value in self.column[column_index]

    def check_square (self, square_index:int, value:int):
        """ Checks if value is in given square by index """
        square: tuple[int] = self.__get_square(square_index)
        return value in square

def test_sudoku ():
    test = Sudoku(9, 9, 3, 3)
    
    num_row = 0
    for row in test.rows:
        num_column = 0
        for column in row:
            test[num_row, num_column] = str(num_row) + str(num_column)
            num_column += 1
        num_row += 1

    print(str(test))

    print(test.check_square(0, "10"))
    print(test.check_square(1, 10))
    print(test.check_square(2, 10))
    print(test.check_square(3, 10))
    print(test.check_square(4, 10))
    print(test.check_square(5, 10))
    print(test.check_square(6, 10))
    print(test.check_square(7, 10))
    print(test.check_square(8, 10))

if __name__ == "__main__":
    test_sudoku()
