import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random
import stdio
import stddraw



CHOICES = ["rock", "paper", "scissors"]

def computer_win(player_choice, computer_choice):
    if computer_choice == 'rock' and player_choice == 'scissors':
        stdio.writeln('Computer wins')
    elif computer_choice == 'paper' and player_choice == 'rock':
        stdio.writeln("Computer wins")
    elif computer_choice == 'scissors' and player_choice == 'paper':
        stdio.writeln("Computer wins")
    elif computer_choice == player_choice:
        stdio.writeln("You drew")
    else: 
        stdio.writeln("You win")
    

def main():
    while True:
        stdio.writeln("User, choose between rock, paper or scissors")
        player_choice = stdio.readString().lower()
            
        if player_choice in CHOICES:
            computer_choice = random.choice(CHOICES)
            stdio.writeln("You threw " + player_choice + ", the computer threw " + computer_choice)
            
            computer_win(player_choice, computer_choice)
               
        else:
            stdio.writeln("You threw " + player_choice + ", which isn't valid")
        
        stdio.writeln("Would you like to play again? (y/n)")
        again = stdio.readString()
        
        if again.lower() == "n":
            stdio.writeln("Goodbye")
            break
        elif again != "y" and again != "n":
            stdio.writeln("This is an invalid answer, Goodbye")
            break
    
   
       

if __name__ == '__main__':
    main()




