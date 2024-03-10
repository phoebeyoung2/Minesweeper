def initialise_board():
    board = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
    return board


def display_board(board):
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

    for i in range(len(positions)):
        col = positions[i][1]
        col -= 1
        row = positions[i][0]
        row -= 1
        mine_position = (5*row) + col
        board[mine_position] = 'X'
    return board


def count_adjacent_mines(board, row, col):
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
    board = initialise_board()
    display_board(board)
    insert_mines(board, positions)
    hidden_mines = int(len(positions))
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
        print("Congrats you won!")
    elif mines_found > 0:
        print("Sorry, you lost!")
