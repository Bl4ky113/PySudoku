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
        self.rows = SudokuAxis(num_columns, num_rows)
        self.columns = SudokuAxis(num_rows, num_columns)
        self.num_rows = num_rows
        self.num_columns = num_columns

    def __str__ (self):
        string = ""

        index = 0
        string += "Row ->\n"
        for row in self.rows:
            string += f"{index} | {row}\n"
            index += 1
    
        index = 0
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
    print(test.rows[0])
    print(test.rows[0][0])
    test.rows[0] = None
    test.rows[1][0] = "hello"
    print(test.rows[0])
    print(test.rows[1])
    print(test.rows[1][0])

if __name__ == "__main__":
    test_sudoku()
