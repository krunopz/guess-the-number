#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from replit import clear
import random

def main():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")


  number=random.randint(1,100)
  decide=input("Choose difficulty. Type 'hard' or 'easy': ").lower()
  if decide=="easy":
    attempts=10
  else:
    attempts=5

  print(f"You have {attempts} left to guess the number.")


  def aiming(number, attempts):
    guess=int(input("Make a guess: "))
    if guess<number:
      attempts-=1
      print(f"Too low. You have {attempts} left. ")
    elif guess>number:
      attempts-=1
      print(f"Too high. You have {attempts} left. ")
    else:
      print(f"Nice job! You guessed it!")
      attempts=0
    return attempts

  while attempts!=0:
    attempts=aiming(number, attempts)

  again=input("Want to start again? Type 'yes' or 'no' ").lower()
  if again=="yes":
    clear()
    main()
  else:
    exit("Game over.")

main()