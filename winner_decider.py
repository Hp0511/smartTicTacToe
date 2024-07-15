def tictactoe_winner(board):
    '''
    Function that checks if someone, comp. or user, has won the tic-tac-toe game
    Inputs: board
    Outputs: Winner (win, lose, draw)
    Winner = 0 #The default is a draw
    '''
    #Horizontal check
    Winner = 69
    for i in range(0,9,3):
        if board[i] == board[i + 1] == board[i+2] == "X":
            Winner = 1 #first player win
            break
        elif board[i] == board[i + 1] == board[i+2] == "O":
            Winner = 2 #second player win
            break
    
    #Vertical check
    for i in range(0,3):
        if board[i] == board[i + 3] == board[i+6] == "X":
            Winner = 1 #first player win
            break
        elif board[i] == board[i + 3] == board[i+6] == "O":
            Winner = 2 #second player win
            break

    #Diagonal check
    if board[0] == board[4] == board[8] == "X" or board[2] == board[4] == board[6] == "X":
        Winner = 1 #first player win
    elif board[0] == board[4] == board[8] == "O" or board[2] == board[4] == board[6] == "O":   
        Winner = 2 #second player win
                  
    return Winner #1 is first player , 2 is second player, 0 is a draw

def test_tictactoe_winner(): #testing tictactoe_winner function
    case1 = ["X","O","X",
             "X","O","O", #test case 1 vertical
             "O","O","X"]
    
    case2 = ["X","O","X",
             "O","X","O", #test case 2 diagonal
             "O","O","X"]
    
    case3 = ["X","X","X",
             "X","O","O", #test case 3 horizontal
             "O","O","X"]
    
    assert tictactoe_winner(case1) == 2, "Case 1 is wrong"
    assert tictactoe_winner(case2) == 1, "Case 2 is wrong"
    assert tictactoe_winner(case3) == 1, "Case 3 is wrong"
    
    print("function tictactoe_winner is good")

test_tictactoe_winner()