grid: list[str] = ["***", "***", "***"]
# grid
#   012      c
# 0 ***    r ***
# 1 ***      ***
# 2 ***      ***
EMPTY = '*'

def check_valid(r: int, c: int, grid: list[str]) -> bool:
    row_to_be_checked: str = grid[r]
    if row_to_be_checked[c] == EMPTY:
        return True
    return False

def ask_x() -> tuple[int, int] | None:
    while True:
        user_input: str = input("X: Enter your move: ") #format: X X
        r, c = map(int, user_input.split())
        if check_valid(r, c, grid):
            return r, c
        else:
            print(f"r = {r} and c = {c} are not valid.")

def ask_o() -> tuple[int, int] | None:
    while True:
        user_input: str = input("O: Enter your move: ") # format: X X
        r, c = map(int, user_input.split())
        if check_valid(r, c, grid):
            return r, c
        else:
            print(f"r = {r} and c = {c} are not valid.")

def get_x_move(r: int, c: int, grid: list[str]) -> str:
    row_string: str = grid[r]
    col_list: list[str] = list(row_string)
    col_list.pop(c)
    col_list.insert(c, 'x')
    return ''.join(col_list)

def get_o_move(r: int, c: int, grid: list[str]) -> str:
    row_string: str = grid[r]
    col_list: list[str] = list(row_string)
    col_list.pop(c)
    col_list.insert(c, 'o')
    return ''.join(col_list)

def tictactoe_simul(grid: list[str]) -> int:

    def print_grid(grid: list[str]):
        for i in range(0, 3):
            print(grid[i])

    def check_still_empty(grid: list[str]) -> bool:
        for row in grid:
            if EMPTY in row:
                return True
        return False
    
    def check_win_horizontals(grid: list[str]):
        state: bool = False
        for i in range(0, 3):
            if list(grid[i])[1] != EMPTY and list(grid[i])[1] == list(grid[i])[0] and list(grid[i])[1] == list(grid[i])[2]:
                state = True
        return state

    def check_win_verticals(grid:list[str]): 
        state: bool = False
        for i in range(0, 3):
            if list(grid[1])[i] != EMPTY and list(grid[1])[i] == list(grid[0])[i] and list(grid[1])[i] == list(grid[2])[i]:
                state = True
        return state

    def check_win_diagonals(grid:list[str]) -> bool:
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

if result == 0:
    print("It's a draw!")
elif result == 1:
    print("X wins!")
elif result == 2:
    print("O wins!")
else:
    print("Unforeseen Event!")
