#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo

print(logo)

def difficulty ():
    select_level = print("Do you want to play 'Easy' or 'hard' level?").lower()
    if select_level == "easy":
        attempts = 5
        print ("You have 5 attempts to the game.")
    elif select_level == "hard":
        attempts = 10
        print ("You have 5 attempts to the game.")


actual_number = 20
guess_number = int(input("Guess a number between 1 and 100"))
game_on = False


if guess_number > actual_number:
    print ("Too high")
elif guess_number < actual_number:
    print ("Too low")
elif guess_number == actual_number:
    print("You guessed right")