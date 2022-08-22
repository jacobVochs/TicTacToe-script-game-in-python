import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


player_dict = {"p1":"","p2":""}
field_list = [" "," "," "," "," "," "," "," "," "," "]
marks_checklist = [field_list[0:9:4],field_list[2:7:2],field_list[0:7:3],field_list[1:8:3],
                   field_list[2:9:3],field_list[0:3],field_list[3:6],field_list[6:9]]
active_player = ""
X_points = 0
O_points = 0
moves = 9
gameon_choice = "wrong"
insert_coin = "error"
  
def restart_game():
    global gameon_choice
    global field_list
    global player_dict
    global active_player
    global moves

    active_player = ""
    field_list = [" "," "," "," "," "," "," "," "," "," "]
    moves = 9
    gameon_choice = "wrong"

def end_game():
    global gameon_choice
    global field_list
    global player_dict
    global active_player
    global X_points
    global O_points
    global moves
    global insert_coin
    player_dict = {"p1":"","p2":""}
    active_player = ""
    field_list = [" "," "," "," "," "," "," "," "," "," "]
    X_points = 0
    O_points = 0
    moves = 9
    gameon_choice = "wrong"
    insert_coin = "error"


marks_checklist = [field_list[1:10:4],field_list[3:8:2],field_list[1:8:3],field_list[2:9:3],
                   field_list[3:10:3],field_list[1:4],field_list[4:7],field_list[7:10]]





def win_check():
    global X_points
    global O_points
    marks_checklist = [field_list[1:10:4],field_list[3:8:2],field_list[1:8:3],field_list[2:9:3],
                   field_list[3:10:3],field_list[1:4],field_list[4:7],field_list[7:10]]
    for group in marks_checklist:
        
        if group == ['X','X','X']:
            X_points +=1
            

            print("X wins")
            return True
        elif group == ['O', 'O', 'O']:
            O_points +=1
            

            print( "O wins")
            return True 
    else:
        return False



def tie_check():
    if moves == 0:
        print("TIE")
        return True
    else:
        return False



def display_board():    

    

    empty_line = "    |  "" |"
    hr_line = "-------------"
    num_line79 = "  ""7 ""|"" 8 ""|"" 9"" "
    num_line46 = "  ""4 ""|"" 5 ""|"" 6"" "
    num_line13 = "  ""1 ""|"" 2 ""|"" 3"" "
    

    empty_line_aligned = empty_line.rjust(30)
    hr_line_aligned = hr_line.rjust(30) 
    num_line79_aligned = num_line79.rjust(29) 
    num_line46_aligned = num_line46.rjust(29)
    num_line13_aligned = num_line13.rjust(29)

    print("==============================================================")
    print("                                                             ")
    print("                                                             ")
    print("                                                             ")
    print("    |  "" |",empty_line_aligned)
    print(" ",field_list[7] ,"|",field_list[8] ,"|",field_list[9] ," ",num_line79_aligned)
    print("    |  "" |",empty_line_aligned)
    print("-------------",hr_line_aligned)
    print("    |  "" |",empty_line_aligned)
    print(" ",field_list[4] ,"|",field_list[5] ,"|",field_list[6] ," ",num_line46_aligned)
    print("    |  "" |",empty_line_aligned)
    print("-------------",hr_line_aligned)
    print("    |  "" |",empty_line_aligned)
    print(" ",field_list[1] ,"|",field_list[2] ,"|",field_list[3] ," ",num_line13_aligned)
    print("    |  "" |",empty_line_aligned)
    print("                                                             ")
    print("                                                             ")
    print("                                                             ")
    print("==============================================================")

from IPython.display import clear_output


def choose_side():
    side_choice = "wrong"
    while side_choice != 'X' and side_choice != 'O':
        
        side_choice = input('Do you want to play X or O?: ')
       
        if side_choice != 'X' or 'x' and side_choice != 'O' or 'o':
            clear_output()
            print('Please choose X or O')
           
           
    return side_choice


