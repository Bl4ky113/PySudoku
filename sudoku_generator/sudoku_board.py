#!/usr/bin/python3

""" Sudoku Board, base of the game. 
    Contains Rows, Columns and Inter Sections
"""

from dataclasses import dataclass, field
from sudoku_cell import Cell

@dataclass
class Board ():
    num_rows: int = 9
    num_columns: int = 9
    width_section: int = 3
    height_section: int = 3
    
    rows: set[Cell] = field(default_factory=set)
    columns: set[Cell] = field(default_factory=set)
    sections: set[Cell] = field(default_factory=set)
    cells: list[Cell] = field(default_factory=list)

    initial_number_list: list[int] = field(default_factory=list)

    def __post_init__ (self):
        self.num_sections_per_row: int = self.num_rows // self.width_section
        self.num_sections_per_column: int = self.num_columns // self.height_section
        self.num_sections:int = self.num_sections_per_row * self.num_sections_per_column
        
        if self.num_sections < 2:
            raise ValueError("Board Must Have At Least 2 Sections")
        elif self.num_sections_per_row == self.num_rows or self.num_sections_per_column == self.num_columns:
            raise ValueError("Board Can't Have a Section For Each Row or Column")

        for row in range(num_rows):
            for column in range(num_columns):
                section: int = self.height_section * (row // self.num_sections_per_row) + (column // self.num_sections_per_column)

                cell: Cell = Cell(row, column, box)
                
                if len(self.initial_number_list) != 0:
                    cell.value = self.initial_number_list.pop()

                if row not in self.rows:
                    self.rows[row]: list[Cell] = []
                
                if column not in self.columns:
                    self.columns[column]: list[Cell] = []

                if section not in self.sections:
                    self.sections[section]: list[Cell] = []

                self.rows[row].append(cell)
                self.columns[column].append(cell)
                self.sections[section].append(cell)
                self.cells.append(cell)
