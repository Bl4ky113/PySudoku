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
    def __init__ (self, num_rows, num_columns):
        """ States the number of rows and columns,
            then creates a SudokuAxis instance for each 
            one with the given number size.
        """
        self.num_rows: int = num_rows
        self.num_columns: int = num_columns
        self.rows = SudokuAxis(num_columns, num_rows)
        self.columns = SudokuAxis(num_rows, num_columns)

    def __getitem__ (self, index:int):
        """ Returns row element """
        return self.rows[index]

    def __setitem__ (self, index:tuple, value:int):
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

def test_sudoku ():
    separator = "-" * 20

    test = Sudoku(4, 6)
    print(str(test))

    print(separator)
    print(test[0][1])
    test[0, 1] = "hello"
    print(test[0])
    print(test[0][1])

    print(str(test))

if __name__ == "__main__":
    test_sudoku()
