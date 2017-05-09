# "Develop Another Python Program"
# CIS 640 - Tu/Th 1:05
# Author: Christian J. Hughes

# Checks that the given board configuration (a list of strings) has one winning (three-in-a-row/column/diagonal) pattern and returns the symbol used to form the winning pattern.
def tic_tac_toe_check(board):
    # Check to ensure that the board passed in is in fact a list
    if (type(board) != list):
        raise ValueError()

    # Check to see if the list passed in has 9 entires
    # This covers an empty list, or a list of wrong size
    if (len(board) != 9):
        raise ValueError()

    # Ensure that the list passed in does not contain any non-strings
    for symbol in board:
        if (type(symbol) != str):
            raise TypeError()

    # Ensure that there are only "x", "o", and "" symbols on the board
    for symbol in board:
        if (symbol != "x" and symbol != "o" and symbol != ""):
            raise ValueError()

    # Find the winning symbol.
    winCount = 0 # Number of winning patterns on the board
    winningSymbol = None # The symbol with a winning pattern

    # Check row 1
    if (check_for_three_in_a_row(board[0], board[1], board[2]) != None):
        winningSymbol = check_for_three_in_a_row(board[0], board[1], board[2])
        winCount += 1

    # Check row 2
    if (check_for_three_in_a_row(board[3], board[4], board[5]) != None):
        winningSymbol = check_for_three_in_a_row(board[3], board[4], board[5])
        winCount += 1

    # Check row 3
    if (check_for_three_in_a_row(board[6], board[7], board[8]) != None):
        winningSymbol = check_for_three_in_a_row(board[6], board[7], board[8])
        winCount += 1

    # Check column 1
    if (check_for_three_in_a_row(board[0], board[3], board[6]) != None):
        winningSymbol = check_for_three_in_a_row(board[0], board[3], board[6])
        winCount += 1

    # Check column 2
    if (check_for_three_in_a_row(board[1], board[4], board[7]) != None):
        winningSymbol = check_for_three_in_a_row(board[1], board[4], board[7])
        winCount += 1

    # Check column 3
    if (check_for_three_in_a_row(board[2], board[5], board[8]) != None):
        winningSymbol = check_for_three_in_a_row(board[2], board[5], board[8])
        winCount += 1

    # Check diag 1
    if (check_for_three_in_a_row(board[0], board[4], board[8]) != None):
        winningSymbol = check_for_three_in_a_row(board[0], board[4], board[8])
        winCount += 1

    # Check diag 2
    if (check_for_three_in_a_row(board[2], board[4], board[6]) != None):
        winningSymbol = check_for_three_in_a_row(board[2], board[4], board[6])
        winCount += 1

    # If no winning patterns were found, then return None
    if (winCount == 0):
        return None
    elif (winCount == 1): # One winning pattern was found
        return winningSymbol
    else: # More than one winning pattern was found
        raise ValueError()


# checks to see if there strings are equal, and equal to "x" or "o"
def check_for_three_in_a_row(sym1, sym2, sym3):
    if (sym1 == sym2 == sym3 and (sym1 == "x" or sym1 == "o")):
        return sym1
    else:
        return None


def run_tests():
    xWins = ["x","x","x","o","o","x","o","",""]
    oWins = ["o","x","x","","o","","","","o"]
    oWins2 = ["x","x","o","","o","","o","","x"]
    noWinner = ["x","","x","o","","","o","",""]
    multiWin = ["x","x","x","x","x","x","x","x","x"]
    multiWin2 = ["x","x","x","o","o","o","x","x","x"]
    badList = ["","","","","",""]
    badList2 = ["","","","","","","",4,2]
    badList3 = ["X","","","","","","","",""]
    notAList = 1
    print(tic_tac_toe_check(xWins))
    print(tic_tac_toe_check(oWins))
    print(tic_tac_toe_check(oWins2))
    print(tic_tac_toe_check(noWinner))
    print(tic_tac_toe_check(multiWin))
    print(tic_tac_toe_check(multiWin2))
    print(tic_tac_toe_check(badList))
    print(tic_tac_toe_check(badList2))
    print(tic_tac_toe_check(badList3))
    print(tic_tac_toe_check(notAList))
    # Should print:
        # "x"
        # "o"
        # "o"
        # None
        # ValueError
        # ValueError
        # ValueError
        # TypeError
        # ValueError
        # ValueError
