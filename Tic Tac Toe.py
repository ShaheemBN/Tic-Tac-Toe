def printBoard(boardLine1, boardLine3, boardLine5):
    l1 = ""
    for j in range(0, 9):
        l1 += boardLine1[j]
    print(l1)
    print("--+---+--")
    l2 = ""
    for j in range(0, 9):
        l2 += boardLine3[j]
    print(l2)
    print("--+---+--")
    l3 = ""
    for j in range(0, 9):
        l3 += boardLine5[j]
    print(l3)


gameEnd = False
index = 0
sub1Ind = 0
p = 0
xo1 = ""
xo2 = ""
board_line1 = list("  |   |  ")
board_line3 = list("  |   |  ")
board_line5 = list("  |   |  ")
numbers = list()
while not gameEnd:
    if index == 0:
        xo1 = input("Player 1, please input your choice of placement(X / O): ")
        xo1 = xo1.upper()
        while not(xo1 == "X" or xo1 == "O"):
            xo1 = input("Player 1, please input a valid letter(X / O): ")
            xo1 = xo1.upper()
        if xo1 == "X":
            xo2 = "O"
        else:
            xo2 = "X"
        print("Please type in numbers according to the square to print " + xo1 + " and " + xo2 + " as given below: ")
        print("1 | 2 | 3")
        print("--+---+--")
        print("4 | 5 | 6")
        print("--+---+--")
        print("7 | 8 | 9")
        index += 1
    elif index == 10:
        gameEnd = True
    else:
        okay = False
        while not okay:
            try:
                if sub1Ind == 0:
                    if index % 2 == 1:
                        p = int(input("Player 1, please type the number of the spot to place your " + xo1 + ": "))
                    else:
                        p = int(input("Player 2, please type the number of the spot to place your " + xo2 + ": "))
                    found = False
                    for i in range(0, len(numbers)):
                        if numbers[i] == p:
                            found = True
                    while found:
                        foundSub = False
                        p = int(input("Please input an available number: "))
                        for i in range(0, len(numbers)):
                            if numbers[i] == p:
                                foundSub = True
                        if not foundSub:
                            numbers.append(p)
                            found = False
                    sub1Ind += 1
                else:
                    p = int(input("Please input a valid number(1 to 9): "))
                    sub1Ind += 1
                if 0 < p < 10:
                    okay = True
            except ValueError:
                continue
        sub1Ind = 0
        numbers.append(p)
        if index % 2 == 1:
            if p == 1:
                board_line1[0] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 2:
                board_line1[4] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 3:
                board_line1[8] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 4:
                board_line3[0] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 5:
                board_line3[4] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 6:
                board_line3[8] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 7:
                board_line5[0] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 8:
                board_line5[4] = xo1
                printBoard(board_line1, board_line3, board_line5)
            elif p == 9:
                board_line5[8] = xo1
                printBoard(board_line1, board_line3, board_line5)
        else:
            if p == 1:
                board_line1[0] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 2:
                board_line1[4] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 3:
                board_line1[8] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 4:
                board_line3[0] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 5:
                board_line3[4] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 6:
                board_line3[8] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 7:
                board_line5[0] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 8:
                board_line5[4] = xo2
                printBoard(board_line1, board_line3, board_line5)
            elif p == 9:
                board_line5[8] = xo2
                printBoard(board_line1, board_line3, board_line5)
        if (board_line1[0] == "X" and board_line3[0] == "X" and board_line5[0] == "X") or \
                (board_line1[4] == "X" and board_line3[4] == "X" and board_line5[4] == "X") or \
                (board_line1[8] == "X" and board_line3[8] == "X" and board_line5[8] == "X") or \
                (board_line1[0] == "X" and board_line3[4] == "X" and board_line5[8] == "X") or \
                (board_line1[8] == "X" and board_line3[4] == "X" and board_line5[0] == "X"):
            if xo1 == "X":
                print("Player 1 won the game!\n Thank you for playing. See you soon.")
                gameEnd = True
            elif xo2 == "X":
                print("Player 2 won the game!\n Thank you for playing. See you soon.")
                gameEnd = True
        elif (board_line1[0] == "O" and board_line3[0] == "O" and board_line5[0] == "O") or \
                (board_line1[4] == "O" and board_line3[4] == "O" and board_line5[4] == "O") or \
                (board_line1[8] == "O" and board_line3[8] == "O" and board_line5[8] == "O") or \
                (board_line1[0] == "O" and board_line3[4] == "O" and board_line5[8] == "O") or \
                (board_line1[8] == "O" and board_line3[4] == "O" and board_line5[0] == "O"):
            if xo1 == "O":
                print("Player 1 won the game!\n Thank you for playing. See you soon.")
                gameEnd = True
            elif xo2 == "O":
                print("Player 2 won the game!\n Thank you for playing. See you soon.")
                gameEnd = True
        index += 1
