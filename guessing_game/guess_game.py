#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

EASY_LEVEL = 5
HARD_LEVEL = 10

#Function to check user's guess.
def check_answer (guess, answer):
    if guess > answer:
        print ("Too high")
    elif guess < answer:
        print ("Too low")
    else:
        print(f"You got it. The answer is {answer}.")
        
#Function to check difficulty      
def set_difficulty (): 
    level = input(print("Do you want to play 'Easy' or 'hard' level?: "))
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
    

#Choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = randint(1, 100)

turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")

#Let the user guess a number
guess = int(input("Guess a number: "))

