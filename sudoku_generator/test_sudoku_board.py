#!/usr/bin/python3

""" Sudoku Board Testing Module
"""

from sudoku_cell import Cell
from dataclasses import asdict, astuple
from unittest import TestCase, main

class SudokuBoardTesting (TestCase):
    def test_cell (self):
        cell = Cell(0, 0, 0, 1)

        self.assertEqual(asdict(cell), {"row": 0, "column": 0, "section": 0, "value": 1})
        self.assertEqual(astuple(cell), (0, 0, 0, 1))

if __name__ == "__main__":
    main(verbosity=2)
