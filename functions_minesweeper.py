def initialise_board():
    """
    Initialises the blank minesweeper grid.

    Returns
    -------
    board : 1 x 25 list
            blank minesweeper grid

    Notes
    -----
    (post-condition 1) : All values in grid must be 'O'
    (post-condition 2) : The grid must have 25 items
    """
    board = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
    return board


def display_board(board):
    """
    Displays the minesweeper grid as a 5 x 5 board.

    Arguments
    --------
    board : 1 x 25 list
            Contains minesweeper operations

    Notes
    -----
    (precondition 1) : Input list must contain 25 items

    (post-condition 1) : Hidden mines 'X' must be displayed as 'O'
    (post-condition 2) : Board should display 'O', spaces and the number of adjacent mines
    """
    internal_board = board[:]
    i = 0

    while i in range(len(board)):
        if board[i] == 'X':
            internal_board[i] = 'O'
            i += 1
        else:
            internal_board[i] = board[i]
            i += 1

    j = 0
    while j in range(len(board)):
        print(internal_board[j:j+5])
        j += 5
    return


def insert_mines(board, positions):
    """
    Inserts mines on the board at the positions provided by the input

    Arguments
    ---------
    board     : 1 x 25 list
                Contains minesweeper operations
    positions : A list of 2 item lists
                Each 2 item list represents a mine location in the format [row, col]

    Returns
    -------
    board : Updated board with mines inserted at the specified locations

    Notes
    -----
    (precondition 1)   : Mine locations must be within the bounds of the 5 x 5 board
    (precondition 2)   : Input list representing the board must contain 25 items

    (post-condition 1) : Mines should be represented with the 'X' character
    """

    for i in range(len(positions)):
        col = positions[i][1]
        col -= 1
        row = positions[i][0]
        row -= 1
        mine_position = (5*row) + col
        board[mine_position] = 'X'
    return board


def count_adjacent_mines(board, row, col):
    """
    Counts the number of mines adjacent to the location specified by the row and column input

    Arguments
    --------
    board : 1 x 25 list
           Contains updated minesweeper operations
    row   : int
           Vertical location on the board
    col   : int
           Column (Horizontal) location on the board

    Returns
    -------
    counter : int
             The number of adjacent mines

    Notes
    -----
    (precondition 1)   : The row and col positions must be within the bounds of the board

    (Edge-case 1)      : A row or col position of 0 or 4 means there is 1 less adjacent position to check,
                         the function should alter the way it checks adjacent positions accordingly.
    """
    counter = 0
    mine_position = (5*row) + col

    if col < 4 and board[mine_position+1] == 'X':
        counter += 1

    if col > 0 and board[mine_position-1] == 'X':
        counter += 1

    if row > 0 and board[mine_position-5] == 'X':
        counter += 1

    if row < 4 and board[mine_position+5] == 'X':
        counter += 1

    return counter


def play_turn(board, row, col):
    """
    Plays a turn on the board in the specified row and column location.

    Arguments
    ---------
    board : 1 x 25 list
           Contains updated minesweeper operations
    row   : int
           Vertical location on the board
    col   : int
           Column (Horizontal) location on the board

    Returns
    -------
    board                 : 1 x 25 list
                            Contains updated minesweeper operations
    board[mine_position] : str
                           The new character inserted on the board that has resulted from the turn played

    Notes
    -----
    (precondition 1)   : row and col positions must be within bounds of the grid

    (post-condition 1) : If a hidden mine is selected it must be replaced wih '#'
    (post-condition 2) : If there are mines adjacent to the location, a string representation of the number of adjacent
                         mines must replace the existing character
    (post-condition 3) : If there is no adjacent mine or hidden mine, the existing character is replaced with a space
    """
    counter = count_adjacent_mines(board, row, col)
    mine_position = (5*row) + col

    if board[mine_position] == 'X':
        board[mine_position] = '#'
    elif counter > 0 and board[mine_position] == 'O':
        board[mine_position] = counter
    elif counter == 0 and board[mine_position] == 'O':
        board[mine_position] = ' '

    return board[mine_position]


def check_win(board):
    """
    Determines if a player has won the game.

    Arguments
    ---------
    board : 1 x 25 list
           Contains updated minesweeper operations

    Returns
    -------
    bool : True if a player has won, False if it has not been won

    Notes
    -----
    (pre-condition 1)  : 'O' represents positions that have not yet been selected,
                         '#' represents found mines, and 'X' represents hidden mines
    (pre-condition 2)  : Any string representing a number is the number of adjacent mines

    (post-condition 1) : The game has been won if all positions have been selected and no mines have been found
    (post-condition 2) : If the function returns false, it does not mean the game has been lost,
                         it just means the game has not been won

    """
    i = 0
    position_counter = 0
    hidden_mines = 0
    found_mines = 0

    for i in range(len(board)):
        if board[i] == 'O':
            position_counter += 1
        if board[i] == 'X':
            hidden_mines += 1
        if board[i] == '#':
            found_mines += 1
    i += 1

    if position_counter == 0 and found_mines == 0:
        return True
    else:
        return False


def play_game(positions):
    """
    Can use the preceding functions to play a full game of minesweeper.

    Arguments
    ---------
    positions : a list of lists
                locations of the mines placed on the board

    Notes
    -----
    (pre-condition 1) : The mine positions are within the bounds of the grid

    (post-condition 1) : The initial board is first displayed with an input command for the user
                         to play their first turn
    (post-condition 2) : After each turn is played, the current state of the board is displayed and
                         another input command is posed to the user to play their next turn
    (post-condition 3) : When the user selects a mine location, the final board
                         is displayed with the message "Sorry, you lost!"
    (post-condition 4) : When the user wins the game, the final board is displayed with the
                         message "Congrats, you won!"

    """
    board = initialise_board()
    display_board(board)
    insert_mines(board, positions)
    mines_found = 0

    while not check_win(board) and mines_found == 0:

        position_list = []
        position_list = input("Enter row and column position in the format 'row column':")
        col_string = position_list[2]
        row_string = position_list[0]
        row_integer = int(row_string)
        column_integer = int(col_string)
        row_integer -= 1
        column_integer -= 1

        mine_position = (5*row_integer) + column_integer
        play_turn(board, row_integer, column_integer)
        if board[mine_position] == '#':
            mines_found += 1
        display_board(board)

    if check_win(board):
        print("Congrats, you won!")
    elif mines_found > 0:
        print("Sorry, you lost!")