def player_assignment():
    player_one = choose_side()
    player_two = ""
    if player_one == "X":
        player_two = "O"
    elif player_one == "O":
        player_two = "X"
    player_dict['p1'] = player_one
    player_dict['p2'] = player_two
    print("Player 1: ",player_one,"Player 2: ",player_two)
    return player_dict

import random
import time


def who_starts(player_dict):
    global active_player

    num = random.randint(1,100)
    print("")
    print("Starting draw who starts...")
    print("")
    time.sleep(1.5)
    if num % 2 == 0:
        print("Player 1 starts")
        active_player = player_dict['p1']
        return active_player
    else:
        print("Player 2 starts") 
        active_player = player_dict['p2']
        return active_player


def whos_next():
    global active_player
    if active_player == 'O':
        active_player = 'X'
    elif active_player == 'X':
        active_player = 'O'
        
    return active_player

def player_field_choice():

    global active_player
    global moves
    occupied = False
    num_choice = "wrong"
    while num_choice.isdigit() == False or num_choice not in ['1','2','3','4','5','6','7','8','9'] or occupied == False:
        display_board()
        print("")
        print("X: ",X_points," O: ",O_points)
        print("Player ",active_player," turn")
        num_choice = input("Choose a number from 1 to 9:")
        
        
        if num_choice.isdigit() == False:
            clear_output()
            print("This is not an integer, please type a number from 1 to 9")
            
        elif num_choice not in ['1','2','3','4','5','6','7','8','9']:
                clear_output()
                print("Number out of range, please type a number from 1 to 9")
                
    
        elif field_list[int(num_choice)] == 'O' or field_list[int(num_choice)] == 'X':
            clear_output()
            print("This field is already taken, please choose other field.")
            occupied = False
        
        elif field_list[int(num_choice)] == ' ':
            occupied = True
                    
    if active_player == 'X':
        clear_output()

        moves -= 1
        field_list[int(num_choice)] = "X"
        cls()
        display_board()
        
      
    
    elif active_player == 'O':
        clear_output()

        moves -= 1
        field_list[int(num_choice)] = "O"
        cls()
        display_board()

      

    
    active_player = whos_next()
    
def play_again():
    global gameon_choice
    while gameon_choice != 'y'and gameon_choice != 'n':
        gameon_choice = input('Do you want to play again? y/n')
        if gameon_choice != 'y'and gameon_choice != 'n':
            clear_output()
            print('Please type "y" for Yes or "n" for No.')
            
        return gameon_choice


def launch():
    global insert_coin
    while insert_coin != 'y' and insert_coin != 'n':
        insert_coin = input('Game start? y/n')
        if insert_coin != 'y' and insert_coin != 'n':
            clear_output()
            print('Please type "y" for Yes or "n" for No.')
            

def game_start():
    player_assignment()
    who_starts(player_dict)
    while win_check() == False and tie_check() == False:



        clear_output()
        player_field_choice()
    play_again()

def game_on():
    who_starts(player_dict)
    while win_check() == False and tie_check() == False:
        clear_output()
        player_field_choice()



    play_again()



def game():
    global X_points
    global O_points
    game_start()
    while gameon_choice == 'y':
        restart_game()
        game_on()
    if gameon_choice == 'n':
        if X_points > O_points:
            print("X: ",X_points," O: ",O_points)
            print("And the winner is Player X with ",X_points," points.")
            end_game()
        elif X_points < O_points:
            print("X: ",X_points," O: ",O_points)
            print("And the winner is Player O with ",O_points," points.")
            end_game()
        elif X_points == O_points:
            print("X: ",X_points," O: ",O_points)
            print("Draw, X got ",X_points," O got ",O_points)
            end_game()
  
    
def tic_tac_toe():
    print('Welcome to Tic Tac Toe!')
    launch()
    if insert_coin == 'y':
        game()
    elif insert_coin == 'n':
        print("GAME OVER")
        end_game()
        
tic_tac_toe()