# write your code here

table = "         "
table = list(table)

x_turn = True
o_turn = False
x_cell_occupied = False
o_cell_occupied = False
game_on = True


while True:
    # table print
    print("---------")
    print("|", table[0], table[1], table[2], "|")
    print("|", table[3], table[4], table[5], "|")
    print("|", table[6], table[7], table[8], "|")
    print("---------")

    n = 3

    count_x = 0
    count_o = 0

    for char in table:
        if char == 'X':
            count_x += 1
        elif char == 'O':
            count_o += 1

    out_test = [(table[i:i+n]) for i in range(0, len(table), n)]

    x_wins = False
    o_wins = False

    if (out_test[0] == 'XXX' or out_test[1] == 'XXX' or out_test[2] == 'XXX'
            or out_test[0][0] == 'X' and out_test[1][0] == 'X' and out_test[2][0] == 'X'
            or out_test[0][1] == 'X' and out_test[1][1] == 'X' and out_test[2][1] == 'X'
            or out_test[0][2] == 'X' and out_test[1][2] == 'X' and out_test[2][2] == 'X'
            or out_test[0][0] == 'X' and out_test[1][1] == 'X' and out_test[2][2] == 'X'
            or out_test[0][2] == 'X' and out_test[1][1] == 'X' and out_test[2][0] == 'X'):
        x_wins = True

    if (out_test[0] == 'OOO' or out_test[1] == 'OOO' or out_test[2] == 'OOO'
            or out_test[0][0] == 'O' and out_test[1][0] == 'O' and out_test[2][0] == 'O'
            or out_test[0][1] == 'O' and out_test[1][1] == 'O' and out_test[2][1] == 'O'
            or out_test[0][2] == 'O' and out_test[1][2] == 'O' and out_test[2][2] == 'O'
            or out_test[0][0] == 'O' and out_test[1][1] == 'O' and out_test[2][2] == 'O'
            or out_test[0][2] == 'O' and out_test[1][1] == 'O' and out_test[2][0] == 'O'):
        o_wins = True

    if x_wins and o_wins or not x_wins and not o_wins and abs(count_x - count_o) >= 2:
        print("Impossible")
        game_on = False
    elif x_wins:
        print("X wins")
        game_on = False
    elif o_wins:
        print("O wins")
        game_on = False
    elif ' ' not in table:
        print("Draw")
        game_on = False

    if not game_on:
        break
    # input check
    user_coords = input("Enter the coordinates: ")
    if not user_coords[0].isdigit() or not user_coords[2].isdigit():
        print("You should enter numbers!")
        continue
    col = int(user_coords[0])
    row = int(user_coords[2])
    if col > 3 or row > 3 or col < 0 or row < 0 or len(user_coords) > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    # Turn changer
    if x_cell_occupied:
        x_turn = True
        o_turn = False
    elif o_cell_occupied:
        o_turn = True
        x_turn = False

    if not x_turn:
        o_turn = True

    # X and O placement
    user_coords = user_coords.split()
    while x_turn:
        x_turn = False
        if user_coords == ['1', '3']:
            if table[0] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[0] = 'X'
                break
        if user_coords == ['2', '3']:
            if table[1] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[1] = 'X'
                break
        if user_coords == ['3', '3']:
            if table[2] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[2] = 'X'
                break
        if user_coords == ['1', '2']:
            if table[3] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[3] = 'X'
                break
        if user_coords == ['2', '2']:
            if table[4] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[4] = 'X'
                break
        if user_coords == ['3', '2']:
            if table[5] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[5] = 'X'
                break
        if user_coords == ['1', '1']:
            if table[6] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[6] = 'X'
                break
        if user_coords == ['2', '1']:
            if table[7] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[7] = 'X'
                break
        if user_coords == ['3', '1']:
            if table[8] != ' ':
                print("This cell is occupied! Choose another one!")
                x_cell_occupied = True
                break
            else:
                table[8] = 'X'
                break

    while o_turn:
        o_turn = False
        x_turn = True
        if user_coords == ['1', '3']:
            if table[0] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[0] = 'O'
                break
        if user_coords == ['2', '3']:
            if table[1] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[1] = 'O'
                break
        if user_coords == ['3', '3']:
            if table[2] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[2] = 'O'
                break
        if user_coords == ['1', '2']:
            if table[3] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[3] = 'O'
                break
        if user_coords == ['2', '2']:
            if table[4] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[4] = 'O'
                break
        if user_coords == ['3', '2']:
            if table[5] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[5] = 'O'
                break
        if user_coords == ['1', '1']:
            if table[6] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[6] = 'O'
                break
        if user_coords == ['2', '1']:
            if table[7] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[7] = 'O'
                break
        if user_coords == ['3', '1']:
            if table[8] != ' ':
                print("This cell is occupied! Choose another one!")
                o_cell_occupied = True
                break
            else:
                table[8] = 'O'
                break
