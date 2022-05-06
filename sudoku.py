#!/usr/bin/python3

class SudokuAxis ():
    def __init__ (self, num_values:int, num_lines:int):
        self.axis_values: list[list[int]] = [[None for _ in range(num_values)] for _ in range(num_lines)]

    def __getitem__ (self, index:int):
        return self.axis_values[index]

    def __setitem__ (self, index:int, value:int):
        self.axis_values[index] = value

    def __iter__ (self):
        return iter(self.axis_values)

class Sudoku ():
    def __init__ (self, num_rows, num_columns):
        self.num_rows: int = num_rows
        self.num_columns: int = num_columns
        self.__rows = SudokuAxis(num_columns, num_rows)
        self.__columns = SudokuAxis(num_rows, num_columns)

    def __getitem__ (self, index:int):
        return self.__rows[index]

    def __setitem__ (self, index:tuple, value:int):
        if len(index) != 2:
            raise IndexError("Index must be [x, y]")

        i, j = index

        self.__rows[i][j] = value
        self.__columns[j][i] = value

    def __str__ (self):
        string: str = ""

        index: int = 0
        string += "Row ->\n"
        for row in self.__rows:
            string += f"{index} | {row}\n"
            index += 1
    
        index: int = 0
        string += "Column ->\n"
        for column in self.__columns:
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
