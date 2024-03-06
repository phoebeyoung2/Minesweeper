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
        row = positions[i][0]
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
    initial_board = initialise_board()
    hidden_mines_board = initialise_board()
    non_hidden_mines_board = insert_mines(initial_board, positions)
    display_board(hidden_mines_board)

    while not check_win(non_hidden_mines_board):

        row = int(input("Enter row number:"))
        col = int(input("Enter col number:"))

        row -= 1
        col -= 1
        mine_position = (5*row) + col

        play_turn(non_hidden_mines_board, row, col)
        hidden_mines_board[mine_position] = non_hidden_mines_board[mine_position]
        display_board(hidden_mines_board)

    if check_win(non_hidden_mines_board) == bool(1):
        print("You won!")
        return
