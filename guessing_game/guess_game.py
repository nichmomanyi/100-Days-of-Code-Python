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

EASY_LEVEL = 10
HARD_LEVEL = 5

#Function to check user's guess.
def check_answer (guess, answer, turns):
    """Checks answer against guess. Returns number of turns remaining"""
    if guess > answer:
        print ("Too high")
        print("Guess again")
        return turns - 1
    elif guess < answer:
        print ("Too low")
        print("Guess again")
        return turns - 1
    else:
        print(f"You got it. The answer is {answer}.")
        
#Function to check difficulty      
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
    
def game():
    print(logo)
#Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    print(f"Pssst, The answer is : {answer}")
    turns = set_difficulty()
    
    #Let the user guess a number
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))
        if turns == 1:
            print("You run out of guesses, You lose.")
            return
        turns = check_answer(guess, answer, turns)
game()