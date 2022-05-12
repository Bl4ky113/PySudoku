#!/usr/bin/python3

""" Cell Class for each invividual cell in the Sudoku Board.
    Containing the position information in the board and its value.
    Default, "Empty" value is 0
"""

from dataclasses import dataclass

@dataclass
class Cell ():
    row: int
    column: int
    section: int
    value: int = 0
