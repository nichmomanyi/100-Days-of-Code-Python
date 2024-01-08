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

#Generate a random account for the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_b == account_a:
    account_b = random.choice(data)
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")


#Ask for user a guess

#check if user is correct
##Get follower count on each account
##use if statement to check if user is correct

#Give user feedback on their guess

#Score keeping

#Make the game repeatable

#Making account at position B become the next position A

#Clear the screen between rounds