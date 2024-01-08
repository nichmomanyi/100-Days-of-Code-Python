from art import logo, vs
from game_data import data
import random

# Display art
print (logo)

#Format the account data into printable format
def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

##Get follower count on each account
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#Generate a random account for the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_b == account_a:
    account_b = random.choice(data)
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")


score = 0
#Ask for user a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#check if user is correct
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
check_answer()
##use if statement to check if user is correct
is_correct = check_answer(guess, a_follower_count, b_follower_count)
#Give user feedback on their guess
if is_correct:
    score  += 1
    print(f"You're right!. Current score: {score}")
else:
    print(f"Sorry, that's wrong. Final score: {score}")

#Score keeping

#Make the game repeatable

#Making account at position B become the next position A

#Clear the screen between rounds