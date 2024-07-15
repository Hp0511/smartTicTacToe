import random

def computer_move(boardstate, computer_turn, player_turn):
    '''This function decides the best option for computer's move depending on the board state
    Inputs: list of moves, computer_turn, player turn
    Output: Updated boardstate with computer move
    '''
    # Winning combinations
    winning_combinations = [
        ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
        ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"], #The combination of winning the game
        ["A1", "B2", "C3"], ["A3", "B2", "C1"]
    ]
    #check if the computer can win
    win_move = 0 
    for combination in winning_combinations:
        win_move = 0
        for computer_move in combination:
            if boardstate[computer_move] == computer_turn: 
                win_move += 1
        if win_move == 2: #If the computer is having 2 and almost wins
            for computer_move in combination:
                if boardstate[computer_move] != player_turn and boardstate[computer_move] != computer_turn:#check if that space is taken
                    boardstate[computer_move] = computer_turn
                    return boardstate
    
    #check if the computer can block if the players is going to win
    for combination in winning_combinations:
        win_move = 0
        for computer_move in combination:
            if boardstate[computer_move] == player_turn:
                win_move += 1
        if win_move == 2: #If the player is about to win in 1 more
            for computer_move in combination:
                if boardstate[computer_move] != player_turn and boardstate[computer_move] != computer_turn: #check if that space is taken
                    boardstate[computer_move] = computer_turn
                    return boardstate

    # If neither player nor computer is about to win, make a random move
    while True:
        randint = random.randrange(9)  # Randomize the move for computer

        if randint == 0:
            move = "A1"
        elif randint == 1:
            move = "A2"
        elif randint == 2:
            move = "A3"
        elif randint == 3:
            move = "B1"
        elif randint == 4:
            move = "B2"
        elif randint == 5:
            move = "B3"
        elif randint == 6:
            move = "C1"
        elif randint == 7:
            move = "C2"
        else:
            move = "C3"

        if boardstate[move] != player_turn and boardstate[move] != computer_turn:  # Check if the space is taken or not
            boardstate[move] = computer_turn
            return boardstate
            break

def test_computer_move():
    computer_turn = 1
    player_turn = 2

    case_1 = {"A1":1, "A2":1, "A3":0, "B1":2, "B2":0, "B3":0, "C1":2, "C2":0, "C3":0} #test the case that the computer is about to win

    case_2 = {"A1":2, "A2":2, "A3":0, "B1":1, "B2":0, "B3":0, "C1":1, "C2":0, "C3":0} #test the case that the computer blocks the player move

    #Testing
    assert computer_move(case_1,computer_turn,player_turn) == {"A1":1, "A2":1, "A3":1, "B1":2, "B2":0, "B3":0, "C1":2, "C2":0, "C3":0}  #testing case 1

    assert computer_move(case_2,computer_turn,player_turn) == {"A1":2, "A2":2, "A3":1, "B1":1, "B2":0, "B3":0, "C1":1, "C2":0, "C3":0}  #testing case 2

    print("the computer runs smooth")
    return

test_computer_move()