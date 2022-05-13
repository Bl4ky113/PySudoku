#!/usr/bin/python3

""" Sudoku Board Testing Module
"""

from sudoku_cell import Cell
from sudoku_board import Board
from dataclasses import asdict, astuple
from unittest import TestCase, main

class SudokuBoardTesting (TestCase):
    def test_cell (self):
        cell = Cell(0, 0, 0, 1)

        self.assertEqual(asdict(cell), {"row": 0, "column": 0, "section": 0, "value": 1})
        self.assertEqual(astuple(cell), (0, 0, 0, 1))

    def test_row_column_section_properties (self):
        board = Board(9, 9, 3, 3)
        self.assertEqual(board.num_sections_per_row, 3)
        self.assertEqual(board.num_sections_per_column, 3)

        board = Board(6, 6, 2, 2)
        self.assertEqual(board.num_sections_per_row, 3)
        self.assertEqual(board.num_sections_per_column, 3)

    def test_check_min_max_sections (self):
        with self.assertRaises(ValueError) as context:
            board = Board(9, 9, 9, 9)

        self.assertTrue("Board Must Have At Least 2 Sections" in str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            board = Board(9, 9, 1, 1)

        self.assertTrue("Board Can't Have a Section For Each Row or Column" in str(context.exception))

    def test_cell_values (self):
        pass

    def test_use_initial_number_list (self):
        pass

if __name__ == "__main__":
    main(verbosity=2)
