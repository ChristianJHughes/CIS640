# "EC1"
# CIS 640 - Tu/Th 1:05
# Author: Christian J. Hughes

import impl
import pytest

class TestTicTacToeCheck:

    # Non-list should raise TypeError`.
    def test_tic_tac_toe_check_non_list_value(self):
        with pytest.raises(TypeError):
            impl.tic_tac_toe_check(0)

    # Empty list should raise ValueError.
    def test_tic_tac_toe_check_empty_board(self):
        with pytest.raises(ValueError):
            impl.tic_tac_toe_check([])

    # List with any non-string data types should raise TypeError.
    def test_tic_tac_toe_check_board_with_non_strings(self):
        with pytest.raises(TypeError):
            board = ["","","","","","","",4,2]
            impl.tic_tac_toe_check(board)

    # List with elements not equal to 9 should raise ValueError
    def test_tic_tac_toe_check_board_of_incorrect_length(self):
        with pytest.raises(ValueError):
            board = ["","","","","",""]
            impl.tic_tac_toe_check(board)

    # Valid board with no winning pattern should return None.
    def test_tic_tac_toe_check_(self):
        noWinner = ["x","","x","o","","","o","",""]
        result = impl.tic_tac_toe_check(noWinner)
        assert result == None

    # Valid board with no plays should return None.
    def test_tic_tac_toe_check_unplayed_valid_board(self):
        noWinner = ["","","","","","","","",""]
        result = impl.tic_tac_toe_check(noWinner)
        assert result == None

    # Multiple winning patterns by the same symbol should raise ValueError.
    def test_tic_tac_toe_check_multi_win_same_symbol(self):
        with pytest.raises(ValueError):
            multiWinSameSymbol = ["x","x","x","x","x","x","x","x","x"]
            impl.tic_tac_toe_check(multiWinSameSymbol)

    # Multiple winning patterns by different symbols should raise ValueError
    def test_tic_tac_toe_check_multi_win_different_symbols(self):
        with pytest.raises(ValueError):
            multiWinDiffSymbol = ["x","x","x","o","o","o","x","x","x"]
            impl.tic_tac_toe_check(multiWinDiffSymbol)

    # Make sure the correct winning symbol if x is a winner.
    def test_tic_tac_toe_check_returns_valid_winner(self):
        xWins = ["x","x","x","o","o","x","o","",""]
        result = impl.tic_tac_toe_check(xWins)
        assert result == "x"

    # Make sure the correct winning symbol if y is a winner.
    def test_tic_tac_toe_check_returns_valid_winner(self):
        oWins = ["o","x","x","","o","","","","o"]
        result = impl.tic_tac_toe_check(oWins)
        assert result == "o"

    # Board with strings beyond "x","o", and "" should raise ValueError
    def test_tic_tac_toe_check_invalid_symbols(self):
        with pytest.raises(ValueError):
            incorrectSymbolBoard = ["o","o","o","z","","","","",""]
            impl.tic_tac_toe_check(incorrectSymbolBoard)
