"""
This program implements a simple Tic-Tac-Toe game in Python.
It allows one or two players to make moves and determines the winner or if it's a draw.
Author: Huy Phan and Chuck
Date: 12/08/2023
"""
import random
from move_generator import computer_move
from graphic import instruction, drawgrid
from winner_decider import tictactoe_winner


def tictactoe_input(boardstate,player_turn):
    '''Function that asks the user for a input and checks if that input is possible, if not it re-asks for an input
    Inputs:Boardstate
    Outputs:Updated Boardstate
    '''
    print("Your move must be a position on the grid, B2 for example")
    legal = False
    while not legal:
        try:
            move = input("What is your move? ")
            move = move.upper()
            assert move in boardstate.keys()  #checks if input is right format or an option
            assert boardstate[move]!=1  #checks if space is taken
            assert boardstate[move]!=2
            legal = True
        except AssertionError:
            print("Your move is invalid or the spot is taken. Retry")
            continue
    
    boardstate[move] = player_turn
    return boardstate


def singleplayermode(boardstate,board):
    """
    This function simulates a single player mode of a Tic Tac Toe game. The player can choose to go first or second against the computer.

    Parameters:
    boardstate (list): A list representing the current state of the game board.
    board (list): A list representing the game board.

    Returns:
    None
    """
    numberofmoves = 0 #to calculate how many is left
    player_turn = 1
    computer_turn = 2
    check = 0 #check if the player win or not

    #checking if the player want to go first or not
    while True:
        user_input = input("Do you want to go first? Yes/No?  ")
        if user_input == "Yes" or user_input == "yes":
            break
        elif user_input == "No" or user_input == "no":
            player_turn = 2
            computer_turn = 1
            break
        else:
            print("Please enter Yes/No only")

    #If the player decide to go first
    if player_turn == 1:
        while numberofmoves < 9: #run all 9 spaces in the board
            tictactoe_input(boardstate,player_turn) #ask the player to input
            drawgrid(boardstate,board) #draw the board
            check = tictactoe_winner(board) #check the status of the board
            if check == player_turn:
                print("Congratulations, you have won!")
                break
            if "-" not in board: #check for a draw
                break
            print("Here is the computer move:")
            computer_move(boardstate,computer_turn,player_turn) #computer to move
            drawgrid(boardstate,board) #update on the board
            check = tictactoe_winner(board) #check the winner
            if check == computer_turn:
                print("Don't be sad, try again")
                break
            if "-" not in board: #check for a draw
                break
            numberofmoves = numberofmoves + 1
    
    #If the player decides to go second
    else:
        while numberofmoves < 9:
            print("Here is the computer move:")
            computer_move(boardstate,computer_turn,player_turn) #the computer goes first
            drawgrid(boardstate,board) #update move on board
            check = tictactoe_winner(board) #update on winner
            if check == computer_turn:
                print("Don't be sad, try again")
                break
            if "-" not in board: #check for a draw
                break
            tictactoe_input(boardstate,player_turn) #ask the player for input
            drawgrid(boardstate,board) #update on the board
            check = tictactoe_winner(board) #update on the status
            if check == player_turn:
                print("Congratulations, you have won!")
                break
            numberofmoves = numberofmoves + 1
            if "-" not in board: #check for a draw
                break

    if check == 0:
        print("It's a draw")
    return

def multiplayermode(boardstate,board):
    """
    This function simulates a multi player mode of a Tic Tac Toe game. Two players can play together until one wins or both draw

    Parameters:
    boardstate (list): A list representing the current state of the game board.
    board (list): A list representing the game board.

    Returns:
    None
    """
    numberofmoves = 0 #to calculate how many is left
    check = 0 #check if the player win or not
    player1 = 1 
    player2 = 2

    while numberofmoves < 9:
        print("Player 1 please enter your move")
        tictactoe_input(boardstate,player1) #let player 1 enter
        drawgrid(boardstate,board) #update on board
        check = tictactoe_winner(board) #check if the winner wins
        if check == player1:
            print("Congratulations, player 1 have won!")
            break
        if "-" not in board:
            break
        print("Player 2 please enter your move")
        tictactoe_input(boardstate,player2) #ask the player 2 to input
        drawgrid(boardstate,board) #update on the board
        check = tictactoe_winner(board) #check on winner
        if check == player2:
            print("Congratulations, player 2 have won!")
            break
        numberofmoves = numberofmoves + 1
        if "-" not in board:
            break

    if check == 0:
        print("It is a draw")
    return

def main():
    boardstate = {"A1":0, "A2":0, "A3":0, "B1":0, "B2":0, "B3":0, "C1":0, "C2":0, "C3":0}
    board = ["-","-","-",
             "-","-","-",
             "-","-","-"]
    instruction(board) # print the instruction
    while True:
        try:
            players = int(input("How many people are playing, 1 or 2? ")) #asking single player or multiplayer
    #entering singleplayer
            if players == 1:#single player mode
                singleplayermode(boardstate,board)
                break
            elif players == 2:#multiplayermode
                multiplayermode(boardstate,board)
                break
            else:
                print ("Invalid number of players")
        except ValueError:
            print("Please enter 1 or 2 only")
    print("Thanks for playing")

main()