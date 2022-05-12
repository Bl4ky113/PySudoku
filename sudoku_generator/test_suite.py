#!/usr/bin/python3

""" Testing for the Package, 
    - Sudoku Board Testing
"""

from unittest import TextTestRunner, TestSuite, TestLoader
from test_sudoku_board import SudokuBoardTesting

def run_test_suite (debug=False):
    """ Run TestCases in a TestSuite """

    board_testing_results = TestLoader().loadTestsFromTestCase(SudokuBoardTesting)

    test_suite = TestSuite((
        board_testing_results
        ))

    test_runner = TextTestRunner()
    test_runner.run(test_suite)

if __name__ == "__main__":
    run_test_suite()

