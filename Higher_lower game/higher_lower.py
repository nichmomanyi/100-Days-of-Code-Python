#Compare A vs B
#Who has more followers? Type 'A' or 'B': 

#if answer is correct, print "Your current score: {1++}"
#compare the correct answer which now A vs another choise B

#if answer now not correct, print "Sorry, that's wrong final score: {1++}"
#break the loop
from game_data import data
import random
#EXAMPLE OUTPUTS
#Compare A: 9GAG, a Social media platform, from China.
A = random.choice(data)
B = random.choice(data)

score = 0
is_correct = True
    
while is_correct:
    choice_a = print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    choice_b = print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if user_choice == 'A' and A["follower_count"] > B["follower_count"]:
        score += 1
        print(f"Your current score: {score}")
        B = random.choice(data)
    elif user_choice == 'B' and B["follower_count"] > A["follower_count"]:
        score += 1
        print(f"Your current score: {score}")
        B = random.choice(data)      
    else:
        score += 1
        print("Sorry, that's wrong final score: {score}")
        break

