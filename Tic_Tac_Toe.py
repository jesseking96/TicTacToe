#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:26:10 2019

@author: skyking
"""

'''
This project is a Tic Tac Toe game for 2 players. One player will be X and the
other will be O. Players will select positions on the board using the numbers
1-9, corresponding to the position of numbers on the numpad of a typical
keyboard. At the beginning, and between each turn, the game will print out a
visual representation of the game board. The program will check for win
conditions between each turn, and announce the winner if a win condition is
met. The program will then give the user the option to play again, or to quit.
'''

from random import randint

def get_letter():
    '''
    Prompts Player 1 to choose a marker, X or O, and returns that choice.
    '''
    
    while True:
        p1 = input("Player 1, would you like to be X or O? ")
        if p1.upper() == "X" or p1.upper() == "O":
            return p1.upper()
        print("Invalid input. Try again.\n")

       
def goes_first():
    '''
    Randomly selects which player will go first, informs the user of the
    result, and returns that result
    '''
    
    first_turn = randint(1,2)
    print("Player {} goes first!".format(first_turn))
    return first_turn

def play_turn(current_player):
    '''
    Prompts the current player to make a move, and records that move
    on the game board.
    '''
    
    while True:
        move = int(input("Player {}, select a move (1-9): ".format(current_player)))
        if move in range(1,10) and game_board[move-1] == ' ':
            game_board[move-1] = markers[current_player]
            break
        else:
            print("Invalid input. Try again.\n")
    
            
         
    
def check_win(game_board, marker):
    '''
    Checks for win conditions on the board by checking each row, each column,
    and the two diagonals.
    '''
    for i in range(0,3):
        counter = 0
        for j in range(i,i+7,3):
            if game_board[j] == marker:
                counter +=1
        if counter == 3:
            return True
        
    for i in range(0,7,3):
        counter = 0
        for j in range(i,i+3):
            if game_board[j] == marker:
                counter += 1
        if counter == 3:
            return True
        
    if game_board[0] == game_board[4] ==  game_board[8] == marker:
        return True
    if game_board[2] == game_board[4] == game_board[6] == marker:
        return True
    return False
        
            
        
        
def update_player(current_player):
    '''
    Updates the current player, and returns the updated current player
    '''
    
      
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    return current_player
          
def is_game_over(game_board):
    '''
    checks if there are still remaining moves to be made on the board.
    '''
    
    return not ' ' in game_board
    
def play_again():
    '''
    Asks the user if they would like to play again.
    '''
    
    while True:
        
        again = input("Would you like to play again (Y/N)? ")
        if again.upper() == 'Y' or again.upper() == 'N':
            return again.upper() == 'Y'
        else:
            print("Invalid input. Try again. ")

def print_game_board(game_board):
    '''
    Prints 100 new lines to clear the board, then prints the current state
    of the game board.
    '''
    
    print('\n' * 100)
    print('''
           {} | {} | {} 
          ---|---|---
           {} | {} | {} 
          ---|---|---
           {} | {} | {} '''.format(game_board[6], game_board[7], game_board[8],
           game_board[3], game_board[4], game_board[5], game_board[0],
           game_board[1], game_board[2]))

game_board = [' '] * 9
print_game_board(game_board)

play_game = True
while play_game:
    
    game_board = [' '] * 9
    
    win_condition = False
    game_over = False
    
    markers = {1: get_letter()}
    if markers[1] == 'X':
        markers[2] = 'O'
    else:
        markers[2] = 'X'
    
    current_player = goes_first()
    
    while not win_condition and not game_over:
        play_turn(current_player)
        print_game_board(game_board)
        win_condition = check_win(game_board, markers[current_player])
        if not win_condition:
            game_over = is_game_over(game_board)
            current_player = update_player(current_player)
    
    if win_condition:
        print("Player {} wins!".format(current_player))
    else:
        print("Game over!")
    play_game = play_again()
        
        
    
    
    
    
