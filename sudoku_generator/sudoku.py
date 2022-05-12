#!/usr/bin/python3

""" Creates a Sudoku Obj, which values can be returned as a 
    row, column, inter section, and invidiualy.
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
    def __init__ (self, num_rows:int, num_columns:int, section_width:int=0, section_height:int=0) -> None:
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

    def __setitem__ (self, index:tuple[int, int], value:int) -> None:
        """ Checks if index is [x, y] and changes the value 
            in the row "x" and cloumn "y" with the given value
        """
        if len(index) != 2:
            raise IndexError("Index must be [x, y]")

        i, j = index

        self.rows[i][j] = value
        self.columns[j][i] = value

    def __str__ (self) -> str:
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
    def __sections_by_rows (self) -> int:
        """ Calculates the number of sections by rows 
            dividing the number of them by the width of each section
        """
        return self.num_rows // self.section_width

    @property
    def __sections_by_columns (self) -> int:
        """ Calculates the number of sections by columns
            dividing the number of them by the height of each section
        """
        return self.num_columns // self.section_height

    @property
    def __num_section (self) -> int:
        """ Calculates the number of sections by multipling the 
            number of sections by columns and rows
        """
        return self.__sections_by_columns * self.__sections_by_rows

    def __get_section(self, section_index:int) -> tuple[int]:
        """ Gets the values of a Inter Section in the sudoku by a given index
            using the values of rows and number of rows, columns of the sudoku and 
            width, height of each section.
            Returns the values in a tuple in this order (row[0][value_1], row[0][value_n], row[n][value_1] ...)
        """
        if section_index > (self.__num_section - 1) or section_index < 0:
            raise IndexError("Section Index out of range")

        section_values: list[int] = []

        row_index: int = (section_index // self.__sections_by_rows) * self.section_height
        value_index: int = (section_index % self.__sections_by_columns) * self.section_height
    
        for row in self.rows[row_index:(row_index + self.section_width)]:
            for j in range(self.section_height):
                section_values.append(row[j + value_index])

        return tuple(section_values)

    def get_section_index (self, row_index:int, column_index:int) -> int:
        """ Uses a row and column index to calulate the 
            equivalent section index
        """
        section_row = (row_index // self.__sections_by_rows)
        section_column = (column_index // self.__sections_by_columns)

        return section_row + (section_column * self.__sections_by_columns)

    def check_row (self, row_index:int, value:int) -> bool:
        """ Checks if values is in given square by index """
        return value in self.rows[row_index]

    def check_column (self, column_index:int, value:int) -> bool:
        """ Checks if value is in given square by index """
        return value in self.columns[column_index]

    def check_section (self, section_index:int, value:int) -> bool:
        """ Checks if value is in given section by index """
        section: tuple[int] = self.__get_section(section_index)
        return value in section

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

if __name__ == "__main__":
    test_sudoku()
