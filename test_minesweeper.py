from functions_minesweeper import *
import pytest


def test_count_adjacent_mines_in_corner():
    board = [
             'X', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
               ]

    count = count_adjacent_mines(board, 0, 4)
    assert(count == 0)


def test_insert_mines_accuracy():
    blank_board = ['O'] * 25
    board = [
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'X', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
               ]
    position = [[2, 3]]
    updated_board = insert_mines(blank_board, position)
    assert (updated_board == board)


def test_count_adjacent_mines_no_diagonal():
    board = [
        'O', 'O', 'O', 'O', 'O',
        'O', 'X', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'X', 'X', 'O',
        'O', 'O', 'O', 'O', 'O',
    ]
    count = count_adjacent_mines(board, 3, 3)
    assert (count == 1)


def test_play_turn_found_mine():
    hidden_mine_board = [
        'X', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
    ]

    found_mine = play_turn(hidden_mine_board, 0, 0)
    assert (found_mine == '#')


def test_check_win_winning_example():
    board = [
        ' ', ' ', ' ', '1', ' ',
        ' ', ' ', '2', 'X', '1',
        ' ', '1', 'X', '2', ' ',
        ' ', ' ', '1', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ',
    ]
    assert check_win(board) is True
