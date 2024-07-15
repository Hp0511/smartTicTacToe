def instruction(board):
    '''This function provdes the instruction for the player about the tictactoe game'''
    print("Tic Tac Toe is a game for two players, who take turns marking the spaces in a 3x3 grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. This program will have two modes: single player where you can play with the computer or multiplayer where you can play with your friend")
    print("You will be provided a board like this where you could type in your move like in chess: A1,A2,A3,B1,B2,B3,C1,C2,C3")
    print("    A"  + "   B"   + "   C")
    print("1 | " + board[0] + " | " +  board[1] + " | " +  board[2])
    print("2 | " + board[3] + " | " +  board[4] + " | " +  board[5])
    print("3 | " + board[6] + " | " +  board[7] + " | " +  board[8])
    print("Good luck have fun!")
    return

def drawgrid(boardstate, board):
    '''Function that transforms boardstate onto board
    Inputs: boardstate, board
    Outputs: board
    '''
    # Map the boardstate to the board
    for key, value in boardstate.items():
        col = ord(key[0]) - ord('A') #calculate the order of the column
        row = int(key[1]) - 1 #calculate the order of the row
        index = 3*row + col #calculate the index base on the row and the column

        if value == 1:
            board[index] = "X"
        elif value == 2:
            board[index] = "O"
        else:
            board[index] = "-"

    print("    A"  + "   B"   + "   C")
    print("1 | " + board[0] + " | " +  board[1] + " | " +  board[2])
    print("2 | " + board[3] + " | " +  board[4] + " | " +  board[5])
    print("3 | " + board[6] + " | " +  board[7] + " | " +  board[8])

    return board

def test_drawgrid():
    board1 = ["-","-","-",
              "-","-","-",
              "-","-","-"]
    
    boardstate1 = {"A1":1, "A2":2, "A3":1, "B1":2, "B2":1, "B3":2, "C1":1, "C2":2, "C3":1} #test case 1
    board1result = ["X","O","X",
                    "O","X","O",
                    "X","O","X"]
    

    assert drawgrid(boardstate1,board1) == board1result

    board2 = ["-","-","-",
              "-","-","-",
              "-","-","-"]
    boardstate2 = {"A1":1, "A2":0, "A3":1, "B1":2, "B2":0, "B3":2, "C1":1, "C2":2, "C3":1}
    board2result = ["X","O","X",
                    "-","-","O",
                    "X","O","X"]
    
    assert drawgrid(boardstate2,board2) == board2result

    board3 = ["-","-","-",
              "-","-","-",
              "-","-","-"]
    boardstate3 = {"A1":0, "A2":0, "A3":0, "B1":0, "B2":0, "B3":0, "C1":0, "C2":0, "C3":0}

    assert drawgrid(boardstate3,board3) == board3
    
    print("Drawgrid function is good")
    return

test_drawgrid()