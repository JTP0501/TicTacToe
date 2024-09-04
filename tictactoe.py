grid: list[str] = ["▫▫▫", "▫▫▫", "▫▫▫"]
# grid
#   012      c
# 0 ▫▫▫    r ▫▫▫
# 1 ▫▫▫      ▫▫▫
# 2 ▫▫▫      ▫▫▫
EMPTY = '▫'

def check_valid(r: int, c: int, grid: list[str]) -> bool:
    
    """ This function checks if the cell at r,c is empty or not """
    
    row_to_be_checked: str = grid[r]
    if row_to_be_checked[c] == EMPTY:
        return True
    return False

def ask_x() -> tuple[int, int]:
    
    """ This function asks for X's move """

    while True:
        user_input: str = input("X: Enter your move: ") #format: X X
        try:
            r, c = map(int, user_input.split())
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")
            continue        
        
        if not (0 <= r <= 2 and 0 <= c <= 2):
            print("Invalid input for row/column.")
            continue

        if check_valid(r, c, grid):
            return r, c
        else:
            print(f"Row {r} with Col {c} is not empty")

def ask_o() -> tuple[int, int]:

    """ This function asks for O's move """

    while True:
        user_input: str = input("O: Enter your move: ") # format: X X
        
        try:
            r, c = map(int, user_input.split())

        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")
            continue
        if not(0 <= r <= 2 and 0 <= c <= 2):
            print("Invalid input for row/column.")
            continue

        if check_valid(r, c, grid):
            return r, c
        else:
            print(f"Row {r} with Col {c} is not empty")

def get_x_move(r: int, c: int, grid: list[str]) -> str:

    """ This function does X's move """

    row_string: str = grid[r]
    col_list: list[str] = list(row_string)
    col_list.pop(c)
    col_list.insert(c, 'x')
    return ''.join(col_list)

def get_o_move(r: int, c: int, grid: list[str]) -> str:
    
    """ This function does O's move """
    
    row_string: str = grid[r]
    col_list: list[str] = list(row_string)
    col_list.pop(c)
    col_list.insert(c, 'o')
    return ''.join(col_list)

def tictactoe_simul(grid: list[str]) -> int:

    """ This function runs the tic tac toe game """

    def print_grid(grid: list[str]):
        
        """ This function prints the current state of the grid """

        print("0 1 2".rjust(28))
        for i in range(0, 3):
            formatted_string: str = ' '.join(grid[i])
            print(f"{i} {formatted_string}".rjust(28))
        print()

    def check_still_empty(grid: list[str]) -> bool:

        """ This function checks if the entire grid still has some empty cells """

        for row in grid:
            if EMPTY in row:
                return True
        return False
    
    def check_win_horizontals(grid: list[str]):

        """ This function checks for any horizontal wins """

        state: bool = False
        for i in range(0, 3):
            if list(grid[i])[1] != EMPTY and list(grid[i])[1] == list(grid[i])[0] and list(grid[i])[1] == list(grid[i])[2]:
                state = True
        return state

    def check_win_verticals(grid:list[str]): 

        """ This function checks for any vertical wins """

        state: bool = False
        for i in range(0, 3):
            if list(grid[1])[i] != EMPTY and list(grid[1])[i] == list(grid[0])[i] and list(grid[1])[i] == list(grid[2])[i]:
                state = True
        return state

    def check_win_diagonals(grid:list[str]) -> bool:

        """ This function checks for any diagonal wins """

        state: bool = False
        character_to_check: str = list(grid[1])[1]
        if character_to_check == EMPTY:
            return state 
        else:
            if list(grid[0])[0] == character_to_check and list(grid[2])[2] == character_to_check:
                state = True
            elif list(grid[2])[0] == character_to_check and list(grid[0])[2] == character_to_check:
                state = True
        return state

    print("▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫  TIC TAC TOE  ▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫")
    print_grid(grid)
    while check_still_empty(grid):
        
        rx: int = 0
        cx: int = 0
        ro: int = 0
        co: int = 0

        rx, cx = ask_x()
        new_row: str = get_x_move(rx, cx, grid)
        grid.pop(rx)
        grid.insert(rx, new_row)
        
        print("After X's Move: ")
        print_grid(grid)

        if check_win_horizontals(grid) or check_win_verticals(grid) or check_win_diagonals(grid):
            return 1

        ro, co = ask_o()
        new_row: str = get_o_move(ro, co, grid)
        grid.pop(ro)
        grid.insert(ro, new_row)

        print("After O's Move:")
        print_grid(grid)

        if check_win_horizontals(grid) or check_win_verticals(grid) or check_win_diagonals(grid):
            return 2
         
    return 0

result: int = tictactoe_simul(grid)

# Result is printed

if result == 0:
    print("It's a draw!")
elif result == 1:
    print("X wins!")
elif result == 2:
    print("O wins!")
else:
    print("Unforeseen Event!")
